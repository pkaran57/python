import logging
import matplotlib.pyplot as plt

from ml.perceptron.domain.Perceptron import Perceptron


class PerceptronLearningAlgo:

    def __init__(self, learning_rate, num_of_epochs, training_samples, validation_samples,
                 true_class_labels_in_dataset):
        self.__learning_rate = learning_rate
        self.__num_of_epochs = num_of_epochs
        self.__perceptrons = [Perceptron(training_samples, perceptron_class_label) for perceptron_class_label in
                              true_class_labels_in_dataset]

        self.__training_samples = training_samples
        self.__training_accuracies_per_epoch = []

        self.__validation_samples = validation_samples
        self.__validation_accuracies_per_epoch = []

        self.__logger = logging.getLogger('learning-rate={}'.format(learning_rate))

    def train_and_compute_accuracy(self):
        self.__compute_accuracy(0)

        for epoch_num in range(1, self.__num_of_epochs + 1):
            list(map(lambda perceptron: perceptron.train_for_an_epoch(self.__learning_rate), self.__perceptrons))
            self.__compute_accuracy(epoch_num)

        self.__plot_accuracies()

    def __compute_accuracy(self, epoch_num):
        for samples in self.__validation_samples, self.__training_samples:
            correct_predictions = 0
            total_num_predictions = len(samples)

            for sample in samples:
                net_inputs = list(map(lambda perceptron: perceptron.get_net_input(sample), self.__perceptrons))
                perceptron_target_label_with_max_net_input = net_inputs.index(max(net_inputs))

                if perceptron_target_label_with_max_net_input == sample.true_class_label:
                    correct_predictions += 1

            accuracy = (correct_predictions / total_num_predictions) * 100

            if samples is self.__validation_samples:
                self.__validation_accuracies_per_epoch.append(accuracy)
            else:
                self.__training_accuracies_per_epoch.append(accuracy)

            self.__logger.info("For epoch #{}, accuracy for {} dataset = {}".format(epoch_num,
                                                                                    'training' if samples is self.__training_samples else 'validation',
                                                                                    accuracy))

    def __plot_accuracies(self):
        plt.title("Accuracy over epochs for learning rate = {}".format(self.__learning_rate))

        plt.xlabel('Epoch Number')
        plt.ylabel('Accuracy (%)')

        plt.plot(self.__training_accuracies_per_epoch, label='Training Accuracy')
        plt.plot(self.__validation_accuracies_per_epoch, label='Validation Accuracy')

        plt.legend()
        plt.show()
