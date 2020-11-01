import tkinter as tk
from tkinter.font import Font
import random
import pyperclip

# only symbols AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz123456789


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Constats
        self.bg = "#EFEFEF"
        self.fg = "#3B413C"
        self.hl = "#D6D6D6"
        self.rel_style = "groove"
        default_disallowed = "{}[]()#$%^&*`,./?\\|\'\";:+~="

        # Window
        self.geometry("600x300+630+200")
        self.resizable(False, False)
        self.title("Password Generator")
        self.configure(bg=self.bg)

        # Labels
        self.pw_display = tk.Label(
            self, text="Password will appear here (Max length of 24)", font=Font(size=16), bg=self.bg, fg=self.fg)
        self.pw_display.place(anchor="n", relx=0.5, rely=0.35)

        self.disallowed_label = tk.Label(
            self, text="To exclude:", font=Font(size=16), bg=self.bg, fg=self.fg)
        self.disallowed_label.place(anchor="n", relx=0.15, rely=0.02)

        self.pw_length_label = tk.Label(
            self, text="Length:", font=Font(size=16), bg=self.bg, fg=self.fg)
        self.pw_length_label.place(anchor="n", relx=0.15, rely=0.14)

        # Buttons
        self.generate = tk.Button(
            self, text="Generate Password", font=Font(size=16), bg=self.bg, fg=self.fg,
            relief=self.rel_style,
            command=lambda: self.generate_password())
        self.generate.place(anchor="n", relx=0.5, rely=0.5, relwidth=1, relheight=0.2)

        self.copy_pw = tk.Button(
            self, text="Copy to clipboard", font=Font(size=16), bg=self.bg, fg=self.fg,
            relief=self.rel_style, command=lambda: pyperclip.copy(self.pw))
        self.copy_pw.place(anchor="n", relx=0.5, rely=0.7, relwidth=1, relheight=0.2)

        # Entries
        self.disallowed_entry = tk.Entry(
            self, relief=self.rel_style, font=Font(size=12))
        self.disallowed_entry.place(anchor="n", relx=0.62, rely=0.02, relwidth=0.66, relheight=0.10)
        self.disallowed_entry.insert(0, default_disallowed)

        self.pw_length = tk.Entry(
            self, relief=self.rel_style, font=Font(size=12))
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

if __name__ == "__main__":
    MainWindow().mainloop()