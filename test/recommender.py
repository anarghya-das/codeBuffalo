import pdb
import os
from surprise import accuracy
from surprise.model_selection import train_test_split
from surprise import Dataset
from surprise import Reader
from surprise.prediction_algorithms import SVD
import pandas as pd
from convert_pandas import json_to_pandas
num_traits = 52

# path to dataset file

def user_to_dfrows(num_rows, personality):
    uid = (num_rows//num_traits) + 1
    final = {}

    final['trait'] = []
    final['user'] = []
    final['percentile'] = []
    for trait in personality:
        final['user'].append(uid)
        final['trait'].append(trait)
        final['percentile'].append(personality[trait])
    return final



def run_model(personality):

    reader = Reader(sep=',', skip_lines=0, rating_scale=(0.0, 1.0))
    df = pd.DataFrame(json_to_pandas())

    new = pd.DataFrame(user_to_dfrows(len(df.index), personality))
    df = df.append(new)
    import pdb;pdb.set_trace()
    data = Dataset.load_from_df(df[['user', 'trait', 'percentile']], reader=reader)

    # pdb.set_trace()
    trainset = data.build_full_trainset()
    # Use user_based true/false to switch between user-based or item-based collaborative filtering
    # algo = KNNWithMeans(k=40, sim_options={
    # 'name': 'pearson_baseline', 'user_based': False})
    algo = SVD()
    # algo.fit(trainset)
    algo.fit(trainset)
    # exit(1)
    testset = trainset.build_anti_testset()
    predictions = algo.test(testset)

    import heapq
    heap = []
    for prediction in predictions:
        heap.append((prediction[3], prediction[1]))
    heapq.heapify(heap)
    return heapq.nlargest(3, heap)
