from PyQt5.QtCore import QObject, pyqtSignal
from scipy import constants


class Conversion(QObject):
    input_value_changed = pyqtSignal(float)
    output_value_changed = pyqtSignal(float)
    enable_reset_changed = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self._input_value = 0
        self._output_value = 0
        self._enable_reset = False

    @property
    def input_value(self):
        return self._input_value

    @input_value.setter
    def input_value(self, value):
        self._input_value = value
        self.input_value_changed.emit(value)

    @property
    def output_value(self):
        return self._output_value

    @output_value.setter
    def output_value(self, value):
        self._output_value = value
        self.output_value_changed.emit(value)

    @property
    def enable_reset(self):
        return self._enable_reset

    @enable_reset.setter
    def enable_reset(self, value):
        self._enable_reset = value
        self.enable_reset_changed.emit(value)

    def kilograms_to_pounds(self):
        self.output_value = (1 / constants.pound) * self.input_value

    def pounds_to_kilograms(self):
        self.output_value = constants.pound * self.input_value

    def grams_to_pounds(self):
        self.output_value = (1 / constants.pound) * self.input_value * constants.gram

    def pounds_to_grams(self):
        self.output_value = constants.pound * self.input_value * constants.gram

    def kilograms_to_ounces(self):
        self.output_value = (1 / constants.ounce) * self.input_value

    def ounces_to_kilograms(self):
        self.output_value = constants.ounce * self.input_value

    def grams_to_ounces(self):
        self.output_value = (1 / constants.ounce) * self.input_value * constants.gram

    def ounces_to_grams(self):
        self.output_value = constants.ounce * self.input_value * constants.gram

    def meters_to_inches(self):
        self.output_value = (1 / constants.inch) * self.input_value

    def inches_to_meters(self):
        self.output_value = constants.inch * self.input_value

    def meters_to_feet(self):
        self.output_value = (1 / constants.foot) * self.input_value

    def feet_to_meters(self):
        self.output_value = constants.foot * self.input_value

    def meters_to_yards(self):
        self.output_value = (1 / constants.yard) * self.input_value

    def yards_to_meters(self):
        self.output_value = constants.yard * self.input_value

    def meters_to_miles(self):
        self.output_value = (1 / constants.mile) * self.input_value

    def miles_to_meters(self):
        self.output_value = constants.mile * self.input_value

    def joules_to_ev(self):
        self.output_value = (1 / constants.eV) * self.input_value

    def ev_to_joules(self):
        self.output_value = constants.eV * self.input_value

    def joules_to_calories(self):
        self.output_value = (1 / constants.calorie) * self.input_value

    def calories_to_joules(self):
        self.output_value = constants.calorie * self.input_value
