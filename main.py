import glob
import pickle

from estimate import estimate_model_score
from image_processing import load_transform_test_data, load_transform_label_train_data
from predictions import write_predictions
from trainer import fit_with_params

filename = glob.glob("TestCC2/*")

print("//////////////// LOADING TEST DATA ////////////////")
data_Test = load_transform_test_data("TestCC2", "PX")

print("//////////////// LOADING TRAIN DATA ////////////////")
train_data = load_transform_label_train_data("Data", "PX")


algo_dico_Gaussian = {
    'algorithm_name': 'GaussianNB',
    'hyperparameters': {
        'var_smoothing': [1e-9, 1e-7, 1e-5]
    }
}

algo_dico_MLP = {
    'algorithm_name': 'MLP',
    'hyperparameters': {
        'hidden_layer_sizes': [(10,), (20,), (30,)],
        'activation': ['identity', 'logistic', 'tanh', 'relu'],
        'solver': ['sgd', 'adam'],
        'alpha': [0.0001, 0.001, 0.01, 0.1],
        'learning_rate': ['constant', 'invscaling', 'adaptive'],
    }
}

parameters = {
    'algorithm_name': 'SVC',
    'hyperparameters': {
        'C': 1,
        'gamma': 'scale',
        'kernel': 'rbf',
        'verbose': False
    }
}

print("//////////////// LOADING MODEL ////////////////")
##grid_search = search_best_params(train_data, algo_dico_SVC)
##model = fit_with_params(train_data, parameters)

print("//////////////// LOADING WITH PICKLE ////////////////")
model = pickle.load(open("model.pickle", 'rb'))

print("//////////////// WRITE PREDICTIONS ////////////////")
write_predictions("./", filename, data_Test, model)

##print("//////////////// ESTIMATING ////////////////")
##print(estimate_model_score(train_data, model, 5))