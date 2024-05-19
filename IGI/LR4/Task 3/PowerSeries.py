import math
import matplotlib.pyplot as plt
import numpy as np
from statistics import median, mode, variance, stdev


class PowerSeries:
    def __init__(self, eps: float):
        self.member = 0
        self.eps = eps
        self.result = 0
        self.n = 0
        self.factorial = 1
        self.double_n_factorial = 1
        self.series_values = []

    @staticmethod
    def argument_check(arg):
        if abs(arg) > 1:
            raise ValueError("Argument must be in range (-1, 1)")

    def compute_statistics(self):
        """Compute additional statistics"""
        mean = sum(self.series_values) / len(self.series_values)
        med = median(self.series_values)
        mod = mode(self.series_values)
        var = variance(self.series_values)
        std_dev = stdev(self.series_values)
        return mean, med, mod, var, std_dev

    def calculate_arcsin(self, arg):
        """Calculate arcsin using power series"""
        self.argument_check(arg)
        self.member = arg
        self.factorial = 1
        self.double_n_factorial = 1
        self.n = 0
        self.result = 0
        while self.n < 500 and math.fabs(self.member) > self.eps:
            self.result += self.member
            self.factorial *= (self.n + 1)
            self.double_n_factorial *= (2 * self.n + 1) * (2 * (self.n + 1))
            self.n += 1
            self.member = (self.double_n_factorial /
                           (math.pow(4, self.n) *
                            math.pow(self.factorial, 2) *
                            (2 * self.n + 1))) * math.pow(arg, 2 * self.n + 1)
            self.series_values.append(self.result)
            
        return self.result

    def draw_graphs(self, filename: str):
        """Draw graphs using matplotlib and save to file"""
        x_values = np.linspace(-1, 1, 100)
        y_values = [math.asin(x) for x in x_values]
        y_values_series = [self.calculate_arcsin(x) for x in x_values]

        plt.plot(x_values, y_values_series, color='red', label='series')
        plt.plot(x_values, y_values, color='blue', label='math.asin')

        plt.xlabel('x')
        plt.ylabel('Value')
        plt.title('Graphs of Power Series and math.asin Function')
        plt.legend()
        plt.grid(True)

        plt.savefig(filename)
        plt.show()
        plt.close()
