!pip install xgboost
from xgboost import XGBClassifier
xgb = XGBClassifier(n_estimators=3, random_state=42)  # 10초 소요
xgb.fit(X_train, y_train)
xgb_pred = xgb.predict(X_test)
accuracy_eval('XGBoost', xgb_pred, y_test)