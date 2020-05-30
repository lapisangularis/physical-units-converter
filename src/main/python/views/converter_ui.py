from PyQt5 import QtCore, QtGui, QtWidgets


class ConverterUi(object):
    def _setup_layouts(self):
        self.vbox_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.vbox_layout.setObjectName("vboxlayout")
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("vertical_layout")
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2.setObjectName("horizontal_layout_2")
        self.horizontal_layout_3 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_3.setObjectName("horizontal_layout_3")
        self.horizontal_layout_4 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_4.setObjectName("horizontal_layout_4")
        self.horizontal_layout_5 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_5.setObjectName("horizontal_layout_5")
        self.horizontal_layout_6 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_6.setObjectName("horizontal_layout_6")

    def _setup_edit_fields(self):
        self.line_edit_input_value = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_input_value.setObjectName("line_edit_input_value")
        self.line_edit_input_value.setValidator(QtGui.QDoubleValidator(decimals=10))
        self.line_edit_output_value = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_output_value.setObjectName("line_edit_output_value")

        self.push_button_reset = QtWidgets.QPushButton(self.central_widget)
        self.push_button_reset.setEnabled(False)
        self.push_button_reset.setObjectName("push_button_reset")

        self.horizontal_layout.addWidget(self.line_edit_input_value)
        self.horizontal_layout.addWidget(self.line_edit_output_value)
        self.horizontal_layout.addWidget(self.push_button_reset)

    def _setup_pounds(self):
        self.push_button_kilograms_to_pounds = QtWidgets.QPushButton(self.central_widget)
        self.push_button_kilograms_to_pounds.setEnabled(True)
        self.push_button_kilograms_to_pounds.setObjectName("push_button_kilograms_to_pounds")
        self.horizontal_layout_2.addWidget(self.push_button_kilograms_to_pounds)

        self.push_button_pounds_to_kilograms = QtWidgets.QPushButton(self.central_widget)
        self.push_button_pounds_to_kilograms.setEnabled(True)
        self.push_button_pounds_to_kilograms.setObjectName("push_button_pounds_to_kilograms")
        self.horizontal_layout_2.addWidget(self.push_button_pounds_to_kilograms)

        self.push_button_grams_to_pounds = QtWidgets.QPushButton(self.central_widget)
        self.push_button_grams_to_pounds.setEnabled(True)
        self.push_button_grams_to_pounds.setObjectName("push_button_grams_to_pounds")
        self.horizontal_layout_2.addWidget(self.push_button_grams_to_pounds)

        self.push_button_pounds_to_grams = QtWidgets.QPushButton(self.central_widget)
        self.push_button_pounds_to_grams.setEnabled(True)
        self.push_button_pounds_to_grams.setObjectName("push_button_pounds_to_grams")
        self.horizontal_layout_2.addWidget(self.push_button_pounds_to_grams)

    def _setup_ounces(self):
        self.push_button_kilograms_to_ounces = QtWidgets.QPushButton(self.central_widget)
        self.push_button_kilograms_to_ounces.setEnabled(True)
        self.push_button_kilograms_to_ounces.setObjectName("push_button_kilograms_to_ounces")
        self.horizontal_layout_3.addWidget(self.push_button_kilograms_to_ounces)

        self.push_button_ounces_to_kilograms = QtWidgets.QPushButton(self.central_widget)
        self.push_button_ounces_to_kilograms.setEnabled(True)
        self.push_button_ounces_to_kilograms.setObjectName("push_button_ounces_to_kilograms")
        self.horizontal_layout_3.addWidget(self.push_button_ounces_to_kilograms)

        self.push_button_grams_to_ounces = QtWidgets.QPushButton(self.central_widget)
        self.push_button_grams_to_ounces.setEnabled(True)
        self.push_button_grams_to_ounces.setObjectName("push_button_grams_to_ounces")
        self.horizontal_layout_3.addWidget(self.push_button_grams_to_ounces)

        self.push_button_ounces_to_grams = QtWidgets.QPushButton(self.central_widget)
        self.push_button_ounces_to_grams.setEnabled(True)
        self.push_button_ounces_to_grams.setObjectName("push_button_ounces_to_grams")
        self.horizontal_layout_3.addWidget(self.push_button_ounces_to_grams)

    def _setup_inches(self):
        self.push_button_meters_to_inches = QtWidgets.QPushButton(self.central_widget)
        self.push_button_meters_to_inches.setEnabled(True)
        self.push_button_meters_to_inches.setObjectName("push_button_meters_to_inches")
        self.horizontal_layout_4.addWidget(self.push_button_meters_to_inches)

        self.push_button_inches_to_meters = QtWidgets.QPushButton(self.central_widget)
        self.push_button_inches_to_meters.setEnabled(True)
        self.push_button_inches_to_meters.setObjectName("push_button_inches_to_meters")
        self.horizontal_layout_4.addWidget(self.push_button_inches_to_meters)

    def _setup_feet(self):
        self.push_button_meters_to_feet = QtWidgets.QPushButton(self.central_widget)
        self.push_button_meters_to_feet.setEnabled(True)
        self.push_button_meters_to_feet.setObjectName("push_button_meters_to_feet")
        self.horizontal_layout_4.addWidget(self.push_button_meters_to_feet)

        self.push_button_feet_to_meters = QtWidgets.QPushButton(self.central_widget)
        self.push_button_feet_to_meters.setEnabled(True)
        self.push_button_feet_to_meters.setObjectName("push_button_feet_to_meters")
        self.horizontal_layout_4.addWidget(self.push_button_feet_to_meters)

    def _setup_yards(self):
        self.push_button_meters_to_yards = QtWidgets.QPushButton(self.central_widget)
        self.push_button_meters_to_yards.setEnabled(True)
        self.push_button_meters_to_yards.setObjectName("push_button_meters_to_yards")
        self.horizontal_layout_5.addWidget(self.push_button_meters_to_yards)

        self.push_button_yards_to_meters = QtWidgets.QPushButton(self.central_widget)
        self.push_button_yards_to_meters.setEnabled(True)
        self.push_button_yards_to_meters.setObjectName("push_button_yards_to_meters")
        self.horizontal_layout_5.addWidget(self.push_button_yards_to_meters)

    def _setup_miles(self):
        self.push_button_meters_to_miles = QtWidgets.QPushButton(self.central_widget)
        self.push_button_meters_to_miles.setEnabled(True)
        self.push_button_meters_to_miles.setObjectName("push_button_meters_to_miles")
        self.horizontal_layout_5.addWidget(self.push_button_meters_to_miles)

        self.push_button_miles_to_meters = QtWidgets.QPushButton(self.central_widget)
        self.push_button_miles_to_meters.setEnabled(True)
        self.push_button_miles_to_meters.setObjectName("push_button_miles_to_meters")
        self.horizontal_layout_5.addWidget(self.push_button_miles_to_meters)

    def _setup_ev(self):
        self.push_button_joules_to_ev = QtWidgets.QPushButton(self.central_widget)
        self.push_button_joules_to_ev.setEnabled(True)
        self.push_button_joules_to_ev.setObjectName("push_button_joules_to_ev")
        self.horizontal_layout_6.addWidget(self.push_button_joules_to_ev)

        self.push_button_ev_to_joules = QtWidgets.QPushButton(self.central_widget)
        self.push_button_ev_to_joules.setEnabled(True)
        self.push_button_ev_to_joules.setObjectName("push_button_ev_to_joules")
        self.horizontal_layout_6.addWidget(self.push_button_ev_to_joules)

    def _setup_calories(self):
        self.push_button_joules_to_calories = QtWidgets.QPushButton(self.central_widget)
        self.push_button_joules_to_calories.setEnabled(True)
        self.push_button_joules_to_calories.setObjectName("push_button_joules_to_calories")
        self.horizontal_layout_6.addWidget(self.push_button_joules_to_calories)

        self.push_button_calories_to_joules = QtWidgets.QPushButton(self.central_widget)
        self.push_button_calories_to_joules.setEnabled(True)
        self.push_button_calories_to_joules.setObjectName("push_button_calories_to_joules")
        self.horizontal_layout_6.addWidget(self.push_button_calories_to_joules)

    def setup_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(500, 50)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self._setup_layouts()

        spacer_item = QtWidgets.QSpacerItem(10, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.vertical_layout.addItem(spacer_item)

        self._setup_edit_fields()
        self._setup_pounds()
        self._setup_ounces()
        self._setup_inches()
        self._setup_feet()
        self._setup_yards()
        self._setup_miles()
        self._setup_ev()
        self._setup_calories()

        self.vertical_layout.addLayout(self.horizontal_layout)
        self.vertical_layout.addLayout(self.horizontal_layout_2)
        self.vertical_layout.addLayout(self.horizontal_layout_3)
        self.vertical_layout.addLayout(self.horizontal_layout_4)
        self.vertical_layout.addLayout(self.horizontal_layout_5)
        self.vertical_layout.addLayout(self.horizontal_layout_6)

        self.vbox_layout.addLayout(self.vertical_layout)
        main_window.setCentralWidget(self.central_widget)

        self.translate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def translate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        self.central_widget.setWindowTitle(_translate("main_window", "Physical Units Converter"))
        self.push_button_reset.setText(_translate("main_window", "Reset"))

        self.push_button_kilograms_to_pounds.setText(_translate("main_window", "kg / lb"))
        self.push_button_pounds_to_kilograms.setText(_translate("main_window", "lb / kg"))
        self.push_button_grams_to_pounds.setText(_translate("main_window", "g / lb"))
        self.push_button_pounds_to_grams.setText(_translate("main_window", "lb / g"))

        self.push_button_kilograms_to_ounces.setText(_translate("main_window", "kg / oz"))
        self.push_button_ounces_to_kilograms.setText(_translate("main_window", "oz / kg"))
        self.push_button_grams_to_ounces.setText(_translate("main_window", "g / oz"))
        self.push_button_ounces_to_grams.setText(_translate("main_window", "oz / g"))

        self.push_button_meters_to_inches.setText(_translate("main_window", "m / in"))
        self.push_button_inches_to_meters.setText(_translate("main_window", "in / m"))

        self.push_button_meters_to_feet.setText(_translate("main_window", "m / ft"))
        self.push_button_feet_to_meters.setText(_translate("main_window", "ft / m"))

        self.push_button_meters_to_yards.setText(_translate("main_window", "m / yd"))
        self.push_button_yards_to_meters.setText(_translate("main_window", "yd / m"))

        self.push_button_meters_to_miles.setText(_translate("main_window", "m / mi"))
        self.push_button_miles_to_meters.setText(_translate("main_window", "mi / m"))

        self.push_button_joules_to_ev.setText(_translate("main_window", "J / eV"))
        self.push_button_ev_to_joules.setText(_translate("main_window", "eV / J"))

        self.push_button_joules_to_calories.setText(_translate("main_window", "J / cal"))
        self.push_button_calories_to_joules.setText(_translate("main_window", "cal / J"))
