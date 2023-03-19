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

                #Fill in code here
                index = {} # {term: {doc_id: term_f}}
                idf_dict = {} # {term: term_idf}
                N = len(docIDs)

                for i, id in enumerate(docIDs):
                        current_doc = docs[i]
                        for sentence in current_doc:
                                for word in sentence:
                                        if word not in index:
                                                index[word] = {}
                                        if id not in index[word]:
                                                index[word][id] = 1
                                        else:
                                                index[word][id] += 1

                idf_dict = {}
                
                for word in index:
                        
                        idf_dict[word] = np.log2(N / len(index[word]))
                
                dvecs = {}  # Document vectors of the form {doc_id: document vector of len(vocabulary)} 
                for id in docIDs:
                        dvec = []
                        for word in idf_dict:
                                if id in index[word]:
                                        dvec.append(index[word][id] * idf_dict[word])
                                else:
                                        dvec.append(0)
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

                for query in queries:
                        q_w_count = {}
                        for sentence in query:
                                for word in sentence:
                                        if word not in q_w_count:
                                                q_w_count[word] = 0
                                        q_w_count[word] += 1
                        
                        qvec = []
                        qwords = []
                        for word in self.idfs:
                                if word not in q_w_count:
                                        tf = 0
                                else:
                                        tf = q_w_count[word]
                                        qwords.append(word)
                                qvec.append(tf * self.idfs[word])
                
                        scores = {}

                        doc_subset = []
                        for w in qwords:
                                for id in self.index[w]:
                                        if id not in doc_subset:
                                                doc_subset.append(id)
                        for id in doc_subset:                
                                a_vec, b_vec = np.array(self.dvecs[id]), np.array(qvec)
                                scores[id] = np.dot(a_vec, b_vec) / (np.linalg.norm(a_vec) * np.linalg.norm(b_vec))
                        
                        doc_IDs_ordered.append(sorted(scores, key=scores.get, reverse=True))
        
                return doc_IDs_ordered




