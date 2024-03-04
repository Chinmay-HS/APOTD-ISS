
import json
import tkinter as tk
from tkinter import ttk
import urllib.request
import time
import geocoder

def fetch_iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # Extract the ISS location
    location = result["iss_position"]
    lat = float(location['latitude'])
    lon = float(location['longitude'])

    # Output to the terminal
    print("\nLatitude: " + str(lat))
    print("Longitude: " + str(lon))

    # Update GUI labels
    latitude_label.config(text=f"Latitude: {lat}")
    longitude_label.config(text=f"Longitude: {lon}")

    # Update the ISS Location on the map
    x, y = lon_to_pixel(lon), lat_to_pixel(lat)
    canvas.coords(iss_icon, x - 15, y - 15)  # Adjust icon size if needed

    # Refresh``
    root.after(5000, fetch_iss_location)  # Call the function every 5000 milliseconds (5 seconds)

def lon_to_pixel(lon):
    return (lon + 180) * (canvas.winfo_width() / 360)

def lat_to_pixel(lat):
    return (90 - lat) * (canvas.winfo_height() / 180)

# Create main window
root = tk.Tk()
root.title("ISS Tracking with Tkinter")

# Create labels for Latitude and Longitude
latitude_label = ttk.Label(root, text="Latitude: ")
latitude_label.pack(pady=10)

longitude_label = ttk.Label(root, text="Longitude: ")
longitude_label.pack(pady=10)

# Setup the world map using Tkinter canvas
canvas = tk.Canvas(root, width=1280, height=720)
canvas.pack()

# Load the world map image
map_image_path = "C:\\Users\TIAT\Downloads\APOTD-ISS-main\APOTD-ISS-main\map2.gif"  # Replace with the actual path to your image file
map_image = tk.PhotoImage(file=map_image_path)
canvas.create_image(0, 0, anchor=tk.NW, image=map_image)

# Load the ISS icon
iss_icon_path = "C:\\Users\TIAT\Downloads\APOTD-ISS-main\APOTD-ISS-main\iss_icon2.gif"  # Replace with the actual path to your image file
iss_icon_image = tk.PhotoImage(file=iss_icon_path)
iss_icon = canvas.create_image(0, 0, anchor=tk.CENTER, image=iss_icon_image)

# Fetch ISS location initially and start the tracking
fetch_iss_location()

# Run the main loop
root.mainloop()
