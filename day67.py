from sklearn.ensemble import RandomForestRegressor as rfr
from sklearn.metrics import roc_auc_score, accuracy_score, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns


train_y = np.ravel(train_y, order='C')

model=rfr(n_estimators=100,max_depth=5,min_samples_split=30,min_samples_leaf=15)
model.fit(train_x, train_y)

pred_y = model.predict(test_x)
print("RMSE on Test set : {0:.5f}".format(mean_squared_error(test_y,pred_y)**0.5))
print("R-squared Score on Test set : {0:.5f}".format(r2_score(test_y,pred_y)))

rf_importances_values = model.feature_importances_
rf_importances = pd.Series(rf_importances_values, index = train_x.columns)
rf_top10 = rf_importances.sort_values(ascending=False)[:10]

plt.rcParams["font.family"] = 'NanumGothicCoding'
plt.figure(figsize=(8,6))
plt.title('Top 10 Feature Importances')
sns.barplot(x=rf_top10, y=rf_top10.index,palette = "RdBu")
plt.show()