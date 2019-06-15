import os
from surprise import accuracy
from surprise.model_selection import train_test_split
from surprise import Dataset
from surprise import Reader
from surprise.prediction_algorithms import *
import pandas as pd
# path to dataset file
file_path = os.path.expanduser('output.csv')

reader = Reader(sep=',', skip_lines=0, rating_scale=(0.0, 1.0))

data = Dataset.load_from_file(file_path, reader=reader)

trainset, testset = train_test_split(data, test_size=.05)
# Use user_based true/false to switch between user-based or item-based collaborative filtering
algo = KNNWithMeans(k=2, sim_options={
                    'name': 'pearson_baseline', 'user_based': False})
algo.fit(trainset)
# we can now query for specific predicions
uid = "500"  # raw user id
iid = "adventure"  # raw item id
# get a prediction for specific users and items.
pred = algo.predict(uid, iid, r_ui=1, verbose=True)
# run the trained model against the testset
test_pred = algo.test(testset)
# get RMSE
print("User-based Model : Test Set")
accuracy.rmse(test_pred, verbose=True)
# if you wanted to evaluate on the trainset
print("User-based Model : Training Set")
train_pred = algo.test(trainset.build_testset())
accuracy.rmse(train_pred)

'''
benchmark = []
# Iterate over all algorithms
for algorithm in [SVD(), SVDpp(), SlopeOne(), NMF(), NormalPredictor(), KNNBaseline(), KNNBasic(), KNNWithMeans(), KNNWithZScore(), BaselineOnly(), CoClustering()]:
    # Perform cross validation
    results = cross_validate(algorithm, data, measures=['RMSE'], cv=3, verbose=False)

    # Get results & append algorithm name
    tmp = pd.DataFrame.from_dict(results).mean(axis=0)
    tmp = tmp.append(pd.Series([str(algorithm).split(' ')[0].split('.')[-1]], index=['Algorithm']))
    benchmark.append(tmp)

print(min(benchmark, key=lambda x: x[0]))
print()
'''
