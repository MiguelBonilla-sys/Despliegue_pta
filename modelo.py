import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

df = pd.read_csv(r'Data\input_data_ptap_f.csv', sep=';')
print(df.info())

x = df.drop('Eficiencia', axis=1)
y = df['Eficiencia']

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
xgb_regressor = XGBRegressor()
xgb_regressor.fit(xtrain, ytrain)
y_pred_xgb = xgb_regressor.predict(xtest)

print("Mean squared error: ", mean_squared_error(ytest, y_pred_xgb))

pickle.dump(xgb_regressor, open(r'regre_ptap.pkl', 'wb'))
