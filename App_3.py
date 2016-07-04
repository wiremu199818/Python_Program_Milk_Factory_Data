from tkinter import *
import tkinter as tk
from math import *

#Opens up the first menu.
class Average_Calculator:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Average Calculation', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Average_Window_2(self.newWindow)
#Average calculation
n = []
def n_input(): #Data input TODO: Make data input from entry go into list "n" and then calculate Average.
    n.append(entry)
class Average:
    def print_n(n):
        for i in n:
            print (i)
            return (i)
    def n_sum(n):
        total = 0
        for i in n: 
            total += i
        return total
    def n_average(n):
        sum_of_n = n_sum(n)
        average = sum_of_n / int(len(n))
        return average
#Data input menu.
class Average_Window_2:
    def __init__(self, master):
        self.master = master
        w = Tk()
        w.title = ("Program")
        w.geometry("500x200")
        Label(self, text = "Input your data using the enter key after each piece of data.").pack()
        entry = Entry(self)
        entry.bind("<Return>")
        entry.pack()
        res = Label(self)
        res.pack
        self.calculateButtion = tk.Button(w, text = 'Calculate Average', width = 25, command = Average).pack()
        self.quitButton = tk.Button(w, text = 'Quit', width = 25, command = self.close_windows).pack()
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = Average_Calculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
