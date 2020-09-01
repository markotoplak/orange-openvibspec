import unittest

from openvibspec.models import CellularComponentsClassification

import Orange

import orangecontrib.spectroscopy  # to load data
from orangecontrib.openvibspecl.nntransfer import NNTransferLearner


class TestPerformance(unittest.TestCase):

    def test_overfit(self):
        data = Orange.data.Table("collagen")
        learner = NNTransferLearner(original_model=CellularComponentsClassification())
        c = learner(data)
        preds = c(data, 0)
        print(preds)