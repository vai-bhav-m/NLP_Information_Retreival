for hypothesis testing

python3.11 hyptest.py <name of folder 1> <name of folder 2>

eg.
python3.11 hyptest.py initial bm25

The hypotheses are:
Null : the two distributions have identical average (expected) values
Alternate : the mean of the distribution underlying the first sample is less than the mean of the distribution underlying the second sample.

Hypothesis tested in two cases : i) for a particular rank, say 5 ii) averaged over all ranks