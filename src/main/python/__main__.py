import sys
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from models.conversion import Conversion
from views.converter_view import ConverterView
from controllers.converter_controller import ConverterController


class AppContext(ApplicationContext):
    def _setup_converter(self):
        self.conversion_model = Conversion()
        self.converter_controller = ConverterController(self.conversion_model)
        self.converter_view = ConverterView(self.conversion_model, self.converter_controller)

    def __init__(self):
        super(AppContext, self).__init__()
        self._setup_converter()

    def run(self):
        self.converter_view.show()
        return self.app.exec_()


if __name__ == '__main__':
    app_context = AppContext()
    exit_code = app_context.run()
    sys.exit(exit_code)
