
import tkinter as tk
from game_app import NumericalMethodsGame
if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))
    app = NumericalMethodsGame(root)
    root.mainloop()