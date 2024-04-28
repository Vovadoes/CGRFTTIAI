import math

# from Charts import *

# from scipy.stats import t

# CONST
# None

class Calculation:
    def __init__(self, i, n, h):
        self.i = i
        self.n = n
        self.h = h
        self.r = None

    def f1(self):
        self.r = (((1 + self.n * self.i / 100) * math.pow(1 + self.h / 100, self.n) - 1) / self.n) * 100

    def f2(self):
        self.r = (self.h/100 + self.i / 100 + self.i * self.h / 10000) * 100


if __name__ == "__main__":
    i = 7
    n = 2
    h = 22

    calculation = Calculation(i, n, h)
    calculation.f1()
    print(calculation.r)
    calculation.f2()
    print(calculation.r)

    # ChartLinePLT(calculation.chart_v_y_data)
    # plt.legend()
    # plt.show()
