from sklearn.ensemble import StackingRegressor, StackingClassifier
stack_models = [
    ('LogisticRegression', lg), 
    ('KNN', knn), 
    ('DecisionTree', dt),
]

stacking = StackingClassifier(stack_models, final_estimator=rfc, n_jobs=-1)
stacking.fit(X_train, y_train)
stacking_pred = stacking.predict(X_test)
accuracy_eval('Stacking Ensemble', stacking_pred, y_test)