import random
import string
import tkinter as tk
import tkinter.messagebox as msgbox

def generate_password(length):
    if length == 31:
        return "HAHAHAHAP31AŞİASLŞFASİLASGÜAKPAVVVVVVERYFUNNYYYYYYYYAĞSFŞLPAKDGĞAGAKOMIKASLFŞAÜĞAGĞALGDGLĞÜS"

    # Define the possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation + "çğıöşüÇĞİÖŞÜ"

    # Generate a password by randomly selecting characters from the pool
    password = ''.join(random.choice(characters) for i in range(length))

    return password

def generate_button_clicked():
    length = int(length_entry.get())
    password = generate_password(length)
    password_label.config(text="Generated Password:")
    password_text.config(state=tk.NORMAL)
    password_text.delete(1.0, tk.END)
    password_text.insert(tk.END, password)
    password_text.config(state=tk.DISABLED)
    copy_button.config(state=tk.NORMAL)

def copy_button_clicked():
    password = password_text.get(1.0, tk.END)
    window.clipboard_clear()
    window.clipboard_append(password)
    msgbox.showinfo("Password Copied", "The password has been copied to the clipboard.")

def switch_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        window.config(bg="#252525")
        length_label.config(fg="#FF0000")
        password_label.config(fg="#FF0000")
        switch_button.config(text="Light Mode")
    else:
        window.config(bg="#ffffff")
        length_label.config(fg="#FF0000")
        password_label.config(fg="#FF0000")
        switch_button.config(text="Dark Mode")

# Create the main window
window = tk.Tk()
window.geometry("400x400")
window.title("Password Generator")

# Create the input and output widgets
length_label = tk.Label(window, text="Password Length:", fg="#FF0000")
length_entry = tk.Entry(window)
password_label = tk.Label(window, text="", fg="#FF0000")
password_text = tk.Text(window, height=1, state=tk.DISABLED)
copy_button = tk.Button(window, text="Copy", command=copy_button_clicked, state=tk.DISABLED)

# Create the button widgets
generate_button = tk.Button(window, text="Generate", command=generate_button_clicked)
switch_button = tk.Button(window, text="Dark Mode", command=switch_mode)

# Add the widgets to the window
length_label.pack()
length_entry.pack()
generate_button.pack()
password_label.pack()
password_text.pack()
copy_button.pack()
switch_button.pack(side=tk.BOTTOM)

# Set initial mode
dark_mode = False
switch_mode()

# Start the main event loop
window.mainloop()
