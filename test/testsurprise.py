import pdb
import os
from surprise import accuracy
from surprise.model_selection import train_test_split
from surprise import Dataset
from surprise import Reader
from surprise.prediction_algorithms import SVD
import pandas as pd
from convert_pandas import json_to_pandas

# path to dataset file
import pdb
pdb.set_trace()
reader = Reader(sep=',', skip_lines=0, rating_scale=(0.0, 1.0))
df = pd.DataFrame(json_to_pandas())
data = Dataset.load_from_df(df[['user', 'trait', 'percentile']], reader=reader)
# pdb.set_trace()
trainset = data.build_full_trainset()
print(trainset)
# Use user_based true/false to switch between user-based or item-based collaborative filtering
# algo = KNNWithMeans(k=40, sim_options={
# 'name': 'pearson_baseline', 'user_based': False})
algo = SVD()
# algo.fit(trainset)
algo.fit(trainset)
print(algo)
# exit(1)
testset = trainset.build_anti_testset()
predictions = algo.test(testset)

print(predictions)
# run the trained model against the testset
#test_pred = algo.test(testset)
# get RMSE
#print("User-based Model : Test Set")
#accuracy.rmse(test_pred, verbose=True)
# if you wanted to evaluate on the trainset
#print("User-based Model : Training Set")
#train_pred = algo.test(trainset.build_testset())
# accuracy.rmse(train_pred)

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
