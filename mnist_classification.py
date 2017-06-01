import numpy as np 
np.random.seed(123)

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Dropout
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train /= 255
X_test /= 255

Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

model = Sequential()
 
model.add(Conv2D(32, 1, 1 activation='relu', input_shape=(1,28,28)))
model.add(Conv2D(32, 1 1 activation='relu'))
model.add(MaxPooling2D(pool_size=(1,1)))
model.add(Dropout(0.25))
 
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(X_train, Y_train, batch_size=32, nb_epoch=10, verbose=1)

score = model.evaluate(X_test, Y_Test, verbose=0)

print "Loss is %f, accuracy is %f", score[0], score[1]

values = model.predict(X_test, verbose=0) #this values[0] is 10 feature value with float value for each from 0-9
Y_test = list(Y_test)

value = []
for i in range(values.shape[0]):
  index_max = np.argmax(values[i])
  value.append(index_max)

bool = []
for i in range(len(values)):
  bool_value = (value[i]==Y_test[i])
  bool.append(bool_value)
  
 
