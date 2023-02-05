"""
Created on Fri Jan 20 19:07:43 2023

@author: cecile capponi
"""
from collections import Counter
import glob

import numpy as np
import cv2
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

"""
Computes a representation of an image from the (gif, png, jpg...) file 
representation can be (to extend) 
'HC': color histogram
'PX': tensor of pixels
'GC': matrix of gray pixels 
other to be defined
input = an image (jpg, png, gif)
output = a new representation of the image
"""


def raw_image_to_representation(image, representation):
    img = cv2.imread(image)

    desired_size = (500, 500)

    resized_image = cv2.resize(img, desired_size)

    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    return np.ravel(gray).tolist()


"""
Returns a data structure embedding train images described according to the 
specified representation and associate each image to its label.
-> Representation can be (to extend) 
'HC': color histogram
'PX': tensor of pixels 
'GC': matrix of gray pixels
other to be defined
input = where are the data, which represenation of the data must be produced ? 
output = a structure (dictionnary ? Matrix ? File ?) where the images of the
directory have been transformed and labelled according to the directory they are
stored in.
-- uses function raw_image_to_representation
"""


def load_transform_label_train_data(directory, representation):
    labelAndRepresentation = {
        -1: [],
        1: []
    }

    label = []
    data = []

    arrMer = glob.glob(directory + "/Mer/*")
    arrAilleur = glob.glob(directory + "/Ailleurs/*")
    for path in arrMer:
        label.append(1)
        data.append(raw_image_to_representation(path, representation))
    for path in arrAilleur:
        label.append(-1)
        data.append(raw_image_to_representation(path, representation))

    return label, data


"""
Returns a data structure embedding test images described according to the 
specified representation.
-> Representation can be (to extend) 
'HC': color histogram
'PX': tensor of pixels 
'GC': matrix of gray pixels 
other to be defined
input = where are the data, which represenation of the data must be produced ? 
output = a structure (dictionnary ? Matrix ? File ?) where the images of the
directory have been transformed (but not labelled)
-- uses function raw_image_to_representation
"""


def load_transform_test_data(directory, representation):
    testData = []
    arrTest = glob.glob(directory + "/*")
    for path in arrTest:
        testData.append(raw_image_to_representation(path, representation))

    return testData


"""
Learn a model (function) from a representation of data, using the algorithm 
and its hyper-parameters described in algo_dico
Here data has been previously transformed to the representation used to learn
the model
input = transformed labelled data, the used learning algo and its hyper-parameters (a dico ?)
output =  a model fit with data
"""


def learn_model_from_data(train_data, algo_dico):
    X_train = train_data[1]
    y_train = train_data[0]

    print(len(X_train))
    print(len(y_train))

    model = SVC(**algo_dico['hyper_parameters'])
    model.fit(X_train, y_train)
    return model


"""
Given one example (representation of an image as used to compute the model),
computes its class according to a previously learned model.
Here data has been previously transformed to the representation used to learn
the model
input = representation of one data, the learned model
output = the label of that one data (+1 or -1)
-- uses the model learned by function learn_model_from_data
"""


def predict_example_label(example, model):
    print("a")
    print(model.predict(example))
    label = 1  # could be -1
    return label


algo_dico = {
    'algorithm': 'SVC',
    'hyper_parameters': {
        'C': 1.0,
        'kernel': 'rbf',
        'degree': 3,
        'gamma': 'scale',
        'coef0': 0.0,
        'shrinking': True,
        'probability': False,
        'tol': 0.001,
        'class_weight': None,
        'verbose': False,
        'max_iter': -1,
        'decision_function_shape': 'ovr',
        'random_state': None
    }
}

print(predict_example_label(load_transform_label_train_data("test", "")[0],
                            learn_model_from_data(load_transform_label_train_data("Data", "HIST"), algo_dico)))

"""
Computes an array (or list or dico or whatever) that associates a prediction 
to each example (image) of the data, using a previously learned model. 
Here data has been previously transformed to the representation used to learn
the model
input = a structure (dico, matrix, ...) embedding all transformed data to a representation, and a model
output =  a structure that associates a label to each data (image) of the input sample
"""


def predict_sample_label(data, model):
    predictions = None
    return predictions


"""
Save the predictions on data to a text file with syntax:
filename <space> label (either -1 or 1)  
NO ACCENT  
Here data has been previously transformed to the representation used to learn
the model
input = where to save the predictions, structure embedding the data, the model used
for predictions
output =  OK if the file has been saved, not OK if not
"""


def write_predictions(directory, filename, data, model):
    return None


"""
Estimates the accuracy of a previously learned model using train data, 
either through CV or mean hold-out, with k folds.
Here data has been previously transformed to the representation used to learn
the model
input = the train labelled data as previously structured, the learned model, and
the number of split to be used either in a hold-out or by cross-validation  
output =  The score of success (betwwen 0 and 1, the higher the better, scores under 0.5
are worst than random
"""


def estimate_model_score(train_data, model, k):
    return None
