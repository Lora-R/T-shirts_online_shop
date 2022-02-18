import tkinter as tk
from render_screen import render_main_screen

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('700x900')
    window.title("Exercise")
    render_main_screen(window)
    window.mainloop()