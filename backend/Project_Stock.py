#!/usr/bin/env python
# coding: utf-8

# In[79]:


import math
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense,LSTM
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark-palette')


# In[100]:


#Getting the stock dataset --- in this case it's preinstalled so using pandas
df = pd.read_csv(r'C:\Users\rajku\OneDrive\Documents\Cletus\ClePro\HACKATHON\STOCK-PRICE\BHEL.NS_new.csv')
df


# In[101]:


#number of rows x column 
print(df.shape)
print(df['Close'])


# In[102]:


import datetime as dt

def str_to_datetime(st):
    split = st.split('-')
    year,month,day = int(split[0]),int(split[1]),int(split[2])
    return dt.datetime(year,month,day)

df['Date'] = df['Date'].apply(str_to_datetime)


# In[103]:


#Making date column the index column 
#can also be done in read_csv()
df.index = df.pop('Date')

#To Visulize closing price
plt.figure(figsize=(20,10))
plt.title("CLOSING PRICE PLOT")
plt.plot(df["Close"])
plt.xlabel("Date",fontsize=20)
plt.ylabel("Close price (USD/$)",fontsize=20)
plt.show()


# In[113]:


#Create a dataframe with only 'Close' column
print('Filtering <close> column') 
data = df.filter(['Close'])
#converting to a numpy array
dataset = data.to_numpy()
#get length of train set
train_set_len = math.ceil(len(dataset) * 0.8)

print(train_set_len)


# In[117]:


#Scaling / Normalizing the data
print('Scaling / Normalizing the data')
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)
print(scaled_data)
print('Done')

# In[128]:


#Creating the training dataset from scaled data
print("Creating the training dataset")
train_data = scaled_data[0:train_set_len, : ]
#split into x_train and y_train
x_train = []
y_train = []

for i in range(60,train_set_len):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i,0])
print('Done')

# In[135]:


#Converting train sets (x and y) to numpy array
#numpy array is 2-D -- major change in train sets
print('Converting to numpy array')
x_train ,y_train = np.array(x_train) ,np.array(y_train)
print('Done')

# In[154]:


#Reshaping data in 3-D
#Coz LSTM network excepts a 3-D model ... number of samples, number of time steps ,number of features
#len or x_train.shape[0]
print('Reshaping train sets')
x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))
print('Done')

# In[157]:


#Building LSTM model
print("Building the LSTM model")
model = Sequential()
model.add(LSTM(50,return_sequences=True,input_shape = (x_train.shape[1],1)))
model.add(LSTM(50,return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
print('Model Built')

#Compile the model
print('Compiling Model')
model.compile(optimizer='adam',loss = 'mean_squared_error')
print('Done')

# In[206]:


#Train the model
print('Traning the model now')
model.fit(x_train, y_train, batch_size = 1,epochs = 6)
print('Model Trained')

# In[163]:


#Create the testing dataset
print("Creating test dataset")
test_data = scaled_data[train_set_len - 60 :, :]
#Create x_test and y_test
x_test = []
y_test = dataset[train_set_len : , : ]
for i in range(60,len(test_data)):
    x_test.append(test_data[i-60:i , 0])
print('Test dataset created')

# In[165]:


#Convert x_test to a numpy array
#LSTM module accepts numpy array as input
print('Converting to a numpy array')
x_test = np.array(x_test)
print('Done')


# In[166]:


#Reshape x_tests
print("Reshaping test sets")
x_test = np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))
print('Done')

# In[203]:


#Get the models predicted test value
#Inverse Transforming the data
print("Predicting")
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)
print('Done')

# In[204]:


#Get RMSE (roomt mean squared error) 
#This basically gives accuracy of the model
#standard deviation
rmse = np.sqrt(np.mean(predictions - y_test)**2)
print(f'Accuracy --- {rmse}')


# In[190]:


#Plot the data
print('Plotting final plot')
train = data[ : train_set_len]
valid = data[train_set_len : ]
#Adding new column to valid
valid['Prediction'] = predictions
#Visualizing
plt.figure(figsize=(20,10))
plt.title("Model")
plt.plot(train['Close'])
plt.plot(valid[['Close','Prediction']])
plt.xlabel("Date",fontsize=20)
plt.ylabel("Close price (USD/$)",fontsize=20)
plt.legend(['Train','Valid','Predictions'], loc = 'upper right')
plt.show()


# In[191]:


#Showing valid and predicted prices 
print(valid)


