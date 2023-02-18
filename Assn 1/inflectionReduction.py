from util import *

# Add your import statements here
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('wordnet')


class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = None

		#Fill in code here
		reducedText = []
		# Stemming
		porter = PorterStemmer()
		for l in text:
			reducedText.append([porter.stem(x) for x in l])

		return reducedText