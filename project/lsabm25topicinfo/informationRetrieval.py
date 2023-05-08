from util import *
from lsa_nlp import lsa_transform


class InformationRetrieval:
	def __init__(self):
		self.index = None
		self.idfs = None
		self.dvecs = None
		self.k = 1.75
		self.b = 0.9
		self.adl = 0
		self.title_k = 1.75

	def buildIndex(self, docs, titles, docIDs):
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

		# Fill in code here
		doc_index = {}  # {term: {doc_id: term_f}}
		idf_dict = {}  # {term: term_idf}
		N = len(docIDs)

		ddls = {} # {doc_id : document_length}

		for i, id in enumerate(docIDs):
			current_doc = docs[i]
			ddls[id] = 0
			for sentence in current_doc:
				for word in sentence:
					if word not in doc_index:
						doc_index[word] = {}
					if id not in doc_index[word]:
						doc_index[word][id] = 1
					else:
						doc_index[word][id] += 1
				ddls[id]+=len(sentence)
			
		
		

		title_index = {}
		tls = {}

		for i, id in enumerate(docIDs):
			current_title = titles[i]
			tls[id] = 0
			for sentence in current_title:
				for word in sentence:
					if word not in title_index:
						title_index[word] = {}
					if id not in title_index[word]:
						title_index[word][id] = self.title_k
					else:
						title_index[word][id] += self.title_k
				tls[id]+=len(sentence)*self.title_k
		
		index = {}
		for word in doc_index:
			index[word] = {}
			if word in title_index:
				for id in doc_index[word]:
					if id in title_index[word]:
						index[word][id] = doc_index[word][id] + title_index[word][id]
					else:
						index[word][id] = doc_index[word][id]
			else:
				for id in doc_index[word]:
					index[word][id] = doc_index[word][id]
			
		
		dls = {}
		self.adl = 0
		for i, id in enumerate(docIDs):
			dls[id] = ddls[id] + tls[id]
			self.adl+=dls[id]
		self.adl = self.adl/N


		idf_dict = {}
		for word in index:
			idf_dict[word] = np.log2(N / len(index[word]))

		# Document vectors of the form {doc_id: document vector of len(vocabulary)}
		dvecs = {}

		for id in docIDs:
			dvec = []
			for word in idf_dict:
				if id in index[word]:
					tf_now = index[word][id]
					tf_modified = tf_now/(tf_now + self.k*(1-self.b+self.b*dls[id]/self.adl))
					dvec.append(tf_modified * idf_dict[word])
				else:
					dvec.append(0)
			dvecs[id] = dvec

		self.index = index
		self.idfs = idf_dict

		# Performing LSA and extracting a transformer
		self.lsa_transformer, self.dvecs = lsa_transform(dvecs)

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

		i = 0
		for query in queries:
			#print(f"Done with {i/len(queries) * 100} % queries.")
			i += 1

			q_w_count = {}
			qlen = 0
			for sentence in query:
				for word in sentence:
					if word not in q_w_count:
						q_w_count[word] = 0
					q_w_count[word] += 1
				qlen += len(sentence)

			qvec = []
			qwords = []
			for word in self.idfs:
				if word not in q_w_count:
					tf_modified = 0
				else:
					tf_now = q_w_count[word]
					tf_modified = tf_now/(tf_now + self.k*(1-self.b+self.b*qlen/self.adl))
					qwords.append(word)
				qvec.append(tf_modified * self.idfs[word])

			scores = {}

			qvec = self.lsa_transformer.transform(np.array(qvec).reshape(1, -1))
			qvec = list(qvec.ravel())

			doc_subset = []
			for w in qwords:
				for id in self.index[w]:
					if id not in doc_subset:
						doc_subset.append(id)

			for id in doc_subset:
				scores[id] = cosine_similarity(self.dvecs[id], qvec)

			doc_IDs_ordered.append(sorted(scores, key=scores.get, reverse=True))

		return doc_IDs_ordered
