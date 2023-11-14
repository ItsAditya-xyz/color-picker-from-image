<<<<<<< HEAD
import cv2
import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab
from tkinter import filedialog
import numpy as np
import pyperclip

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def update_color_table(red, green, blue):
    hex_color = rgb_to_hex((red, green, blue))
    color_table.insert("", "end", values=(red, green, blue, hex_color), tags=(hex_color,))
    color_table.tag_configure(hex_color, background=hex_color)
    pyperclip.copy(hex_color)
    
def load_image():
    img = np.array([])  # Initialize img as an empty array
    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path)
        cv2.imshow("Image", img)
        cv2.setMouseCallback("Image", click_event, img)

def take_screenshot():
    screenshot = ImageGrab.grab()
    screenshot_np = np.array(screenshot)
    screenshot_cv2 = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("Image", screenshot_cv2)
    cv2.setMouseCallback("Image", click_event, screenshot_cv2)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if param is not None:
            blue = param[y, x, 0]
            green = param[y, x, 1]
            red = param[y, x, 2]
            font = cv2.FONT_HERSHEY_SIMPLEX
            strXY = '#' + str(rgb_to_hex((red, green, blue)))
            cv2.putText(param, strXY, (x, y), font, 1, (0, 0, 0), 2)
            cv2.imshow('Image', param)
            update_color_table(red, green, blue)

def delete_all_records():
    all_items = color_table.get_children()
    for item in all_items:
        color_table.delete(item)


def delete_selected():
    selected_item = color_table.selection()
    if selected_item:
        color_table.delete(selected_item)

def copy_selected():
    selected_item = color_table.selection()
    if selected_item:
        item_values = color_table.item(selected_item, 'values')
        hex_value = item_values[3]  # Assuming the HEX value is in the fourth column
        pyperclip.copy(hex_value)




# Create a Tkinter window
root = tk.Tk()
root.title("OpenCV and Tkinter Color Picker")
root.geometry("800x400")

# Create a label for the title
title_label = tk.Label(root, text="Color Picker App", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Create buttons to load an image and take a screenshot
load_button = ttk.Button(root, text="Load Image", command=load_image)
load_button.pack(pady=5)

screenshot_button = ttk.Button(root, text="Take Screenshot", command=take_screenshot)
screenshot_button.pack(pady=5)

# Create a color table using Treeview
columns = ("Red", "Green", "Blue", "Hex")
color_table = ttk.Treeview(root, columns=columns, show="headings", height=10)

# Set column headings
for col in columns:
    color_table.heading(col, text=col)

color_table.pack(pady=10)


delete_button = ttk.Button(root, text="Delete Selected", command=delete_selected)
delete_button.pack(side="left", padx=5, pady=5)

copy_button = ttk.Button(root, text="Copy HEX to Clipboard", command=copy_selected)
copy_button.pack(side="left", padx=5, pady=5)

exit_button = ttk.Button(root, text="Exit App", command=root.destroy)
exit_button.pack(side="right", padx=5, pady=5)

delete_all_button = ttk.Button(root, text="Delete All Records", command=delete_all_records)
delete_all_button.pack(side="left", padx=5, pady=5)


root.mainloop()
=======
#!/usr/bin/env python3

import sys
import numpy as np
from cv2 import cv2
import pyperclip

if len(sys.argv) == 1:
	picture = 'Just Slide.png'
else:
	picture = sys.argv[1]
img = cv2.imread(picture)

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb	# Converts RGB to Hex. RGB is passed as a tuple.

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue= img[y, x, 0]  
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = '#' + str(rgb_to_hex((red,blue,green)))  
        pyperclip.copy(strXY)
        cv2.putText(img, strXY, (x, y), font, 1, (0, 0, 0), 2)
        cv2.imshow(picture, img)

cv2.imshow(picture, img)
cv2.setMouseCallback(picture, click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
>>>>>>> e588fd2393a1409b343b36f1f9eb4a3e6f132ab9
