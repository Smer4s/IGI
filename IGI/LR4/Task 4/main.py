import math
from parallelogram import Parallelogram
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def input_parameters():
    try:
        d1 = float(input("Enter the d1 length of the parallelogam (max 50): "))
        d2 = float(input("Enter the d2 length of the parallelogam (max 50): "))
        alpha = float(input("Enter the degrees of the parallelogram (max 180): "))
        color = input("Enter the color of the parallelogram: ")
        return d1, d2, alpha, color
    except ValueError:
        print("Invalid input. Please enter numerical values for the side length.")
        return None, None


def validate_input(d1, d2, alpha, color):
   if d1 <= 0 or d1 > 50:
      print("Side length should be a positive number but less or equal 50.")
      return False
   
   if d2 <= 0 or d2 > 50:
      print("Side length should be a positive number but less or equal 50.")
      return False
   
   if alpha <= 0 or alpha >=180:
      print("Alpha should be positive and less or equal than 180 degrees.")
      return False
    
   if not color:
      print("Color should not be empty.")
      return False
   return True


def draw_shape(parallelogram, text, filename):
   fig, ax = plt.subplots()

   alpha = math.radians(parallelogram.alpha)
   half_diag1 = parallelogram.d1 / 2
   half_diag2 = parallelogram.d2 / 2

    # Вычисление координат вершин параллелограмма
   points = [
      (0, 0),
      (half_diag1*math.sin(alpha), parallelogram.d2 * math.cos(alpha)),
      (parallelogram.d1 * math.sin(alpha), parallelogram.d2 * math.cos(alpha)),
      (half_diag1 * math.sin(alpha), 0)
   ]

   parallelogram = Polygon(points, closed=True, edgecolor='black', facecolor=parallelogram.color.color)
   ax.add_patch(parallelogram)
    
   ax.text(0.5, 0.5, text, horizontalalignment='center', verticalalignment='center', fontsize=12, color='black')
   ax.set_xlim(0, max(half_diag1, half_diag2) + 10)
   ax.set_ylim(0, max(half_diag1, half_diag2) + 10)
   ax.axis('off')

   plt.savefig(filename)
   plt.show()

def main():
    d1, d2, alpha, color = input_parameters()
    if validate_input(d1, d2, alpha, color):
        parallelogram = Parallelogram(d1, d2, alpha, color)
        parallelogram.figure_name = input("Input name of parallelogram: ")
        draw_shape(parallelogram, parallelogram.figure_name, 'Task 4/parallelogram.png')
        print(parallelogram)


if __name__ == "__main__":
    main()