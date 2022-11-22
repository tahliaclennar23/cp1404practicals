from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = 'Tahlia Clennar'

CONVERSION = 1.61


class UnitConversionApp(App):
    """Convert miles to kilometers in GUI"""
    kilometers = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        miles = self.convert_to_number(value)
        self.kilometers = str(miles * CONVERSION)

    def handle_increment(self, value, increment):
        miles = self.convert_to_number(value) + increment
        self.root.ids.input_number.text = str(miles)

    def convert_to_number(self, string):
        """Convert string to number"""
        try:
            number = float(string)
        except ValueError:
            number = 0.0
        return number


UnitConversionApp().run()
