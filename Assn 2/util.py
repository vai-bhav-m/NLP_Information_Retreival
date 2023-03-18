# Add your import statements here
import numpy as np
import matplotlib.pyplot as plt

import re
import nltk
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Add any utility functions here
def cosine_similarity(list1, list2):
    '''
    Computes the cosine similarity between 2 lists of numbers
    '''
    a, b = np.array(list1), np.array(list2)
    anorm, bnorm = np.linalg.norm(a), np.linalg.norm(b) 
    
    if anorm * bnorm == 0:
        return 0
    return a.T @ b
