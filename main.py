import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# Function to open APOD module
def open_apod():
    os.system(f"python3 /Volumes/Volume/Balthasar/CO6I/PWP_22616/Stuff/Microproject/apod.py")

# Function to open ISS tracking module
def open_iss():
    os.system(f"python3 /Volumes/Volume/Balthasar/CO6I/PWP_22616/Stuff/Microproject/iss.py")

# Create main window
root = tk.Tk()
root.title("Group 26 PWP Microproject")
root.geometry("900x600")

# Load and display background image
bg_image_path = "/Volumes/Volume/Balthasar/CO6I/PWP_22616/Stuff/Microproject/bgimage.jpg"  # Replace with your image path
if os.path.exists(bg_image_path):
    background_image = Image.open(bg_image_path)
    background_photo = ImageTk.PhotoImage(background_image)

    background_label = ttk.Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    # Bring to front
    background_label.lift()

# Title labels
apod_title_label = ttk.Label(root, text="ASTRONOMY PICTURE OF THE DAY", font=('DM Sans', 24, 'bold'))
apod_title_label.pack(pady=20)

iss_title_label = ttk.Label(root, text="ISS TRACKING MICROPROJECT", font=('DM Sans', 24, 'bold'))
iss_title_label.pack(pady=20)

# APOD Button
apod_button = ttk.Button(root, text="Go to APOD Module", command=open_apod, style='RoundedButton.TButton')
apod_button.pack(pady=20)

# ISS Tracking Button
iss_button = ttk.Button(root, text="Go to ISS Tracking Module", command=open_iss, style='RoundedButton.TButton')
iss_button.pack(pady=20)

# Style for rounded buttons
style = ttk.Style()
style.configure('RoundedButton.TButton', borderwidth=0, relief="flat", background="#3186FF", font=('DM Sans', 14, 'bold'))

# Run the main loop
root.mainloop()
