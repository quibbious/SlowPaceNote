import tkinter as tk
from buttons import createButtons
from file_operations import customFileSave, NewLine
from preview_label import createPreviewLabel

# Clear the contents of the file when the program starts
open("output.txt", "w").close()

# make main window
root = tk.Tk()
root.title("SlowPaceNote")
root.geometry("1280x720")

# make buttons
createButtons(root)

# make Save and New Line buttons
saveButton = tk.Button(root, text="Save", width=20, command=customFileSave)
saveButton.pack(side="bottom")

newLineButton = tk.Button(root, text="New Line", width=20, command=NewLine)
newLineButton.pack(side="bottom")

# make preview label
createPreviewLabel(root)

root.mainloop()
