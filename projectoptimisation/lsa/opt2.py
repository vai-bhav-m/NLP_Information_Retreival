from optuna.visualization import plot_intermediate_values
from optuna.visualization import plot_optimization_history
import optuna.visualization as vis
import numpy as np
import optuna
import argparse
import main


def to_be_optimised(x):
    return (x*x - 2)

def objective(trial):
    x = trial.suggest_int('x', -10, 10, step =1)
    return to_be_optimised(x)

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=20)

fig = vis.plot_optimization_history(study)
fig.write_image('plot.png')

print("Best score: {} \nBest parameters: {}".format(study.best_value, study.best_params))