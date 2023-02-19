from util import *

import nltk
from nltk.corpus import stopwords





class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

                

		stopwordRemovedText = [[word for word in sent if not word in stopwords.words('english')] for sent in text]
		

		#Fill in code here

		return stopwordRemovedText




	
