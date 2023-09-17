import tkinter as tk
from tkinter import messagebox, simpledialog
import pickle
from bank_account import BankAccount

class BankGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Bank GUI")
        self.master.configure(bg="#E6F2F5")

        self.bank_accounts = []
        self.load_bank_accounts()

        self.master.geometry("400x300")
        self.center_window()

        self.initial_page()

    def center_window(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry(f"{width}x{height}+{x}+{y}")

    def initial_page(self):
        self.clear_frame()

        label_frame = tk.Frame(self.master, bg="#E6F2F5")
        label_frame.pack(pady=20)

        tk.Label(label_frame, text="Welcome to the Bank", font=(
            "Helvetica", 16, "bold"), bg="#E6F2F5").pack()

        button_style = {"font": ("Helvetica", 10), "width": 15, "height": 1}

        tk.Button(self.master, text="Create Account",
                  command=self.create_account_page, **button_style).pack()
        tk.Button(self.master, text="Enter Account",
                  command=self.select_account_page, **button_style).pack()
        tk.Button(self.master, text="Exit",
                  command=self.exit, **button_style).pack()

    def create_account_page(self):
        self.clear_frame()

        label_frame = tk.Frame(self.master, bg="#E6F2F5")
        label_frame.pack(pady=20)
        tk.Label(label_frame, text="Enter a username:",
                 font=("Helvetica", 12), bg="#E6F2F5").pack()

        self.username_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.username_entry.pack()

        tk.Label(label_frame, text="Enter a password:",
                 font=("Helvetica", 12), bg="#E6F2F5").pack()

        self.password_entry = tk.Entry(
            self.master, font=("Helvetica", 12), show="*")
        self.password_entry.pack()

        button_style = {"font": ("Helvetica", 10), "width": 15, "height": 1}
        tk.Button(self.master, text="Create Account",
                  command=self.create_account, **button_style).pack()
        tk.Button(self.master, text="Back", command=self.initial_page, **button_style).pack()

    def create_account(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        if username and password:
            if self.check_username_available(username):
                new_account = BankAccount(username, password)
                self.bank_accounts.append(new_account)
                self.save_bank_accounts()
                self.initial_page()
            else:
                messagebox.showerror("Error", "Username already exists.")
        else:
            messagebox.showerror(
                "Error", "Username and password cannot be empty.")

    def select_account_page(self):
        self.clear_frame()

        label_frame = tk.Frame(self.master, bg="#E6F2F5")
        label_frame.pack(pady=20)
        tk.Label(label_frame, text="Enter your username:",
                 font=("Helvetica", 12), bg="#E6F2F5").pack()

        self.username_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.username_entry.pack()

        button_style = {"font": ("Helvetica", 10), "width": 15, "height": 1}
        tk.Button(self.master, text="Enter",
                  command=self.enter_account_selection, **button_style).pack()
        tk.Button(self.master, text="Back", command=self.initial_page, **button_style).pack()

    def enter_account_selection(self):
        username = self.username_entry.get().strip()
        account = self.get_account(username)
        if account:
            self.enter_account(account)
        else:
            messagebox.showerror("Error", "Account not found.")

    def enter_account(self, account):
        self.clear_frame()

        password_frame = tk.Frame(self.master, bg="#E6F2F5")
        password_frame.pack(pady=20)

        tk.Label(password_frame, text=f"Enter password for {account.username}:", font=(
            "Helvetica", 12), bg="#E6F2F5").pack()

        password_entry = tk.Entry(
            password_frame, font=("Helvetica", 12), show="*")
        password_entry.pack()

        button_style = {"font": ("Helvetica", 10), "width": 15, "height": 1}

        def verify_password():
            if account.check_password(password_entry.get()):
                self.show_account_page(account)
            else:
                messagebox.showerror("Error", "Incorrect password.")

        tk.Button(password_frame, text="Enter",
                  command=verify_password, **button_style).pack()
        tk.Button(password_frame, text="Back",
                  command=self.initial_page, **button_style).pack()

    def show_account_page(self, account):
        self.clear_frame()

        label_frame = tk.Frame(self.master, bg="#E6F2F5")
        label_frame.pack(pady=20)
        tk.Label(label_frame, text=f"Welcome, {account.username}!\nBalance: ${account.bank.viewaccount()}", font=(
            "Helvetica", 16, "bold"), bg="#E6F2F5").pack()

        button_style = {"font": ("Helvetica", 10), "width": 15, "height": 1}

        tk.Button(self.master, text="Deposit", command=lambda: self.deposit(
            account), **button_style).pack()
        tk.Button(self.master, text="Withdraw", command=lambda: self.withdraw(
            account), **button_style).pack()
        tk.Button(self.master, text="Back",
                  command=self.initial_page, **button_style).pack()

    def deposit(self, account):
        amount = simpledialog.askinteger(
            "Deposit", f"How much would you like to deposit into {account.username}'s account?")
        if amount is not None and amount > 0:
            account.bank.deposit(amount)
            self.save_bank_accounts()
            self.show_account_page(account)
        elif amount < 0:
            messagebox.showerror(
                "Error", "Deposit amount must be valid.")

    def withdraw(self, account):
        amount = simpledialog.askinteger(
            "Withdraw", f"How much would you like to withdraw from {account.username}'s account?")
        if amount is not None and amount > 0 and amount <= account.bank.accountbalance:
            account.bank.withdraw
            account.bank.withdraw(amount)
            self.save_bank_accounts()
            self.show_account_page(account)
        elif amount is not None:
            messagebox.showerror(
                "Error", "Withdrawal amount must be valid and less than account balance.")

    def load_bank_accounts(self):
        try:
            with open("bank_accounts.pickle", "rb") as file:
                self.bank_accounts = pickle.load(file)
        except FileNotFoundError:
            self.bank_accounts = []

    def save_bank_accounts(self):
        with open("bank_accounts.pickle", "wb") as file:
            pickle.dump(self.bank_accounts, file)

    def check_username_available(self, username):
        return not any(account.username == username for account in self.bank_accounts)

    def get_account(self, username):
        for account in self.bank_accounts:
            if account.username == username:
                return account
        return None

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def exit(self):
        self.save_bank_accounts()
        self.master.destroy()
