import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from pprint import PrettyPrinter

pp = PrettyPrinter()
apiKey = 'Owwu0ar0RtvX84p0bjHW1r7nlzKvozGfdCpqx8yR'

def fetch_apod(date):
    URL_APOD = "https://api.nasa.gov/planetary/apod"
    params = {
        'api_key': apiKey,
        'date': date,
        'hd': 'True'
    }
    response = requests.get(URL_APOD, params=params).json()
    return response

def display_image_from_url(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        image_data = Image.open(BytesIO(response.content))
        image_data.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image_data)

        image_label = ttk.Label(root, image=photo)
        image_label.image = photo  # Keep a reference to the image object
        image_label.grid(row=5, column=0, padx=10, pady=10, columnspan=3)

        root.mainloop()
    else:

def fetch_and_display_apod():
    selected_date = date_var.get()
    apod_response = fetch_apod(selected_date)

    if 'url' in apod_response and apod_response['media_type'] == 'image':
        image_url = apod_response['url']
        url_text.config(state=tk.NORMAL)
        url_text.delete('1.0', tk.END)
        url_text.insert(tk.END, f"Image URL: {image_url}")
        url_text.config(state=tk.DISABLED)

        # Display additional information in a cool GUI
        display_info(apod_response)
    else:
        print("Invalid APOD response or not an image type.")

def display_info(apod_response):
    info_frame = ttk.Frame(root, padding=(10, 10, 10, 10))
    info_frame.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="WENS")

    title_label = ttk.Label(info_frame, text="ASTRONOMY PICTURE OF THE DAY", font=('DM Sans', 16, 'bold'))
    title_label.grid(row=0, column=0, padx=10, pady=5, sticky="W")

    group_label = ttk.Label(info_frame, text="Microproject Group 26", font=('DM Sans', 12, 'italic'))
    group_label.grid(row=1, column=0, padx=10, pady=5, sticky="W")

    title_label = ttk.Label(info_frame, text=f"Title: {apod_response['title']}", font=('DM Sans', 14, 'bold'))
    title_label.grid(row=2, column=0, padx=10, pady=5, sticky="W")

    explanation_text = tk.Text(info_frame, wrap=tk.WORD, width=50, height=5, font=('DM Sans', 12))
    explanation_text.grid(row=3, column=0, padx=10, pady=5, sticky="W")
    explanation_text.insert(tk.END, f"Explanation: {apod_response['explanation']}")
    explanation_text.config(state=tk.DISABLED)

    copyright_label = ttk.Label(info_frame, text=f"Copyright: {apod_response['copyright']}", font=('DM Sans', 10))
    copyright_label.grid(row=4, column=0, padx=10, pady=5, sticky="W")

    # Button to display image from the URL
    display_button = ttk.Button(info_frame, text="Display Image", command=lambda: display_image_from_url(apod_response['url']))
    display_button.grid(row=5, column=0, padx=10, pady=10, sticky="W")

# Create the main window
root = tk.Tk()
root.title("NASA APOD Viewer")
root.geometry("800x600")  # Set the initial size of the window

# Center the window on the screen
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry("+{}+{}".format(position_right, position_down))

# Title Label
title_label = ttk.Label(root, text="ASTRONOMY PICTURE OF THE DAY", font=('DM Sans', 16, 'bold'))
title_label.grid(row=0, column=0, padx=10, pady=5, columnspan=3, sticky="W")

group_label = ttk.Label(root, text="Microproject Group 26", font=('DM Sans', 12, 'italic'))
group_label.grid(row=1, column=0, padx=10, pady=5, columnspan=3, sticky="W")

# Date Entry
date_var = tk.StringVar()
date_var.set('2020-01-22')  # Initial date, change as needed
date_label = ttk.Label(root, text="Enter Date (YYYY-MM-DD):")
date_label.grid(row=2, column=0, padx=10, pady=10, sticky="E")
date_entry = ttk.Entry(root, textvariable=date_var, width=15)
date_entry.grid(row=2, column=1, padx=10, pady=10, sticky="W")

# Fetch APOD Button
fetch_button = ttk.Button(root, text="Fetch APOD", command=fetch_and_display_apod)
fetch_button.grid(row=2, column=2, padx=10, pady=10)

# Image URL Text
url_text = tk.Text(root, wrap=tk.WORD, width=50, height=3, state=tk.DISABLED)
url_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Run the main loop
root.mainloop()