import numpy as np

from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []

    # reshape each
    for index in range(0,len(series) - window_size ):
        X.append(series[index:index+window_size])

    y = series[window_size:]
    X = np.asarray(X)
    y = np.asarray(y)
    y = np.reshape(y,len(y),1)

    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    rnn_model = Sequential()
    rnn_model.add(LSTM(5, input_shape=(window_size, 1)))
    rnn_model.add(Dense(1))
    return rnn_model

### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?']
    alpha = ['a','b','c','d','e','f','g','h','i',
            'j','k','l','m','n','o','p','q','r','s',
            't','u','v','w','x','y','z']

    for id in range(len(text)):
        if text[id] not in punctuation and text[id] not in alpha:
                text = text.replace(text[id],' ')

    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    for id in range(0,len(text)- window_size +1,step_size):
        inputs.append(text[id:id+window_size])
        outputs.append(text[id+window_size])
    return inputs,outputs

# TODO build the required RNN model:
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss
def build_part2_RNN(window_size, num_chars):

    rnn_model2 = Sequential()
    rnn_model2.add(LSTM(200, input_shape=(window_size, num_chars)))
    rnn_model2.add(Dense(num_chars))
    rnn_model2.add(Activation('softmax'))

    return rnn_model2




