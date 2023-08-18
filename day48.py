from sklearn.model_selection import train_test_split

cal_cols = ['class', 'sex', 'stop', 'npay', 'termination', 'bill_rating']
df1 = pd.get_dummies(data=df, columns=cal_cols, drop_first=True)
df1.info()

X = df1.drop('termination_Y', axis=1).values
y = df1['termination_Y'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.3, 
                                                    stratify=y,
                                                    random_state=42)

X_train.shape
y_train.shape