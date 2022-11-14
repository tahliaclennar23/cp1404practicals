"""
CP1404 Tahlia Clennar
Box layout modifications
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build GUI"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greet"""
        print('greet')
        print("test")
        # self.root.ids.output_label.text = "Hello "
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handle clear"""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
