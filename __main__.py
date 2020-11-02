import tkinter as tk
from tkinter.font import Font
import random
import pyperclip

# only symbols AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz123456789

# Constants
BG = "#EFEFEF"
FG = "#3B413C"
REL_STYLE = "groove"
DEFAULT_DISALLOWED = "{}[]()#$%^&*`,./?\\|\'\";:+~="
ICON = "pinwheel.ico"


class SubWindow(tk.Toplevel):
    def __init__(self, title, geometry):
        super().__init__()

        # Window
        self.geometry(geometry)
        self.resizable(False, False)
        self.title(title)
        self.configure(bg=BG)
        self.iconbitmap(ICON)

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window
        self.geometry("600x300+630+200")
        self.resizable(False, False)
        self.title("Password Generator")
        self.configure(bg=BG)
        self.iconbitmap(ICON)

        # Labels
        self.pw_display = tk.Label(
            self, text="Password will appear here (Max length of 24)", font=Font(size=16), bg=BG, fg=FG)
        self.pw_display.place(anchor="n", relx=0.5, rely=0.35)

        self.disallowed_label = tk.Label(
            self, text="To exclude:", font=Font(size=16), bg=BG, fg=FG)
        self.disallowed_label.place(anchor="n", relx=0.15, rely=0.02)

        self.pw_length_label = tk.Label(
            self, text="Length:", font=Font(size=16), bg=BG, fg=FG)
        self.pw_length_label.place(anchor="n", relx=0.15, rely=0.14)

        # Buttons
        self.generate = tk.Button(
            self, text="Generate Password", font=Font(size=16), bg=BG, fg=FG,
            relief=REL_STYLE,
            command=lambda: self.generate_password())
        self.generate.place(anchor="n", relx=0.5, rely=0.5, relwidth=1, relheight=0.2)

        self.copy_pw = tk.Button(
            self, text="Copy to clipboard", font=Font(size=16), bg=BG, fg=FG,
            relief=REL_STYLE, command=lambda: pyperclip.copy(self.pw))
        self.copy_pw.place(anchor="n", relx=0.5, rely=0.7, relwidth=1, relheight=0.2)

        self.help_button = tk.Button(
            self, text="Get help", font=Font(size=16), bg=BG, fg=FG,
            relief=REL_STYLE, command=lambda: self.open_help())
        self.help_button.place(anchor="n", relx=0.5, rely=0.9, relwidth=1, relheight=0.1)

        # Entries
        self.disallowed_entry = tk.Entry(
            self, relief=REL_STYLE, font=Font(size=12))
        self.disallowed_entry.place(anchor="n", relx=0.62, rely=0.02, relwidth=0.66, relheight=0.10)
        self.disallowed_entry.insert(0, DEFAULT_DISALLOWED)

        self.pw_length = tk.Entry(
            self, relief=REL_STYLE, font=Font(size=12))
        self.pw_length.place(anchor="n", relx=0.62, rely=0.14, relwidth=0.66, relheight=0.10)

    # Functions
    def generate_password(self):
        allowed_chars = [chr(i) for i in range(33, 127) if chr(i) not in self.disallowed_entry.get()]
        try:
            length = int(self.pw_length.get())
            pw = "".join(random.choices(allowed_chars, k=(length if length<=24 else 8)))
            self.pw_display["text"] = pw
            self.pw = pw
        except ValueError: # as e:
            # print(f"Caught error (Btw hey ace):\n{e}")
            pw = "".join(random.choices(allowed_chars, k=8))
            self.pw_display["text"] = pw
            self.pw = pw

    def open_help(self):
        help_window = SubWindow("Help", "600x100+630+70")
        tk.Label(
            help_window,
            text="Fill 'To Exclude' with any characters you don't want to be in your password.",
            font=Font(size=12, weight="bold"), bg=BG, fg=FG, wraplength=500).place(anchor="n", relx=0.5)
        tk.Label(
            help_window,
            text="Leave 'Length' empty to generate a password with a defualt length of 8, otherwise provide a length you desire",
            font=Font(size=12, weight="bold"), bg=BG, fg=FG, wraplength=500).place(anchor="n", relx=0.5, rely=0.5)

if __name__ == "__main__":
    MainWindow().mainloop()