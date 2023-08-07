import os
import sys
import shutil
import requests
from zipfile import ZipFile
import getpass
import webbrowser
from tkinter import *
from tkinter import scrolledtext
from tkinter.filedialog import askdirectory
import customtkinter
from customtkinter import *
from PIL import Image, ImageTk
import os
from threading import Thread
import getpass
from pathlib import Path
import sys
import shutil
import requests
import psutil
import SarcLib
import libyaz0

def get_app_data_directory():
    username = getpass.getuser()
    aar_dir = f'C:\\Users\\{username}\\AppData\\Roaming\\totk-aar'
    gui_dir = f'C:\\Users\\{username}\\AppData\\Roaming\\totk-aar\\totk-aar-main'
    return aar_dir, gui_dir

def check_and_update_version(gui_dir):
    gui_path = os.path.join(gui_dir, 'GUI.py')
    if os.path.exists(gui_path):
        with open(gui_path, 'r') as file:
            for line in file:
                if line.startswith("tool_version"):
                    current_version = line.split('=')[1].strip().strip('"')
                    break
        # Download the GUI.py from the main branch on GitHub
        url = 'https://raw.githubusercontent.com/fayaz12g/totk-aar/main/GUI.py'
        response = requests.get(url)
        remote_version = None
        for line in response.text.splitlines():
            if line.startswith("tool_version"):
                remote_version = line.split('=')[1].strip().strip('"')
                break
        if remote_version and current_version < remote_version:
            return True
    return False

def update_app_data(gui_dir, progress_label):
    if os.path.exists(gui_dir):
        shutil.rmtree(gui_dir)

    # Download the contents of the GitHub repository
    print("Downloading the contents of the GitHub repository...")
    url = 'https://github.com/fayaz12g/totk-aar/archive/main.zip'
    response = requests.get(url)

    # Save the downloaded content as a zip file
    zip_file_path = os.path.join(aar_dir, 'totk-aar-main.zip')
    with open(zip_file_path, 'wb') as zip_file:
        zip_file.write(response.content)

    # Extract the zip file
    with ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(aar_dir)

    # Remove the downloaded zip file
    os.remove(zip_file_path)

# Create a Tkinter window to display the update progress
def show_update_progress():
    progress_window = customtkinter.Toplevel()
    progress_window.title("Updating...")
    progress_label = customtkinter.CTkLabel(progress_window, text="Updating the application data...")
    progress_label.pack()

    # Get the app data directory
    aar_dir, gui_dir = get_app_data_directory()

    # Check if the directory exists
    if not os.path.exists(aar_dir):
        print(f"Directory '{aar_dir}' does not exist. Creating the directory...")
        os.makedirs(aar_dir)

    # Check if an update is required
    if check_and_update_version(gui_dir):
        update_app_data(gui_dir, progress_label)
        progress_label.config(text="Update completed!")
        # Destroy the progress window after a few seconds
        progress_window.after(3000, progress_window.destroy)

    else:
        progress_label.config(text="No update needed.")
        # Destroy the progress window after a few seconds
        progress_window.after(3000, progress_window.destroy)

    # Add the directory to sys.path
    sys.path.append(gui_dir)

    # Now, you can import GUI
    import GUI

# Create the main Tkinter window
root = customtkinter.CTk()
root.title("Launcher")

# Get the screen's width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window's width and height
window_width = 500
window_height = 300

# Calculate the x and y coordinates for centering the window
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set the geometry of the window to be centered on the screen
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Automatically start the process
show_update_progress()

# Run the Tkinter main loop
root.mainloop()