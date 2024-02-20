import tkinter as tk
from file_operations import button_click

def createButtons(root):
    left_frame = tk.Frame(root, bg="lightgrey", width=320, height=720)
    left_frame.pack(side="left", fill="y")

    right_frame = tk.Frame(root, bg="lightgrey", width=320, height=720)
    right_frame.pack(side="left", fill="y")

    button_texts = [
        ("L", "R", "OVER (/)", "TIGHTENS (>)", "INTO", "CAUTION (!)", "KEEP", "HPR", "HPL", "JUNCTION", "DC", "UNSEEN"),
        ("1", "2", "3", "4", "5", "6", "SPACE", "JUMP", "BUMP", "0")
    ]

    for column, buttons in enumerate(button_texts):
        frame = left_frame if column == 0 else right_frame
        for text in buttons:
            button = tk.Button(frame, text=text, width=20, command=lambda text=text: button_click(text))
            button.pack(side="top")
