import csv
import random

import numpy as np

from ml.hw1.domain.MNISTSample import MNISTSample


def get_samples_from_dataset(dataset_file_location):
    with (open(dataset_file_location)) as csv_file:
        samples = [MNISTSample(int(row[0]), row[1:], row_num) for row_num, row in enumerate(csv.reader(csv_file))]
        print('Found {} samples in the dataset'.format(len(samples)))
        return samples


def get_sample_weights_array(len):
    return np.array([random.uniform(-0.5, 0.5) for i in range(len)], dtype=np.single)


sample_list = get_samples_from_dataset('data/mnist_train.csv')
weights = get_sample_weights_array(sample_list[0].features.size)
learning_rate = 0.1
target_label = 5

correct_predictions = 0
total_samples_matching_label = 0

for _ in range(50):
    for itr_num, sample in enumerate(sample_list):
        y = 1 if np.dot(sample.features, weights) > 0 else 0
        if y != (1 if sample.true_class_label == target_label else 0):
            weights = np.array([wi + (learning_rate * ((1 if target_label == sample.true_class_label else 0) - y) * xi) for wi, xi in zip(weights, sample.features)], dtype=np.single)
        else:
            if sample.true_class_label == target_label:
                correct_predictions += 1

        if sample.true_class_label == target_label:
            total_samples_matching_label += 1

    print('Accuracy % = {}, accurate predictions = {}, sample matching expected label = {}'.format(((correct_predictions / total_samples_matching_label) * 100), correct_predictions, total_samples_matching_label))
