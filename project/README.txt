HYPOTHESIS TESTING

python3.11 hyptest.py <name of folder/model 1> <name of folder/model 2>

eg.
python3.11 hyptest.py initial bm25

The hypotheses are:
Null : the two distributions have identical average (expected) values
Alternate : the mean of the distribution underlying the first sample is less than the mean of the distribution underlying the second sample.

Hypothesis tested in two cases : i) for a particular rank, say 5 ii) averaged over all ranks



PLOTS

to compare the evaluation measures over ranks on different models, use the command

python3.11 plots.py <name of folder/model 1> <name of folder/model 2> ... <name of folder/model n> 

Eg. python3.11 plots.py initial bm25 

the plots will be stored in the folder called 'plots'