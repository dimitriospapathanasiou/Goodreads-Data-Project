import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import roc_curve, roc_auc_score

df = pd.read_csv('cleaned_books.csv')
df['high_rating'] = (df['average_rating'] >= 4.0).astype(int)
df['log_ratings_count'] = np.log1p(df['ratings_count'])
df['log_text_reviews_count'] = np.log1p(df['text_reviews_count'])
df['rating_density'] = df['ratings_count'] / (df['num_pages'] + 1)
df['popularity_index'] = df['ratings_count'] * df['average_rating']

features = ['num_pages', 'log_ratings_count', 'rating_density', 'popularity_index']
X = df[features].fillna(0)
y = df['high_rating']

# Normalization
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

class_0 = df[df['high_rating'] == 0]
class_1 = df[df['high_rating'] == 1]
class_0_undersampled = class_0.sample(len(class_1), random_state=42)
df_balanced = pd.concat([class_0_undersampled, class_1])

X_balanced = df_balanced[features].fillna(0)
y_balanced = df_balanced['high_rating']
X_balanced = scaler.fit_transform(X_balanced)
X_train, X_test, y_train, y_test = train_test_split(X_balanced, y_balanced, test_size=0.2, random_state=42)
clf = GradientBoostingClassifier(n_estimators=200, learning_rate=0.1, max_depth=6, random_state=42)
clf.fit(X_train, y_train)

# Cross-validation
cv_scores = cross_val_score(clf, X_balanced, y_balanced, cv=5, scoring='accuracy')
print("Cross-Validation Accuracy: {:.4f}".format(np.mean(cv_scores)))

y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
feature_importances = clf.feature_importances_
feature_importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importances})
print("\nFeature Importance:\n", feature_importance_df.sort_values(by='Importance', ascending=False))

# Feature Importance
plt.figure(figsize=(8, 6))
plt.barh(feature_importance_df['Feature'], feature_importance_df['Importance'], color='skyblue')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Feature Importance')
plt.gca().invert_yaxis()
plt.show()

y_proba = clf.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
roc_auc = roc_auc_score(y_test, y_proba)
print("AUC: {:.4f}".format(roc_auc))

# ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', label=f'ROC Curve (AUC = {roc_auc:.4f})')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--', label='Random Classifier')
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend()
plt.grid()
plt.show()
