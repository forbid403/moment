from keras import Sequential
from keras.datasets import reuters
from keras.layers import Dense, LSTM, Embedding
from keras.preprocessing import sequence
from keras.utils import np_utils
import load_data

#call model
(X_train, y_train), (X_test, y_test) = load_data.load_article_data(2000)

# make data length equal
X_train = sequence.pad_sequences(X_train, maxlen=100)
X_test = sequence.pad_sequences(X_test, maxlen=100)

# one_hot_encoding
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

# build model
model = Sequential()
model.add(Embedding(2000, 120))
model.add(LSTM(120))
model.add(Dense(46, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(X_train, y_train, batch_size=100, epochs=20, validation_data=(X_test, y_test))
print("\n 테스트 정확도: %.4f" % (model.evaluate(X_test, y_test)[1]))


