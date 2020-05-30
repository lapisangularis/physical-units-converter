from PyQt5.QtCore import QObject, pyqtSlot


class ConverterController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model

    def _calculate_reset_state(self, value):
        self._model.enable_reset = True if value else False

    @pyqtSlot(int)
    def calculate_kilograms_to_pounds(self, value):
        self._model.input_value = float(value)
        self._model.kilograms_to_pounds()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_pounds_to_kilograms(self, value):
        self._model.input_value = float(value)
        self._model.pounds_to_kilograms()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_grams_to_pounds(self, value):
        self._model.input_value = float(value)
        self._model.grams_to_pounds()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_pounds_to_grams(self, value):
        self._model.input_value = float(value)
        self._model.pounds_to_grams()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_kilograms_to_ounces(self, value):
        self._model.input_value = float(value)
        self._model.kilograms_to_ounces()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_ounces_to_kilograms(self, value):
        self._model.input_value = float(value)
        self._model.ounces_to_kilograms()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_grams_to_ounces(self, value):
        self._model.input_value = float(value)
        self._model.grams_to_ounces()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_ounces_to_grams(self, value):
        self._model.input_value = float(value)
        self._model.ounces_to_grams()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_meters_to_inches(self, value):
        self._model.input_value = float(value)
        self._model.meters_to_inches()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_inches_to_meters(self, value):
        self._model.input_value = float(value)
        self._model.inches_to_meters()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_meters_to_feet(self, value):
        self._model.input_value = float(value)
        self._model.meters_to_feet()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_feet_to_meters(self, value):
        self._model.input_value = float(value)
        self._model.feet_to_meters()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_meters_to_yards(self, value):
        self._model.input_value = float(value)
        self._model.meters_to_yards()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_yards_to_meters(self, value):
        self._model.input_value = float(value)
        self._model.yards_to_meters()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_meters_to_miles(self, value):
        self._model.input_value = float(value)
        self._model.meters_to_miles()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_miles_to_meters(self, value):
        self._model.input_value = float(value)
        self._model.miles_to_meters()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_joules_to_ev(self, value):
        self._model.input_value = float(value)
        self._model.joules_to_ev()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_ev_to_joules(self, value):
        self._model.input_value = float(value)
        self._model.ev_to_joules()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_joules_to_calories(self, value):
        self._model.input_value = float(value)
        self._model.joules_to_calories()
        self._calculate_reset_state(value)

    @pyqtSlot(int)
    def calculate_calories_to_joules(self, value):
        self._model.input_value = float(value)
        self._model.calories_to_joules()
        self._calculate_reset_state(value)
