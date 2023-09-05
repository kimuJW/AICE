from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression as lr
from sklearn.metrics import roc_auc_score, accuracy_score, mean_squared_error, r2_score
!pip install statsmodels

results = sm.OLS(train_y, train_x).fit()

results.summary()

train_x, test_x, train_y, test_y = train_test_split(df_feature, df_target, test_size=0.20, random_state=42)

model=lr()
model.fit(train_x, train_y)

print("모델의 회귀계수는 : ", model.coef_, "이고 모델의 절편은 : ",model.intercept_)

pred_y = model.predict(test_x)
print("RMSE on Test set : {0:.5f}".format(mean_squared_error(test_y,pred_y)**0.5))
print("R-squared Score on Test set : {0:.5f}".format(r2_score(test_y,pred_y)))