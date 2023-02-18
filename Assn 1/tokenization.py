from util import *

# Add your import statements here
import re
from nltk.tokenize.treebank import TreebankWordTokenizer



class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = None

		#Fill in code here
		tokenizedText = []
		for t in text:
			nt = re.sub('[^a-zA-Z0-9 ]', ' ', t)
			nt = nt.split()
			tokenizedText.append(nt)

		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = None

		#Fill in code here
		tokenizedText = [TreebankWordTokenizer().tokenize(string) for string in text]
		
		return tokenizedText