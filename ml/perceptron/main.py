import logging

from ml.perceptron.domain.MNISTSample import MNISTSample
from ml.perceptron.domain.PerceptronLearningAlgo import PerceptronLearningAlgo

logger = logging.getLogger("MAIN")

training_samples = MNISTSample.load_samples_from_dataset('data/mnist_train.csv')
validation_samples = MNISTSample.load_samples_from_dataset('data/mnist_test.csv')

learning_rate = 0.001
num_of_epochs = 50
true_class_labels_in_dataset = set(range(10))

perceptron_learning_algo = PerceptronLearningAlgo(learning_rate, num_of_epochs, training_samples, validation_samples, true_class_labels_in_dataset)

logger.info('Training perceptrons ...')
perceptron_learning_algo.train_and_compute_accuracy()
