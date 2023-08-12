from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=3, random_state=42)
rfc.fit(X_train, y_train)
rfc_pred = rfc.predict(X_test)
accuracy_eval('RandomForest Ensemble', rfc_pred, y_test)