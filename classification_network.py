# Importing Keras for classification
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense

# Importing numpy and setting a static seed
import numpy as np
np.random.seed(7)

# input the dimension of the dataset
inputDim = int(input("\nPlease enter the Dimension of the dataset: "))

# loading dataset
dataset = np.loadtxt("./data.csv", delimiter=",")

# splitting into x & y I/O
X = dataset[:, 0:inputDim]
Y = dataset[:, inputDim]

# creation of the model
model = Sequential()
model.add(Dense(int(1.5*inputDim), input_dim=inputDim, activation='relu'))
model.add(Dense(inputDim, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compiling the model
model.compile(optimizer=tf.train.AdamOptimizer(), loss='binary_crossentropy',
              metrics=['accuracy'])

# fit the model
model.fit(X, Y, epochs=100, batch_size=10, verbose=2)

# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

# predictions

# calculating the predictions
predictions = model.predict(X)
# rounding predictions
rounded = [round(x[0]) for x in predictions]
print(rounded)
