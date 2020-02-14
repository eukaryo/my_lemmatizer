# Original source code is here: https://www.nltk.org/_modules/nltk/stem/wordnet.html





# Natural Language Toolkit: WordNet stemmer interface
#
# Copyright (C) 2001-2019 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT
from __future__ import unicode_literals

from nltk.corpus.reader.wordnet import NOUN
from nltk.corpus import wordnet
from nltk.compat import python_2_unicode_compatible


class My_WordNetLemmatizer(object):
    """
    WordNet Lemmatizer

    Lemmatize using WordNet's built-in morphy function.
    Returns the input word unchanged if it cannot be found in WordNet.

        >>> from nltk.stem import WordNetLemmatizer
        >>> wnl = WordNetLemmatizer()
        >>> print(wnl.lemmatize('dogs'))
        dog
        >>> print(wnl.lemmatize('churches'))
        church
        >>> print(wnl.lemmatize('aardwolves'))
        aardwolf
        >>> print(wnl.lemmatize('abaci'))
        abacus
        >>> print(wnl.lemmatize('hardrock'))
        hardrock
    """

    def __init__(self):
        pass

    def my_lemmatize(self, word, pos=NOUN):
        lemmas = wordnet._morphy(word, pos)
        return (min(lemmas, key=len),True) if lemmas else (word,False)


    def __repr__(self):
        return '<WordNetLemmatizer>'



def teardown_module(module=None):
    from nltk.corpus import wordnet

    wordnet._unload()
