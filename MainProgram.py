from tkinter import *
import tkinter as tk


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainWindow, Calculate_Average, Calculate_Best_Time, Display_Average, Display_Best_Time, Open_External_Programs, Change_Settings  ):
            page_name = F.__name__
            frame = F(parent = container, controller = self)
            self.frames[page_name] = frame


            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainWindow")

    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()

class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.button = tk.Button(self, text="Calculate Average",command=lambda: controller.show_frame("Calculate_Average")).pack(side="top", fill = X)
        self.button = tk.Button(self, text="Calculate Best Time",command=lambda: controller.show_frame("Calculate_Best_Time")).pack(fill = X)
        self.button = tk.Button(self, text="Display Average",command=lambda: controller.show_frame("Display_Average")).pack(fill = X)
        self.button = tk.Button(self, text="Display Best Time",command=lambda: controller.show_frame("Display_Best_Time")).pack(fill = X)
        self.button = tk.Button(self, text="Open External Programs",command=lambda: controller.show_frame("Open_External_Programs")).pack(fill = X)
        self.button = tk.Button(self, text="Change Settings",command=lambda: controller.show_frame("Change_Settings")).pack(fill = X)


class Calculate_Average(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        t = tk.Toplevel(self)
        t.wm_title("Calculate Average")
        l = tk.Label(t, text="Input data here")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
        button = tk.Button(self, text="Back",command=lambda: controller.show_frame("MainWindow"))
        button.pack(side="top", fill = X)


class Calculate_Best_Time(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        t = tk.Toplevel(self)
        t.wm_title("Better Time")
        l = tk.Label(t, text="Input data here")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
        button = tk.Button(self, text="Back",command=lambda: controller.show_frame("MainWindow"))
        button.pack(side="top", fill = X)


class Display_Average(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        t = tk.Toplevel(self)
        t.wm_title("Average")
        l = tk.Label(t, text="Input data here")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
        button = tk.Button(self, text="Back",command=lambda: controller.show_frame("MainWindow"))
        button.pack(side="top", fill = X)


class Display_Best_Time(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        t = tk.Toplevel(self)
        t.wm_title("Display Best time")
        l = tk.Label(t, text="Input data here")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
        button = tk.Button(self, text="Back",command=lambda: controller.show_frame("MainWindow"))
        button.pack(side="top", fill = X)


class Open_External_Programs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        t = tk.Toplevel(self)
        t.wm_title("External Programs")
        l = tk.Label(t, text="Input data here")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
        button = tk.Button(self, text="Back",command=lambda: controller.show_frame("MainWindow"))
        button.pack(side="top", fill = X)


class Change_Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        t = tk.Toplevel(self)
        t.wm_title("Calculate Average")
        l = tk.Label(t, text="Input data here")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
        button = tk.Button(self, text="Back",command=lambda: controller.show_frame("MainWindow"))
        button.pack(side="top", fill = X)

if __name__ == "__main__":
    main = App()
    main.mainloop()