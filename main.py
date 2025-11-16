# main.py
import tkinter as tk
from game_app import NumericalMethodsGame

if __name__ == "__main__":
    root = tk.Tk()
    app = NumericalMethodsGame(root)
    root.mainloop()