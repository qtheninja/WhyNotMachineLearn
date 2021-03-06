import numpy
import pandas
import csv
# https://keras.io/models/sequential/
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

#load data sets
dataframe = pandas.read_csv("housing.csv", delim_whitespace=True, header=None)
dataset = dataframe.values
#split into input (X) and output (Y) variables
X = dataset[:,0:13]
Y = dataset[:,13]

#define base mode
#ADAM
#rectifier activation is considered a 'best practice' with neural nets

def baseline_model():
	#create model
	model = Sequential();
	model.add(Dense(13, input_dim=13, init="normal", activation="relu"))
	model.add(Dense(1, init="normal"))
	#compile model
	model.compile(loss="mean_squared_error", optimizer="adam")
	return model

#fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
#evaluate model with standardized dataset
estimator = KerasRegressor(build_fn=baseline_model, nb_epoch=100, batch_size=5, verbose=0)

kfold = KFold(n=len(X), n_folds=10, random_state=seed)
results = cross_val_score(estimator, X, Y, cv=kfold)
print("Baseline: %.2f (%.2f) MSE " % (results.mean(), results.std()))

#CRIM	ZN		CHAS	NOX	RM	AGE	DIS	RAD TAX	PTRATIO	B	LSTAT	MEDV
#0.00632     2.310  0  0.5380  6.5750  65.20  4.0900   1  296.0  15.30 396.90   4.98  24.00
#INDUS 18.00


print results.predict([0.00632, 18.00, 2.310, 0, 0.5380, 6.5750, 65.20, 4.0900, 1, 296.0, 15.30, 396.90, 4.98,  24.00])