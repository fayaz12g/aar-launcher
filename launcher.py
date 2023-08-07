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

def update_app_data(gui_dir):
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

# Get the app data directory
aar_dir, gui_dir = get_app_data_directory()

# Check if the directory exists
if not os.path.exists(aar_dir):
    print(f"Directory '{aar_dir}' does not exist. Creating the directory...")
    os.makedirs(aar_dir)

# Check if an update is required
if check_and_update_version(gui_dir):
    print("Updating the application data...")
    update_app_data(gui_dir)

# Add the directory to sys.path
sys.path.append(gui_dir)

# Now, you can import GUI
import GUI