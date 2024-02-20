import tkinter as tk
from tkinter import filedialog

def button_click(word):
    write_to_file(word)
    update_preview()

def write_to_file(word):
    with open("output.txt", "a") as file:
        file.write(word)
        file.flush()  # Force the data to be written immediately

def update_preview():
    with open("output.txt", "r") as file:
        preview_label.config(text=file.read())

def save_to_custom_file():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "w") as file:
            with open("output.txt", "r") as original_file:
                file.write(original_file.read())
        root.destroy()

def add_newline():
    write_to_file(",\n")
    update_preview()

# Clear the contents of the file when the program starts
open("output.txt", "w").close()

# Create main window
root = tk.Tk()
root.title("Menu with Programmable Buttons")
root.geometry("1280x720")

# Create buttons
def create_button(frame, text, command):
    button = tk.Button(frame, text=text, width=20, command=lambda: button_click(text))
    button.pack(side="top")

left_frame = tk.Frame(root, bg="lightgrey", width=320, height=720)
left_frame.pack(side="left", fill="y")

right_frame = tk.Frame(root, bg="lightgrey", width=320, height=720)
right_frame.pack(side="left", fill="y")

button_texts = [
    (" L", " R", "/", "> ", "< ",", ", " ! ", " long "," el ","keep ", "in ","HPR ", "HPL ", "junction ", "DC ", "unseen "),
    ("1", "2", "3", "4", "5", "6", "7","8", " ", "jump ", "bump ", "0", "C ")
]

for column, buttons in enumerate(button_texts):
    frame = left_frame if column == 0 else right_frame
    for text in buttons:
        create_button(frame, text, button_click)

# Create Save and New Line buttons
save_button = tk.Button(right_frame, text="Save", width=20, command=save_to_custom_file)
save_button.pack(side="bottom")

new_line_button = tk.Button(right_frame, text="New Line", width=20, command=add_newline)
new_line_button.pack(side="bottom")

# Create preview label
preview_label = tk.Label(root, text="", bg="white", anchor="nw", justify="left", wraplength=800)
preview_label.place(x=660, y=10, width=920, height=700)

root.mainloop()
