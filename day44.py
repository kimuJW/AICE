!pip install lightgbm
from lightgbm import LGBMClassifier

lgbm = LGBMClassifier(n_estimators=3, random_state=42)   # 1분 소요
lgbm.fit(X_train, y_train)
lgbm_pred = lgbm.predict(X_test)
accuracy_eval('LGBM', lgbm_pred, y_test)