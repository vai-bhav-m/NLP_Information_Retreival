# Add your import statements here
import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

import re
import nltk
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Add any utility functions here
