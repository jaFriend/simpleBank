import tkinter as tk
from bank_gui import BankGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = BankGUI(root)
    root.mainloop()