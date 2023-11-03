import random
import string
from tkinter import *
import pyperclip
root = Tk()
root.configure(bg="#040D12")
root.geometry("200x200")
root.maxsize(400, 350)
root.minsize(400, 350)
root.title("RANDOM PASSWORD GENERATOR")
output_pass = StringVar()
all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]
def randPassGen():
  password = ""
  for y in range(pass_len.get()):
    char_type = random.choice(all_combi)
    password += random.choice(char_type)
  output_pass.set(password)
def copyPass():
  pyperclip.copy(output_pass.get())
pass_head = Label(root, text="Set Your Password Length: ", font=("Times New Roman", 15), fg="white", bg="#040D12")
pass_head.pack(pady=10) 
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=24, font=("Times New Roman",15), bg="#5C8374", fg="white")
length.pack()
Button(root, command=randPassGen, text="Generate", font=("Times New Roman",12), bg="#183D3D", fg="#93B1A6", activebackground="black", padx=5, pady=5).pack(pady=20) 
pass_label = Label(root, text="Here is Your Password:", font=("Times New Roman", 15), fg="white", bg="#040D12")
pass_label.pack(pady="30 10")
Entry(root, textvariable=output_pass, width=24, font=("Times New Roman",12), bg="#5C8374", fg="white").pack()
Button(root, text="Copy to Clipboard", command=copyPass, font=("Times New Roman",12), bg="#183D3D", fg="#93B1A6", activebackground="black", padx=5, pady=5).pack(pady=20)

root.mainloop()
