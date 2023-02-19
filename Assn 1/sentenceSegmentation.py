from util import *

# Add your import statements here

import re
import nltk

class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach
		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)
		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = re.split('\.|\!|\?',text)
		segmentedText = [i.lstrip() for i in segmentedText]
		if '' in segmentedText:
			segmentedText.remove('')

		return segmentedText





	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer
		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)
		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

		segmentedText = nltk.tokenize.sent_tokenize(text)

		return segmentedText
