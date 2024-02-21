import customtkinter as ctk
from customtkinter import filedialog

def left_button_click():
    write_to_file("L")
    update_preview()

def right_button_click():
    write_to_file("R")
    update_preview()

def number_button_click(number):
    write_to_file(str(number))
    update_preview()

def write_to_file(word):
    with open("output.txt", "a") as file:
        file.write(word)
        file.flush()

def update_preview():
    with open("output.txt", "r") as file:
        content = file.read()
        preview_label.configure(text=content)

def save_to_custom_file():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "w") as file:
            with open("output.txt", "r") as original_file:
                file.write(original_file.read())
        root.destroy()

def add_newline(event=None):
    write_to_file(",\n")
    update_preview()


def print_slash():
    write_to_file(r"/")
    update_preview()


def print_tightens():
    write_to_file(r"> ")
    update_preview()


def print_into():
    write_to_file(r", ")
    update_preview()


def print_crest():
    write_to_file(r"C ")
    update_preview()


def print_opens():
    write_to_file(r"< ")
    update_preview()

def print_space(event=None):
    write_to_file(r" ")
    update_preview()


def print_caution():
    write_to_file(r" ! ")
    update_preview()


def print_keep():
    write_to_file(r" keep")
    update_preview()


def print_jump():
    write_to_file(r" jump")
    update_preview()


def print_bump():
    write_to_file(r" bump")
    update_preview()

def print_unseen():
    write_to_file(r" unseen")
    update_preview()


def print_hpr():
    write_to_file(r" HPR")
    update_preview()


def print_hpl():
    write_to_file(r" HPL")
    update_preview()


def print_junction():
    write_to_file(r"junction ")
    update_preview()


def print_dc():
    write_to_file(r" DC")
    update_preview()


def print_zero():
    write_to_file(r"0")
    update_preview()

def delete_last_word(event=None):
  
    with open("output.txt", "r") as file:
        content = file.read()

   
    words = content.split()

  
    if words:
        words.pop()

       
        updated_content = " ".join(words)

        
        with open("output.txt", "w") as file:
            file.write(updated_content)

       
        update_preview()
    

open("output.txt", "w").close()


root = ctk.CTk()
root.title("SlowPaceNote")
root.geometry("1280x720")

root.bind("<Return>", add_newline)
root.bind("<Delete>", delete_last_word)
root.bind("<space>", print_space)
left_frame = ctk.CTkFrame(root, width=320, height=720)
left_frame.pack(side="left", fill="y")

left_button = ctk.CTkButton(left_frame, text="L", width=100, command=left_button_click)
left_button.pack(side="top")


for i in range(1, 7):
    number_button = ctk.CTkButton(left_frame, text=str(i), width=100, command=lambda i=i: number_button_click(i))
    number_button.pack(side="top")


over_button = ctk.CTkButton(left_frame, text="OVER (/)", width=100, command=print_slash)
over_button.pack(side="top")


tightens_button = ctk.CTkButton(left_frame, text="TIGHTENS (>)", width=100, command=print_tightens)
tightens_button.pack(side="top")


into_button = ctk.CTkButton(left_frame, text="INTO", width=100, command=print_into)
into_button.pack(side="top")


caution_button = ctk.CTkButton(left_frame, text="CAUTION (!)", width=100, command=print_caution)
caution_button.pack(side="top")


keep_button = ctk.CTkButton(left_frame, text="KEEP", width=100, command=print_keep)
keep_button.pack(side="top")


hpr_button = ctk.CTkButton(left_frame, text="HPR", width=100, command=print_hpr)
hpr_button.pack(side="top")


hpl_button = ctk.CTkButton(left_frame, text="HPL", width=100, command=print_hpl)
hpl_button.pack(side="top")

junction_button = ctk.CTkButton(left_frame, text="JUNCTION", width=100, command=print_junction)
junction_button.pack(side="top")

# Create right column buttons
right_frame = ctk.CTkFrame(root, width=320, height=720)
right_frame.pack(side="left", fill="y")


right_button = ctk.CTkButton(right_frame, text="R", width=100, command=right_button_click)
right_button.pack(side="top")


for i in range(1, 7):
    number_button = ctk.CTkButton(right_frame, text=str(i), width=100, command=lambda i=i: number_button_click(i))
    number_button.pack(side="top")


crest_button = ctk.CTkButton(right_frame, text="CREST (C)", width=100, command=print_crest)
crest_button.pack(side="top")

opens_button = ctk.CTkButton(right_frame, text="OPENS (<)", width=100, command=print_opens)
opens_button.pack(side="top")

space_button = ctk.CTkButton(right_frame, text="SPACE", width=100, command=print_space)
space_button.pack(side="top")


jump_button = ctk.CTkButton(right_frame, text="JUMP", width=100, command=print_jump)
jump_button.pack(side="top")


bump_button = ctk.CTkButton(right_frame, text="BUMP", width=100, command=print_bump)
bump_button.pack(side="top")


unseen_button = ctk.CTkButton(right_frame, text="UNSEEN", width=100, command=print_unseen)
unseen_button.pack(side="top")


zero_button = ctk.CTkButton(right_frame, text="0", width=100, command=print_zero)
zero_button.pack(side="top")


dc_button = ctk.CTkButton(right_frame, text="DC", width=100, command=print_dc)
dc_button.pack(side="top")


save_button = ctk.CTkButton(right_frame, text="Save", width=100, command=save_to_custom_file)
save_button.pack(side="bottom")


new_line_button = ctk.CTkButton(right_frame, text="New Line", width=100, command=add_newline)
new_line_button.pack(side="bottom")

delete_word_button = ctk.CTkButton(right_frame, text="Delete Last Word", width=100, command=delete_last_word)
delete_word_button.pack(side="bottom")


preview_label = ctk.CTkLabel(root,
anchor="nw",
justify="left",
wraplength=800,
text="Tip: Use Enter to skip to a new line, and Delete to go back!",
fg_color="black"

)
preview_label.place_configure(x=500, y=10, width=920, height=700)


root.mainloop()
