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

print("Testing at rank = "+str(k))
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
    if(dist1_vals[k-1]==dist2_vals[k-1]):
        print("The distributions are exactly the same.")
    else:
        if(result.pvalue<=alpha):
            print('p-value: '+str(round(result.pvalue,3))+". Reject the null hypothesis at the "+str(100*(1-alpha))+"% confidence level.")
        else:
            print('p-value: '+str(round(result.pvalue,3))+". Fail to reject the null hypothesis at the "+str(100*(1-alpha))+"% confidence level.")


print("\n\nTesting over values averaged over all ranks")
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
    
    dist1_vals_averaged = np.mean(dist1_vals, axis=0)
    dist2_vals_averaged = np.mean(dist2_vals, axis=0)
    result = ttest_rel(dist1_vals_averaged, dist2_vals_averaged, alternative = 'less')
    print(measure+': ')
    if(np.array_equal(dist1_vals_averaged, dist2_vals_averaged)):
        print("The distributions are exactly the same.")
    else: 
        if(result.pvalue<=alpha):
            print('p-value: '+str(round(result.pvalue,3))+". Reject the null hypothesis at the "+str(100*(1-alpha))+"% confidence level.")
        else:
            print('p-value: '+str(round(result.pvalue,3))+". Fail to reject the null hypothesis at the "+str(100*(1-alpha))+"% confidence level.")






