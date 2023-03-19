from util import *




class InformationRetrieval():

	def __init__(self):
		self.index = None
		self.idfs = None
		self.dvecs = None

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""

		index = {}

		#Fill in code here
		tf_dict = {} # {term: {doc_id: term_f}}
		idf_dict = {} # {term: term_idf}
		N = len(docIDs)

		for i, id in enumerate(docIDs):
			current_doc = docs[i]
			for sentence in current_doc:
				for word in sentence:
					if word not in tf_dict:
						tf_dict[word] = dict(zip(docIDs, [0] * N))
					tf_dict[word][id] += 1

		
		idf_dict = dict(zip(list(tf_dict.keys()), [0] * len(tf_dict)))
		
		for word in idf_dict:
			# Typically idf calculation involves log2, but I'm using log10 here
			idf_dict[word] = np.log10(N / np.sum(np.array(list(tf_dict[word].values())) > 0))   
			index[word] = dict(zip(docIDs, [tf * idf_dict[word] for tf in list(tf_dict[word].values())]))
		
		dvecs = {}  # Document vectors of the form {doc_id: document vector of len(vocabulary)} 
		for id in docIDs:
			dvec = []
			for word in idf_dict:
				dvec.append(index[word][id])
			dvecs[id] = dvec

		self.index = index
		self.idfs = idf_dict
		self.dvecs = dvecs

	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""

		doc_IDs_ordered = []

		#Fill in code here
		for query in queries:
			q_w_count = {}
			for sentence in query:
				for word in sentence:
					if word not in q_w_count:
						q_w_count[word] = 0
					q_w_count[word] += 1
			
			qvec = []
			for word in self.idfs:
				if word not in q_w_count:
					tf = 0
				else:
					tf = q_w_count[word]
				qvec.append(tf * self.idfs[word])
		
			scores = {}
			for id in self.dvecs:
				a_vec, b_vec = np.array(self.dvecs[id]), np.array(qvec)
				scores[id] = np.dot(a_vec, b_vec) / (np.linalg.norm(a_vec) * np.linalg.norm(b_vec))
			
			doc_IDs_ordered.append(sorted(scores, key=scores.get, reverse=True))
	
		return doc_IDs_ordered




