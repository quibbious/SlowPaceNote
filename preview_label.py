import tkinter as tk

def createPreviewLabel(root):
    preview_label = tk.Label(root, text="", bg="white", anchor="nw", justify="left", wraplength=800)
    preview_label.place(x=660, y=10, width=920, height=700)
