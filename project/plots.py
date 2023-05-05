import sys
import csv
import matplotlib.pyplot as plt

dists = []
for dist in sys.argv[1:]:
    dists.append(dist)

fig = plt.figure()
measures = measures = ['precision', 'recall', 'fscore', 'mavp', 'ndcg']

for measure in measures:
    for i in range(len(dists)): 
        dist = dists[i]      
        with open(dist + '/plotdata/'+ measure +'.csv', newline='') as f:
            reader = csv.reader(f)
            dist_vals = list(reader)
    
        for j in range(len(dist_vals)):
            dist_vals[j] = [float(i) for i in dist_vals[j]]
        
        plt.plot(range(1,11), dist_vals, label=dist)
       
    plt.title(measure)
    plt.legend()
    plt.savefig('plots/'+measure+'.png')
    plt.clf()


