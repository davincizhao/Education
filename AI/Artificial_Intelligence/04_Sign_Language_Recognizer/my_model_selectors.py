import math
import statistics
import warnings

import numpy as np
from hmmlearn.hmm import GaussianHMM
from sklearn.model_selection import KFold
from asl_utils import combine_sequences

import logging

class ModelSelector(object):
    '''
    base class for model selection (strategy design pattern)
    '''

    def __init__(self, all_word_sequences: dict, all_word_Xlengths: dict, this_word: str,
                 n_constant=3,
                 min_n_components=2, max_n_components=10,
                 random_state=14, verbose=False):
        self.words = all_word_sequences
        self.hwords = all_word_Xlengths
        self.sequences = all_word_sequences[this_word]
        self.X, self.lengths = all_word_Xlengths[this_word]
        self.this_word = this_word
        self.n_constant = n_constant
        self.min_n_components = min_n_components
        self.max_n_components = max_n_components
        self.random_state = random_state
        self.verbose = verbose

    def select(self):
        raise NotImplementedError

    def base_model(self, num_states):
        # with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        # warnings.filterwarnings("ignore", category=RuntimeWarning)
        try:
            hmm_model = GaussianHMM(n_components=num_states, covariance_type="diag", n_iter=1000,
                                    random_state=self.random_state, verbose=False).fit(self.X, self.lengths)
            if self.verbose:
                print("model created for {} with {} states".format(self.this_word, num_states))
            return hmm_model
        except:
            if self.verbose:
                print("failure on {} with {} states".format(self.this_word, num_states))
            return None


class SelectorConstant(ModelSelector):
    """ select the model with value self.n_constant

    """

    def select(self):
        """ select based on n_constant value

        :return: GaussianHMM object
        """
        best_num_components = self.n_constant
        return self.base_model(best_num_components)


class SelectorBIC(ModelSelector):
    """ select the model with the lowest Bayesian Information Criterion(BIC) score

    http://www2.imm.dtu.dk/courses/02433/doc/ch6_slides.pdf
    Bayesian information criteria: BIC = -2 * logL + p * logN
    """

    def select(self):
        """ select the best model for self.this_word based on
        BIC score for n between self.min_n_components and self.max_n_components

        :return: GaussianHMM object
        """
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection based on BIC scores
        best_model = None
        lowest_logl = float("inf")
        d = len(self.X[0])
        for n_state in range(self.min_n_components, self.max_n_components + 1):
            try:
                model = GaussianHMM(n_components=n_state, n_iter=1000).fit(self.X,  self.lengths)
                logL = model.score(self.X,  self.lengths)

                BIC_logl = -2*logL + (n_state*n_state + 2 * d * n_state - 1) * math.log(d)
                if BIC_logl < lowest_logl:
                    lowest_logl = BIC_logl
                    best_model = model
            except:
                continue
        return best_model


class SelectorDIC(ModelSelector):
    ''' select best model based on Discriminative Information Criterion

    Biem, Alain. "A model selection criterion for classification: Application to hmm topology optimization."
    Document Analysis and Recognition, 2003. Proceedings. Seventh International Conference on. IEEE, 2003.
    http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.58.6208&rep=rep1&type=pdf
    DIC = log(P(X(i)) - 1/(M-1)SUM(log(P(X(all but i))
    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection based on DIC scores
        best_model = None
        dic = float("-inf")

        for n_state in range(self.min_n_components, self.max_n_components + 1):
            try:
                antiLogL = 0.0
                w_count = 0
                
                model = GaussianHMM(n_components=n_state,covariance_type="diag", n_iter=1000,verbose=False).fit(self.X,  self.lengths)
                logL = model.score(self.X,  self.lengths)
                
                for word in self.hwords:
                    if word == self.this_word:
                        continue
                    X_not_i, lengths = self.hwords[word]
                    antiLogL += model.score(X_not_i, lengths)
                    w_count += 1
                # SUM(log(P(X(all but i)) / (M-1)
                antiLogL /= float(w_count)
                
                if (logL - antiLogL) > dic:
                    dic = logL - antiLogL
                    best_model = model

            except:
                continue
        return best_model


class SelectorCV(ModelSelector):
    ''' select best model based on average log Likelihood of cross-validation folds

    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection using CV
        n_split = min(3, len(self.sequences))

        avg_logl = float("-inf")
        #split_method = KFold(n_split)
        best_model = None
        for n_state in range(self.min_n_components, self.max_n_components + 1):
            try:
                sum_logl = 0
                split_method = KFold(n_split)
                for cv_train_idx,cv_test_idx in split_method.split(self.sequences):
                    Train_x,Train_len = combine_sequences(cv_train_idx,self.sequences)
                    Test_x,Test_len = combine_sequences(cv_test_idx,self.sequences)
                    model = GaussianHMM(n_components=n_state, covariance_type="diag", n_iter=1000,random_state=self.random_state).fit(Train_x,Train_len)
                    logl = model.score(Test_x,Test_len)
                    sum_logl += logl

                if (sum_logl/n_split) > avg_logl:
                    avg_logl = (sum_logl/n_split)
                    best_model = self.base_model(n_state)
                
            except:
                continue
        
        return best_model
        