from PySide6.QtCharts import QLineSeries, QChart, QChartView
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtGui import QPainter


class PressureChart(QChartView):
    def __init__(self):
        QChartView.__init__(self)
        self.count = 0
        self.series_list = []

        for i in range(16):
            series = QLineSeries()
            series.setName(f"Pa{i}")
            self.series_list.append(series)

        self.line_chart = QChart()
        self.line_chart.legend().hide()
        for series in self.series_list:
            self.line_chart.addSeries(series)

        self.line_chart.createDefaultAxes()
        self.line_chart.setTitle("Druck")

        self.setChart(self.line_chart)
        self.chart().setTheme(QChart.ChartTheme.ChartThemeBlueIcy)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.grab().setDevicePixelRatio(2)

        size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setMinimumSize(0, 300)
        self.line_chart.axisX().setRange(0, 300)
        self.line_chart.axisY().setRange(-1000, 1000)

    def update_chart(self, tlaskan_data: list):
        try:
            if self.count % 9 == 0:
                for i, value in enumerate(tlaskan_data):
                    self.series_list[i].append(round(self.count/9, 1), value)

                if self.count > 3000:
                    for i in range(16):
                        self.series_list[i].remove(0)
                    self.line_chart.axisX().setRange(min(self.series_list[0].pointsVector(), key=lambda p: p.x()).x(),
                                                     round(self.count/9, 1))

                self.update()
            self.count += 1
        except Exception as e:
            print(e)
