from Orange.data import Table
from Orange.widgets.utils.owlearnerwidget import OWBaseLearner
from Orange.widgets.utils.widgetpreview import WidgetPreview
from Orange.classification.logistic_regression import LogisticRegressionLearner

from Orange.widgets.utils.signals import Output

class OWNNTranfer(OWBaseLearner):
    name = 'Neural Network Transfer'
    description = "Transfer learning with neural networks"
    icon = "icons/unknown.svg"
    keywords = ["neural", "network", "nn", "transfer"]

    LEARNER = LogisticRegressionLearner

    class Outputs(OWBaseLearner.Outputs):
        coefficients = Output("Coefficients", Table, explicit=True)

    def add_main_layout(self):
        pass

    def update_model(self):
        super().update_model()
        pass

    def handleNewSignals(self):
        self.apply()

    def create_learner(self):
        common_args = {'preprocessors': self.preprocessors}
        return self.LEARNER(**common_args)


if __name__ == "__main__":  # pragma: no cover
    WidgetPreview(OWNNTranfer).run(Table("iris"))
