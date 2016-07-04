from tkinter import *
from math import *
from openpyxl import *

root = Tk()
root.title('Average Calculator')
root.geometry("500x200")

class AverageCalculator(object):
    def __init__(self, digit, average_list):
        self.digit = digit
        self.average_list = average_list
        average_list = []
        digits = int(input("Enter your set of numbers."))
        average_list.append(digits)
    def print_average_list(
        
        
