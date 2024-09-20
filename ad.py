import tkinter as tk
from tkinter import filedialog
import shutil
import os

def select_and_copy_file(new_file_name):
    # Open file dialog to select a .png file
    file_path = filedialog.askopenfilename(title="Select a PNG File", filetypes=[("PNG files", "*.png")])
    
    if file_path:
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Define the new file path
        new_file_path = os.path.join(script_dir, new_file_name)
        
        # Copy the file to the new location
        shutil.copy(file_path, new_file_path)
        
        print(f"File copied to {new_file_path}")

# Create the main window
root = tk.Tk()
root.title("File Copier")

label1 = tk.Label(text="Pick your photos; maximumu of 3 Ads")
label1.pack()
label2 = tk.Label(text="Preferred Resolution is 1000 x 1000 | Portrait")
label2.pack()

# Create buttons to trigger the file selection and copying
button1 = tk.Button(root, text="Open File for First Advertisement", command=lambda: select_and_copy_file("adsample1.png"))
button1.pack(pady=10)

button2 = tk.Button(root, text="Open File for Second Advertisement", command=lambda: select_and_copy_file("adsample2.png"))
button2.pack(pady=10)

button3 = tk.Button(root, text="Open File for Third Advertisement", command=lambda: select_and_copy_file("adsample3.png"))
button3.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
