# Add your import statements here
import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
import warnings


import re
import nltk
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")


# Add any utility functions here
def cosine_similarity(list1, list2):
    a, b = np.array(list1), np.array(list2)
    anorm, bnorm = norm(a), norm(b)

    if anorm * bnorm == 0:
        return 0
    return np.dot(a, b) / (anorm * bnorm)
