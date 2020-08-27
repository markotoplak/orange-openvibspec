import unittest

from openvibspec.models import CellularComponentsClassification


class TestLoad(unittest.TestCase):

    def test_load_cellular_component(self):
        model = CellularComponentsClassification()
        self.assertTrue(model.name.startswith("Cellular"))
        fitted = model.load()
