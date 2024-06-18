import unittest
import time_series_visualizer

class TestCase(unittest.TestCase):
    def setUp(self):
        self.visualizer = time_series_visualizer

    def test_line_plot(self):
        fig = self.visualizer.draw_line_plot()
        self.assertIsNotNone(fig)

    def test_bar_plot(self):
        fig = self.visualizer.draw_bar_plot()
        self.assertIsNotNone(fig)

    def test_box_plot(self):
        fig = self.visualizer.draw_box_plot()
        self.assertIsNotNone(fig)

if __name__ == '__main__':
    unittest.main()
