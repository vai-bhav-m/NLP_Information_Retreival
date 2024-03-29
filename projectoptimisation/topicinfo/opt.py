import numpy as np
import optuna
import argparse
import main
from optuna.visualization import plot_intermediate_values
from optuna.visualization import plot_optimization_history

#using ndcg as the evaluation metric to be optimised (since relevance scores are available to us)

# Create an argument parser
parser = argparse.ArgumentParser(description='opt.py')

# Tunable parameters as external arguments
parser.add_argument('-dataset', default = "cranfield/", 
                    help = "Path to the dataset folder")
parser.add_argument('-out_folder', default = "output/", 
                    help = "Path to output folder")
parser.add_argument('-segmenter', default = "punkt",
                    help = "Sentence Segmenter Type [naive|punkt]")
parser.add_argument('-tokenizer',  default = "ptb",
                    help = "Tokenizer Type [naive|ptb]")
parser.add_argument('-custom', action = "store_true", 
                    help = "Take custom query as input")

# Parse the input arguments
args = parser.parse_args()

searchEngine = main.SearchEngine(args)

def to_be_optimised(title_w):
    return searchEngine.evaluateDataset(title_w)

def objective(trial):
    title_w = trial.suggest_float('title_w', 0.5, 2.5, step =0.25)
    return to_be_optimised(title_w)

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)

plot_optimization_history(study)

print("Best score: {} \nBest parameters: {}".format(study.best_value, study.best_params))

