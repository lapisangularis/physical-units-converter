from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from .converter_ui import ConverterUi


class ConverterView(QMainWindow):
    def _connect_actions_pounds(self):
        self._ui.push_button_kilograms_to_pounds.clicked.connect(
            lambda: self._controller.calculate_kilograms_to_pounds(self._ui.line_edit_input_value.text()))
        self._ui.push_button_pounds_to_kilograms.clicked.connect(
            lambda: self._controller.calculate_pounds_to_kilograms(self._ui.line_edit_input_value.text()))
        self._ui.push_button_grams_to_pounds.clicked.connect(
            lambda: self._controller.calculate_grams_to_pounds(self._ui.line_edit_input_value.text()))
        self._ui.push_button_pounds_to_grams.clicked.connect(
            lambda: self._controller.calculate_pounds_to_grams(self._ui.line_edit_input_value.text()))

    def _connect_actions_ounces(self):
        self._ui.push_button_kilograms_to_ounces.clicked.connect(
            lambda: self._controller.calculate_kilograms_to_ounces(self._ui.line_edit_input_value.text()))
        self._ui.push_button_ounces_to_kilograms.clicked.connect(
            lambda: self._controller.calculate_ounces_to_kilograms(self._ui.line_edit_input_value.text()))
        self._ui.push_button_grams_to_ounces.clicked.connect(
            lambda: self._controller.calculate_grams_to_ounces(self._ui.line_edit_input_value.text()))
        self._ui.push_button_ounces_to_grams.clicked.connect(
            lambda: self._controller.calculate_ounces_to_grams(self._ui.line_edit_input_value.text()))

    def _connect_actions_inches(self):
        self._ui.push_button_meters_to_inches.clicked.connect(
            lambda: self._controller.calculate_meters_to_inches(self._ui.line_edit_input_value.text()))
        self._ui.push_button_inches_to_meters.clicked.connect(
            lambda: self._controller.calculate_inches_to_meters(self._ui.line_edit_input_value.text()))

    def _connect_actions_feet(self):
        self._ui.push_button_meters_to_feet.clicked.connect(
            lambda: self._controller.calculate_meters_to_feet(self._ui.line_edit_input_value.text()))
        self._ui.push_button_feet_to_meters.clicked.connect(
            lambda: self._controller.calculate_feet_to_meters(self._ui.line_edit_input_value.text()))

    def _connect_actions_yards(self):
        self._ui.push_button_meters_to_yards.clicked.connect(
            lambda: self._controller.calculate_meters_to_yards(self._ui.line_edit_input_value.text()))
        self._ui.push_button_yards_to_meters.clicked.connect(
            lambda: self._controller.calculate_yards_to_meters(self._ui.line_edit_input_value.text()))

    def _connect_actions_miles(self):
        self._ui.push_button_meters_to_miles.clicked.connect(
            lambda: self._controller.calculate_meters_to_miles(self._ui.line_edit_input_value.text()))
        self._ui.push_button_miles_to_meters.clicked.connect(
            lambda: self._controller.calculate_miles_to_meters(self._ui.line_edit_input_value.text()))

    def _connect_actions_ev(self):
        self._ui.push_button_joules_to_ev.clicked.connect(
            lambda: self._controller.calculate_joules_to_ev(self._ui.line_edit_input_value.text()))
        self._ui.push_button_ev_to_joules.clicked.connect(
            lambda: self._controller.calculate_ev_to_joules(self._ui.line_edit_input_value.text()))

    def _connect_actions_calories(self):
        self._ui.push_button_joules_to_calories.clicked.connect(
            lambda: self._controller.calculate_joules_to_calories(self._ui.line_edit_input_value.text()))
        self._ui.push_button_calories_to_joules.clicked.connect(
            lambda: self._controller.calculate_calories_to_joules(self._ui.line_edit_input_value.text()))

    def _connect_actions(self):
        self._connect_actions_pounds()
        self._connect_actions_ounces()
        self._connect_actions_inches()
        self._connect_actions_feet()
        self._connect_actions_yards()
        self._connect_actions_miles()
        self._connect_actions_ev()
        self._connect_actions_calories()
        self._ui.push_button_reset.clicked.connect(lambda: self._controller.calculate_kilograms_to_pounds(1))

    def _update_ui(self):
        self._model.input_value_changed.connect(self.on_input_value_changed)
        self._model.output_value_changed.connect(self.on_output_value_changed)
        self._model.enable_reset_changed.connect(self.on_enable_reset_changed)

    def _set_defaults(self):
        self._controller.calculate_kilograms_to_pounds(1)

    def __init__(self, model, controller):
        super().__init__()
        self._model = model
        self._controller = controller
        self._ui = ConverterUi()
        self._ui.setup_ui(self)
        self._connect_actions()
        self._update_ui()
        self._set_defaults()

    @pyqtSlot(float)
    def on_input_value_changed(self, value):
        self._ui.line_edit_input_value.setText(str(value))

    @pyqtSlot(float)
    def on_output_value_changed(self, value):
        self._ui.line_edit_output_value.setText(str(value))

    @pyqtSlot(bool)
    def on_enable_reset_changed(self, value):
        self._ui.push_button_reset.setEnabled(value)
