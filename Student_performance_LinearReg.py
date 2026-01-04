import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, root_mean_squared_error, r2_score

df = pd.read_csv('Student_Performance.csv')
#encode extracurricular 1yes 0no
df['Extracurricular Activities'] = (df['Extracurricular Activities']=='Yes').astype(int)
#print(df[['Extracurricular Activities','Hours Studied']])
target = df[df.columns[-1]].values
features = df[df.columns[:-1]].values


x = np.array(features,dtype=float)
y = np.array(target,dtype=float)

## split data
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.2,random_state=42)

#fit data

LR_model = LinearRegression()
LR_model.fit(train_x,train_y)
y_test_pred = LR_model.predict(test_x)
print(y_test_pred)
#print(LR_model.intercept_) #b0 = -33.92
print(LR_model.coef_) #ARRAY OF SLOPE

#Model evaluation
MSE = mean_squared_error(test_y,y_test_pred)
RMSE = root_mean_squared_error(test_y,y_test_pred)
R_squared = r2_score(test_y,y_test_pred)#0.988
print(R_squared)



