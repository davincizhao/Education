import warnings
from asl_data import SinglesData
import operator


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    # TODO implement the recognizer
    # return probabilities, guesses

    for index in range(test_set.num_items):

        dic_w_value ={}
        x_word_s,l_word=test_set.get_item_Xlengths(index)
        for word,mod in models.items():
            try:
                # create a dictionary - word:probabilities 
                dic_w_value[word] = mod.score(x_word_s,l_word)
            except:
                dic_w_value[word] = float("-inf")
                continue
        # get the word of the max loglvalue
        guesses.append(max(dic_w_value.items( ), key=operator.itemgetter(1))[0])
        probabilities.append(dic_w_value)

    return probabilities,guesses

