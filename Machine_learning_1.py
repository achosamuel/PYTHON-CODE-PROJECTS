# ---Code from scratch the Linear regression---
# import necessaries libraries
from cProfile import label

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error, mean_squared_error, r2_score
#print(np.__version__)
#print(pd.__version__)

hours_x = [1,2,3,4,5,6,7,8,9,10]
scores = [52,58,66,71,82,94,110,119,127,135]

x = np.array(hours_x,dtype=int)
y = np.array(scores,dtype=int)
#print(f'hours x shape : {x.shape}, scores y shape :{y.shape}')

plt.figure()
plt.scatter(x,y)
plt.xlabel("Hours studied")
plt.ylabel("Scores")
plt.title("Hours studied vs Scores plot")
#plt.show()

#split data train 80/test 20
rng = np.random.default_rng(121)
idx = np.arange(len(x))
rng.shuffle(idx)

split = int(len(x)*0.8)

train_idx,test_idx = idx[:split],idx[split:]

train_x, train_y = x[train_idx],y[train_idx]
test_x, test_y = x[test_idx],y[test_idx]

#Fitting on train only
#line equation y = mx + b
# m = cov(x,y)/var(x)
m = np.cov(train_x,train_y,bias=True)[0,1]/np.var(train_x)
#b = y_bar - m* x_bar
b = np.mean(train_y) - m*np.mean(train_x)

#Evaluation on test only
predict_y = [int(m*i + b) for i in test_x]
#print(test_x)
#print(predict_y)

#Performance evaluation
MSE = sum((predict_y - test_y)**2)/len(test_y) #58.0
#print(MSE)
RMSE = np.sqrt(MSE) #11.42
RSS = sum((test_y-predict_y)**2) #261
TSS = sum((test_y-np.mean(test_y))**2) #72.0
R_squarred = 1 - (RSS/TSS) #-0.61
#print(R_squarred)

#Prediction for news Hours
new_hours = np.array([12,18,24,27,78])
new_prediction = b + m* new_hours
print(new_prediction)

#Plotting of trend line
plot_x = np.linspace(min(x),max(x),100)
plot_y = b + m*plot_x

plt.figure()
plt.scatter(train_x,train_y,label='Train')
plt.plot(plot_x,plot_y)
#plt.show()

### Prediction using python library - sklearn
#split data
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.4,random_state=121)

#MODEL
LR_model = LinearRegression()
LR_model.fit(train_x.reshape(-1,1),train_y)
y_test_predict = LR_model.predict(test_x.reshape(-1,1))
print(y_test_predict)

#Evaluate performance
MSE = mean_squared_error(test_y,y_test_predict) #17.669
RMSE = root_mean_squared_error(test_y,y_test_predict) #4.203
R_squared = r2_score(test_y,y_test_predict) #0.971
print(R_squared)

#Predict for new hours
new_hours = np.array([29,49,100,256],dtype=float)
new_y = LR_model.predict(new_hours.reshape(-1,1))
print(new_y)

#Plotting of the line fit
plot_x = np.linspace(x.min(),x.max(),100).reshape(-1,1)
plot_y = LR_model.predict(plot_x)

plt.figure()
plt.scatter(train_x,train_y,label='TRAIN')
plt.scatter(test_x,y_test_predict,label='TEST')
plt.plot(plot_x,plot_y)
plt.xlabel('Hours of studied')
plt.ylabel('Scores')
plt.title('Scores vs Hours')
plt.show()
