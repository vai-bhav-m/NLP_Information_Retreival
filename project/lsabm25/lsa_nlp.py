import numpy as np
from sklearn.decomposition import TruncatedSVD
import scipy.sparse as sp
import pandas as pd
import time


def lsa_transform(dvecs):
    # A matrix is of the form where each row is a document (text sample) and each column is a feature, here words
    A = pd.DataFrame(dvecs).to_numpy()
    A = sp.csr_matrix(A.T)

    # for n_comp in range(5, 500, 5):
    #     tic = time.time()
    #     svd = TruncatedSVD(n_components=n_comp, n_iter=10, random_state=42)
    #     svd.fit(A)
    #     print(
    #         f"Variance captured for {n_comp} components: {svd.explained_variance_ratio_.sum() * 100} %"
    #     )

    
    svd = TruncatedSVD(n_components=350, n_iter=10, random_state=42)
    svd.fit(A)
    A_trans = svd.transform(A)

    i = 0
    for key in dvecs:
        dvecs[key] = list(A_trans[i, :])
        i += 1

    return svd, dvecs
