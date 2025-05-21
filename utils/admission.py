import pandas as pd
import numpy as np

def calculate_percentile(user_score, dataset_scores):
    dataset_scores = np.array(dataset_scores)
    percentile = (np.sum(dataset_scores < user_score) / len(dataset_scores)) * 100
    return round(percentile, 2)
