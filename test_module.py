

import unittest
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

class TestTimeSeriesVisualizer(unittest.TestCase):
    def test_line_plot(self):
        fig = draw_line_plot()
        self.assertIsNotNone(fig)

    def test_bar_plot(self):
        fig = draw_bar_plot()
        self.assertIsNotNone(fig)

    def test_box_plot(self):
        fig = draw_box_plot()
        self.assertIsNotNone(fig)

if __name__ == "__main__":
    unittest.main()
