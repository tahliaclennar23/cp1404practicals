"""CP1404 Practical 8
Tahlia Clennar
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Display names in list"""
    def __init__(self, **kwargs):
        """Create Main app"""
        super().__init__(**kwargs)
        self.names = ["Tahlia", "Bob", "Billy", "Bianca"]

    def build(self):
        """Build GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.make_labels()
        return self.root

    def make_labels(self):
        """Create labels"""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()
