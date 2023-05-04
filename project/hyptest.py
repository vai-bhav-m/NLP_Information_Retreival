import csv
import matplotlib.pyplot as plt
import numpy as np
import sys
from scipy.stats import ttest_rel

# hypothesis testing carried out on rank k
k = 5

# H0: the two distributions have identical average (expected) values
# H1: the mean of the distribution underlying the first sample is less than the mean of the distribution underlying the second sample.

dist1 = sys.argv[1]
dist2 = sys.argv[2]

#confidence level = 100(1-alpha)
alpha = 0.05

measures = ['precision', 'recall', 'fscore', 'mavp', 'ndcg']

for measure in measures:
    with open(dist1 + '/hypothesesdata/'+ measure +'.csv', newline='') as f:
        reader = csv.reader(f)
        dist1_vals = list(reader)
    
    for j in range(len(dist1_vals)):
        dist1_vals[j] = [float(i) for i in dist1_vals[j]]

    with open(dist2 + '/hypothesesdata/'+ measure +'.csv', newline='') as f:
        reader = csv.reader(f)
        dist2_vals = list(reader)
    
    for j in range(len(dist1_vals)):
        dist2_vals[j] = [float(i) for i in dist2_vals[j]]
           

    result = ttest_rel(dist1_vals[k-1], dist2_vals[k-1], alternative = 'less')
    print(measure+": ")
    if(result.pvalue<=alpha):
        print('p-value is '+str(result.pvalue)+". Reject the null hypothesis at the "+str(100*(1-alpha))+"% confidence level.")
    else:
         print('p-value is '+str(result.pvalue)+". Fail to reject the null hypothesis at the "+str(100*(1-alpha))+"% confidence level.")

    






