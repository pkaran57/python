import numpy as np


class MNISTSample:

    def __init__(self, true_class_label, features, sample_number):
        assert 0 <= true_class_label <= 9
        self.true_class_label = true_class_label  # also known as target

        assert len(features) == 784
        self.features = self.scale_feature([255] + features)
        assert len(self.features) == 785
        assert self.features[0] == 1, 'Bias unit should always be 1, but found - {}'.format(self.features[0])

        self.sample_number = sample_number

    def __str__(self):
        return "For sample # {} : target = {}, feature = {}".format(self.sample_number, self.true_class_label, self.features)

    @staticmethod
    def scale_feature(feature):
        return np.array(feature, dtype=np.single) / 255
