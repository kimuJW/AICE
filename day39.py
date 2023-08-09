from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report

lg = LogisticRegression(C=1.0,max_iter=2000)
lg.fit(X_train, y_train)

lg = LogisticRegression(C=1.0,max_iter=2000)
lg.fit(X_train, y_train)

lg_pred = lg.predict(X_test)

# 오차행렬
# TN  FP
# FN  TP

confusion_matrix(y_test, lg_pred)

# 정확도 : 굉장히 높다
accuracy_score(y_test, lg_pred)  

# 정밀도
precision_score(y_test, lg_pred) 

# 재현율 : 굉장히 낮다.
recall_score(y_test, lg_pred)  

# 정밀도 + 재현율
f1_score(y_test, lg_pred) 

print(classification_report(y_test, lg_pred))
accuracy_eval('LogisticRegression', lg_pred, y_test)