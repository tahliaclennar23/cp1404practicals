from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Tahlia Clennar'


class UnitConversionApp(App):

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) * 1.61
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass
    # def handle_increment(self, value):
    #     try:
    # # handle_increment(input_text.text,-1)


UnitConversionApp().run()
