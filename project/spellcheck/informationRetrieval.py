from util import *
from Levenshtein import distance
import math



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
                
                #index2 = {k: v for k, v in index.items() if k.isalpha()}

                self.index = index
                self.idfs = idf_dict
                self.dvecs = dvecs

        def rank(self, queries, isCustom):
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

                threshold = 15
                doc_IDs_ordered = []

                for query in queries:
                        q_w_count = {}
                        for sentence in query:
                                for word in sentence:
                                        if word not in q_w_count:
                                                q_w_count[word] = 0
                                        q_w_count[word] += 1
                        
                        candidates = {}
                        for c in self.index:
                                candidates[c] = sum(self.index[c].values())
                        tot_words = sum(candidates.values())
                        candidates = {key : value/tot_words for key, value in candidates.items()}
                        
                        q_w_count_revised = {}
                        for word in q_w_count:
                                if word not in self.index: #considered a spelling mistake
                                        candidate_list = {}
                                        for candidate in candidates:
                                                candidate_list[candidate] = distance(word, candidate)*math.log2(1/candidates[candidate])
                                        
                                        sorted_list = dict(sorted(candidate_list.items(), key=lambda item: item[1], reverse=False))
                                        corrected_word = next(iter(sorted_list))
                                        if sorted_list[corrected_word] < threshold:           
                                                q_w_count_revised[corrected_word] = q_w_count[word]
                                        else:
                                                q_w_count_revised[word] = q_w_count[word]
                                        #print(list(sorted_list.items())[:4])
                                else:
                                        q_w_count_revised[word] = q_w_count[word]
                                        
                        #print(q_w_count_revised)
                        
                        if(isCustom):
                                keys_str = ' '.join(q_w_count_revised.keys()) 
                                print("The spelling corrected query: "+keys_str)             
                        
                        qvec = []
                        qwords = []
                        for word in self.idfs:
                                if word not in q_w_count_revised:
                                        tf = 0
                                else:
                                        tf = q_w_count_revised[word]
                                        qwords.append(word)
                                qvec.append(tf * self.idfs[word])
                
                        scores = {}

                        doc_subset = []
                        for w in qwords:
                                for id in self.index[w]:
                                        if id not in doc_subset:
                                                doc_subset.append(id)
                        for id in doc_subset:                              
                                scores[id] = cosine_similarity(self.dvecs[id], qvec) 
                        
                        doc_IDs_ordered.append(sorted(scores, key=scores.get, reverse=True))
        
                return doc_IDs_ordered




