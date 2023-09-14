Hello everyone! This is the first "project" I created for fun a couple of months ago, and I just wanted to post it on GitHub. Let me know if there is something wrong with my code or if there is something I should improve upon.
FYI I did not spend much time refining my code, so the code may look "unclean," as some might say.

# What I did
So this project uses Python and its standard libraries, such as tkinter, pickle, and hashlib.
I first created the Bank class (located inside of Bank.py), which initializes an account balance and has a deposit and withdraw function.

Then, I created the BankAccount class (located inside of bank_account.py), which is where the account username and hashed password. It also has the check_password function to check if the password inputted is the same as the hashed password saved.
I don't know much about cryptography, but I created a hashed password because I think it is somewhat secure.

The last thing I created, the most challenging part for me, was the bank GUI (found in bank_gui.py). It was hard because of I never used tkinter. I looked at the tkinter documentation from [docs.python.org](https://docs.python.org/3/library/tkinter.html) which gave
me a list of websites to look at how to use tkinter, I think I mainly used [tkdocs](https://tkdocs.com/shipman/). There were lots of GUI configurations(color, size, etc) I did but mainly worked on the create_account_page, create_account, select_account_page, etc. 
I also created a different withdraw/deposit function for the GUI that uses the functions from Bank.py.

After I finished with the code, I was happy with my results. I added some pytest elements to this project. Only left the example if anyone pulls this repo.
