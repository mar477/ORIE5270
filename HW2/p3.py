# ORIE 5270
# Spring 2020
# Mrinal Ramsaha (mar477)
# Citation:
# stackoverflow.com/a/53014308

#Remove redundancy
import os
os.environ['KMP_DUPLICATE_LIB_OK'] ='True'

#Import libraries
import keras
from keras.models import Sequential
from keras.layers import Dense,Activation,Flatten,Dropout,BatchNormalization
from keras.layers import Conv2D,MaxPooling2D
from keras.datasets import cifar10
from keras.utils import np_utils as u
import numpy as np
import matplotlib.pyplot as plt

#Question No.1

model = Sequential()

#Convolution Layer
model.add(Conv2D(32, kernel_size=(3, 3),strides=(2, 2),activation='relu',input_shape=(32,32,3))) #shape (32,32)

#MaxPooling Layer
model.add(MaxPooling2D(pool_size=(2, 2), strides=(1, 1)))

#Convolution Layer
model.add(Conv2D(64, (3, 3), activation='relu'))

#Flatten
model.add(Flatten())

#Dense Layer
model.add(Dense(1000, activation='relu'))

#Dense Layer
model.add(Dense(10, activation='softmax'))

#Compile
model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.Adam(),metrics=['accuracy'])

print(model.summary()) #prints summary

# Question No.2

#Loading Data
(x_train,y_train), (x_test,y_test) = cifar10.load_data()
y_train = u.to_categorical(y_train,10)
y_test = u.to_categorical(y_test,10)

#Random 10% sample of data
x_train = x_train[:int(0.1*len(x_train))]
y_train = y_train[:int(0.1*len(y_train))]
x_test = x_test[:int(0.1*len(x_test))]
y_test = y_test[:int(0.1*len(y_test))]

#Fit model
history = model.fit(x_train,y_train,validation_split=0.33,epochs=10,batch_size=128)

# Plot(1)
g = plt.figure();
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['loss','val_loss'],loc='upper left')
g.savefig("p3_output1.pdf",bbox_inches='tight')

# Question No.3

model = Sequential()

#Convolution Layer
model.add(Conv2D(32, kernel_size=(3, 3),strides=(2, 2),activation='relu',input_shape=(32,32,3)))

#Batch Normalization
model.add(BatchNormalization())

#MaxPooling Layer
model.add(MaxPooling2D(pool_size=(2, 2), strides=(1, 1)))

#Convolution Layer
model.add(Conv2D(64, (3, 3), activation='relu'))

#Flatten
model.add(Flatten())

#Dense Layer
model.add(Dense(1000, activation='relu'))

#Dense Layer
model.add(Dense(10, activation='softmax'))

#Compile
model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.Adam(),metrics=['accuracy'])

#Fit model (With Batch)
history = model.fit(x_train,y_train,validation_split=0.33,epochs=10,batch_size=128)

# Plot (with normalization layer)
g = plt.figure();
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['loss','val_loss'],loc='upper left')
g.savefig("p3_output2.pdf",bbox_inches='tight')

# Question No.4

model = Sequential()

#Convolution Layer
model.add(Conv2D(32, kernel_size=(3, 3),strides=(2, 2),activation='relu',input_shape=(32,32,3)))

#Dropout Layer
model.add(Dropout(rate=0.15))

#MaxPooling Layer
model.add(MaxPooling2D(pool_size=(2, 2), strides=(1, 1)))

#Convolution Layer
model.add(Conv2D(64, (3, 3), activation='relu'))

#Flatten
model.add(Flatten())

#Dense Layer
model.add(Dense(1000, activation='relu'))

#Dense Layer
model.add(Dense(10, activation='softmax'))

#Compile
model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.Adam(),metrics=['accuracy'])

#Fit model (With Batch)
history = model.fit(x_train,y_train,validation_split=0.33,epochs=10,batch_size=128)

#Plot (With Dropout Layer)
g = plt.figure();
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['loss','val_loss'],loc='upper left')
g.savefig("p3_output3.pdf",bbox_inches='tight')
