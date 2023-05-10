from util import *


class Evaluation():

        def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
                """
                Computation of precision of the Information Retrieval System
                at a given value of k for a single query

                Parameters
                ----------
                arg1 : list
                        A list of integers denoting the IDs of documents in
                        their predicted order of relevance to a query
                arg2 : int
                        The ID of the query in question
                arg3 : list
                        The list of IDs of documents relevant to the query (ground truth)
                arg4 : int
                        The k value

                Returns
                -------
                float
                        The precision value as a number between 0 and 1
                """

                precision = -1
                num_relevant = 0

                if k > len(query_doc_IDs_ordered): 
                        print("Value Error: k cannot be larger than number of documents retrieved. Pls re-enter k.")
                        return precision
                
                # Finding number of relevant documents in the top k retrieved documents
                for id in query_doc_IDs_ordered[:k]:  
                        if int(id) in true_doc_IDs:
                                num_relevant += 1

                precision = num_relevant/k 

                return precision


        def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
                """
                Computation of precision of the Information Retrieval System
                at a given value of k, averaged over all the queries

                Parameters
                ----------
                arg1 : list
                        A list of lists of integers where the ith sub-list is a list of IDs
                        of documents in their predicted order of relevance to the ith query
                arg2 : list
                        A list of IDs of the queries for which the documents are ordered
                arg3 : list
                        A list of dictionaries containing document-relevance
                        judgements - Refer cran_qrels.json for the structure of each
                        dictionary
                arg4 : int
                        The k value

                Returns
                -------
                float
                        The mean precision value as a number between 0 and 1
                """
                precs = []
                mean_prec = -1

                if len(doc_IDs_ordered) != len(query_ids):
                        print("Error! Number of queries have to be equal to number of lists of document orders")
                        return mean_prec

                mean_prec = 0
                for i in range(len(query_ids)):  
                        
                        true_doc_IDs = []
                        for d in qrels:
                                if int(d["query_num"]) ==  int(query_ids[i]):
                                        true_doc_IDs.append(int(d["id"]))
                        
                        # Using queryPrecision function to get precision for given query
                        mean_prec += self.queryPrecision(doc_IDs_ordered[i], int(query_ids[i]), true_doc_IDs, k)
                        precs.append(self.queryPrecision(doc_IDs_ordered[i], int(query_ids[i]), true_doc_IDs, k))

                mean_prec /=  len(query_ids)  

                return mean_prec, precs

        
        def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
                """
                Computation of recall of the Information Retrieval System
                at a given value of k for a single query

                Parameters
                ----------
                arg1 : list
                        A list of integers denoting the IDs of documents in
                        their predicted order of relevance to a query
                arg2 : int
                        The ID of the query in question
                arg3 : list
                        The list of IDs of documents relevant to the query (ground truth)
                arg4 : int
                        The k value

                Returns
                -------
                float
                        The recall value as a number between 0 and 1
                """

                recall = -1
                num_relevant = 0

                if k > len(query_doc_IDs_ordered): 
                        print("Value Error: k cannot be larger than number of documents retrieved. Pls re-enter k.")
                        return recall
                
                # Finding number of relevant documents in the top k retrieved documents
                for id in query_doc_IDs_ordered[:k]:  
                        if int(id) in true_doc_IDs:
                                num_relevant += 1

                recall = num_relevant/len(true_doc_IDs)

                return recall


        def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
                """
                Computation of recall of the Information Retrieval System
                at a given value of k, averaged over all the queries

                Parameters
                ----------
                arg1 : list
                        A list of lists of integers where the ith sub-list is a list of IDs
                        of documents in their predicted order of relevance to the ith query
                arg2 : list
                        A list of IDs of the queries for which the documents are ordered
                arg3 : list
                        A list of dictionaries containing document-relevance
                        judgements - Refer cran_qrels.json for the structure of each
                        dictionary
                arg4 : int
                        The k value

                Returns
                -------
                float
                        The mean recall value as a number between 0 and 1
                """
                recs = []
                mean_rec = -1

                if len(doc_IDs_ordered) != len(query_ids):
                        print("Error! Number of queries have to be equal to number of lists of document orders")
                        return mean_rec

                mean_rec = 0
                for i in range(len(query_ids)):  
                        
                        true_doc_IDs = []
                        for d in qrels:
                                if int(d["query_num"]) ==  int(query_ids[i]):
                                        true_doc_IDs.append(int(d["id"]))
                        
                        # Using queryRecall function to get precision for given query
                        mean_rec += self.queryRecall(doc_IDs_ordered[i], int(query_ids[i]), true_doc_IDs, k)
                        recs.append(self.queryRecall(doc_IDs_ordered[i], int(query_ids[i]), true_doc_IDs, k))

                mean_rec /=  len(query_ids)  

                return mean_rec, recs


        def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
                """
                Computation of fscore of the Information Retrieval System
                at a given value of k for a single query

                Parameters
                ----------
                arg1 : list
                        A list of integers denoting the IDs of documents in
                        their predicted order of relevance to a query
                arg2 : int
                        The ID of the query in question
                arg3 : list
                        The list of IDs of documents relevant to the query (ground truth)
                arg4 : int
                        The k value

                Returns
                -------
                float
                        The fscore value as a number between 0 and 1
                """

                fscore = -1
                if k > len(query_doc_IDs_ordered):
                        print("Value Error: k cannot be larger than number of documents retrieved. Pls re-enter k.")
                        return recall

                # Using previously defined precision and recall functions
                precision = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
                recall = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)

                if precision == 0.0 or recall == 0.0:   # Null case
                        fscore = 0
                else:
                        fscore = (2 * precision * recall) / (precision + recall)
                return fscore

        def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
                """
                Computation of fscore of the Information Retrieval System
                at a given value of k, averaged over all the queries

                Parameters
                ----------
                arg1 : list
                        A list of lists of integers where the ith sub-list is a list of IDs
                        of documents in their predicted order of relevance to the ith query
                arg2 : list
                        A list of IDs of the queries for which the documents are ordered
                arg3 : list
                        A list of dictionaries containing document-relevance
                        judgements - Refer cran_qrels.json for the structure of each
                        dictionary
                arg4 : int
                        The k value
                
                Returns
                -------
                float
                        The mean fscore value as a number between 0 and 1
                """

                mean_F = -1
                Fs = []
                
                if len(doc_IDs_ordered) != len(query_ids):
                        print("Error! Number of queries have to be equal to number of lists of document orders")
                        return mean_F

                mean_F = 0
                for i in range(len(query_ids)):
                        
                        true_doc_IDs = []
                        for d in qrels:
                                if int(d["query_num"]) ==  int(query_ids[i]):
                                        true_doc_IDs.append(int(d["id"]))
                        
                        #We use queryFscore function to get Fscore for given query
                        mean_F += self.queryFscore(doc_IDs_ordered[i], int(query_ids[i]), true_doc_IDs, k)
                        Fs.append(self.queryFscore(doc_IDs_ordered[i], int(query_ids[i]), true_doc_IDs, k))

                mean_F /=  len(query_ids) #Dividing by number of queries to get mean Fscore

                return mean_F, Fs
        

        def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
                """
                Computation of nDCG of the Information Retrieval System
                at given value of k for a single query

                Parameters
                ----------
                arg1 : list
                        A list of integers denoting the IDs of documents in
                        their predicted order of relevance to a query
                arg2 : int
                        The ID of the query in question
                arg3 : list
                        The list of IDs of documents relevant to the query (ground truth)
                arg4 : int
                        The k value

                Returns
                -------
                float
                        The nDCG value as a number between 0 and 1
                """

                nDCG = -1
                if k > len(query_doc_IDs_ordered):
                        print("Value Error: k cannot be larger than number of documents retrieved. Pls re-enter k.")
                        return nDCG
                
                DCGk, IDCGk = 0, 0
                doc_rel_scores={}

                for d in true_doc_IDs: #Getting relevance scores from cran_qrels.json
                        if int(d["query_num"]) == int(query_id):
                                doc_rel_scores[int(d["id"])] = 5 - int(d["position"])

                doc_list = list(doc_rel_scores.keys())
                rel_vals_des = sorted(doc_rel_scores.values(),reverse=True)

                for i in range(k): #Finding DCG and IDCG values for top k retrieved documents (Formula in report)
                        if int(query_doc_IDs_ordered[i]) in doc_list:
                                DCGk += doc_rel_scores[query_doc_IDs_ordered[i]]/ np.log2(i+2)
                        if i < len(rel_vals_des):
                                IDCGk += rel_vals_des[i] / np.log2(i+2)

                if IDCGk == 0:
                        print("IDCG@k = 0 and hence no relevant documents for given query")
                        return -1

                nDCG = DCGk / IDCGk  

                return nDCG 

        def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
                """
                Computation of nDCG of the Information Retrieval System
                at a given value of k, averaged over all the queries

                Parameters
                ----------
                arg1 : list
                        A list of lists of integers where the ith sub-list is a list of IDs
                        of documents in their predicted order of relevance to the ith query
                arg2 : list
                        A list of IDs of the queries for which the documents are ordered
                arg3 : list
                        A list of dictionaries containing document-relevance
                        judgements - Refer cran_qrels.json for the structure of each
                        dictionary
                arg4 : int
                        The k value

                Returns
                -------
                float
                        The mean nDCG value as a number between 0 and 1
                """

                mean_nDCG = -1
                ndcgs = []

                if len(doc_IDs_ordered) != len(query_ids):
                        print("Error! Number of queries have to be equal to number of lists of document orders")
                        return mean_nDCG

                mean_nDCG = 0
                for i in range(len(query_ids)):  
                        # Using queryNDCG function to get nDCG for the given query
                        mean_nDCG += self.queryNDCG(doc_IDs_ordered[i], int(query_ids[i]), qrels, k)
                        ndcgs.append(self.queryNDCG(doc_IDs_ordered[i], int(query_ids[i]), qrels, k))

                mean_nDCG /=  len(query_ids)

                return mean_nDCG, ndcgs


        def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
                """
                Computation of average precision of the Information Retrieval System
                at a given value of k for a single query (the average of precision@i
                values for i such that the ith document is truly relevant)

                Parameters
                ----------
                arg1 : list
                        A list of integers denoting the IDs of documents in
                        their predicted order of relevance to a query
                arg2 : int
                        The ID of the query in question
                arg3 : list
                        The list of documents relevant to the query (ground truth)
                arg4 : int
                        The k value

                Returns
                -------
                float
                        The average precision value as a number between 0 and 1
                """

                if k > len(query_doc_IDs_ordered):
                        print("Value Error: k cannot be larger than number of documents retrieved. Pls re-enter k.")
                        return -1

                avgPrecision = 0
                number_rel = 0
                for i in range(k):
                        if query_doc_IDs_ordered[i] in true_doc_IDs:
                                number_rel+=1
                                avgPrecision += number_rel/(i+1)          

                if number_rel == 0:
                        return 0
                else:
                        avgPrecision /= number_rel

                return avgPrecision


        def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
                """
                Computation of MAP of the Information Retrieval System
                at given value of k, averaged over all the queries

                Parameters
                ----------
                arg1 : list
                        A list of lists of integers where the ith sub-list is a list of IDs
                        of documents in their predicted order of relevance to the ith query
                arg2 : list
                        A list of IDs of the queries
                arg3 : list
                        A list of dictionaries containing document-relevance
                        judgements - Refer cran_qrels.json for the structure of each
                        dictionary
                arg4 : int
                        The k value

                Returns
                -------
                float
                        The MAP value as a number between 0 and 1
                """

                MAP = -1
                avps = []

                if len(doc_IDs_ordered) != len(query_ids):
                        print("Error! Number of queries have to be equal to number of lists of document orders")
                        return MAP

                MAP = 0
                for i in range(len(query_ids)):

                        true_doc_IDs = []
                        for d in q_rels:
                                if int(d["query_num"]) ==  int(query_ids[i]):
                                        true_doc_IDs.append(int(d["id"]))
                        
                        # Using queryAveragePrecision function to get AP for given query
                        MAP += self.queryAveragePrecision(doc_IDs_ordered[i], int(query_ids[i]), true_doc_IDs, k)
                        avps. append(self.queryAveragePrecision(doc_IDs_ordered[i], int(query_ids[i]), true_doc_IDs, k))

                MAP /=  len(query_ids) #Dividing by number of queries to get mean AP

                return MAP, avps
