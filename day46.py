final_outputs = {
    'DecisionTree': dt_pred, 
    'randomforest': rfc_pred, 
    'xgb': xgb_pred, 
    'lgbm': lgbm_pred,
    'stacking': stacking_pred,
}

final_prediction=\
final_outputs['DecisionTree'] 
+final_outputs['randomforest'] 
+final_outputs['xgb'] 
+final_outputs['lgbm'] 
+final_outputs['stacking'] 

final_prediction = np.where(final_prediction > 0.5, 1, 0)
accuracy_eval('Weighted Blending', final_prediction, y_test)