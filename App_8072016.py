from tkinter import *

class Average_Menu:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.averageButton = Button(frame, text = "Average Calculation", width = 25,  command = Average).pack()
        self.quitButton = Button(frame, text = "Quit",width = 25, command = master.destroy).pack()
    i
    def Average(numbers, self, master):
        frame = Frame(master)
        self.input = input("Enter the digits seperated by a comma:.")
        input_list = input.split(',')
        numbers = [float(x.strip()) for x in input_list]
        total = 0
        for i in numbers:
            total += i
        Average = total / float(len(numbers))
        w = Label(frame, text = Average, bg = "White", fg = "Black")

def main():
    Average(numbers)
    root = Tk()
    Average_Menu(root)
    root.mainloop()
if __name__ ='__main__':
    main()



