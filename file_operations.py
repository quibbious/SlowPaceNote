from tkinter import filedialog

def customFileSave():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "w") as file:
            with open("output.txt", "r") as original_file:
                file.write(original_file.read())

def NewLine():
    with open("output.txt", "a") as file:
        file.write(",\n")
