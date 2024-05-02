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
import subprocess
import sys
import os
import time
import packaging
import requests
import tkinter
import customtkinter
import psutil
import PIL
import certifi
import idna
import charset_normalizer
import darkdetect
import libyaz0
import urllib3
import zstandard
from keystone import *
import pyautogui




#######################
#### Create Window ####
#######################

tool_version = "5.7"

username = getpass.getuser()
aar_dir = f'C:\\Users\\{username}\\AppData\\Roaming\\AnyAspectRatio'
    
aar_tools = [
    {'1': 'totk', '2': 'Tears of the Kingdom'},
    {'1': 'smo', '2': 'Super Mario Odyssey'},
    {'1': 'sm3dw', '2': 'Super Mario 3D World'},
    {'1': 'mk8d', '2': 'MarioKart 8 Deluxe'},
    {'1': 'mm2', '2': 'Super Mario Maker 2'},
    {'1': 'ssbu', '2': 'Super Smash Brothers Ultimate'},
    {'1': 'mvdk', '2': 'Mario vs. Donkey Kong'},
    {'1': '12switch', '2': '1-2 Switch'},
    {'1': 'splatoon3', '2': 'Splatoon 3'},
    {'1': 'splatoon2', '2': 'Splatoon 2'},
    {'1': 'pmtok', '2': 'Paper Mario: The Origami King'}
]

gui_dirs = {}

for tool in aar_tools:
    gui_dirs[tool['1']] = f'C:\\Users\\{username}\\AppData\\Roaming\\AnyAspectRatio\\{tool["1"]}-aar-main'

dependencies = [
    "packaging",
    "requests",
    "tkinter",
    "customtkinter",
    "sarclib",
    "psutil",
    "pillow",
    "keystone-engine",
    "certifi",
    "idna",
    "charset_normalizer",
    "darkdetect",
    "libyaz0",
    "urllib3",
    "zstandard",
    "pyautogui",
]

def update_text(new_text):
    text_box.config(state="normal")  # Set state to normal to enable editing
    text_box.delete(1.0, "end")  # Clear existing text
    text_box.insert("end", new_text)  # Insert new text
    text_box.config(state="disabled")  # Set state to disabled to make it read-only
    
def is_pip_installed():
    try:
        subprocess.run(["pip", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

# Function to install pip
def install_pip():
    try:
        subprocess.run(["python", "-m", "ensurepip", "--default-pip"], check=True)
        update_text("pip has been successfully installed.")
    except subprocess.CalledProcessError:
        update_text("Failed to install pip. Please install it manually.")


# Function to check and install dependencies
def check_and_install_dependencies():
    if not is_pip_installed():
        update_text("pip is not installed. Attempting to install pip...")
        install_pip()
        
    for dependency in dependencies:
        try:
            __import__(dependency)
            update_text(f"{dependency} is already installed.")
        except ImportError:
            update_text(f"{dependency} is not installed. Attempting to install...")
            install_dependency(dependency)

# Function to install a specific dependency using pip
def install_dependency(dependency):
    try:
        subprocess.run(["python", "-m", "pip", "install", dependency], check=True)
        update_text(f"{dependency} has been successfully installed.")
    except subprocess.CalledProcessError:
        update_text(f"Failed to install {dependency}. Please install it manually.")

# Create a Tkinter window to display the update progress
def show_update_progress():
    global aar_dir

    # Check if the directory exists
    if not os.path.exists(aar_dir):
        update_text(f"Directory '{aar_dir}' does not exist. Creating the directory...")
        os.makedirs(aar_dir)


show_update_progress()

root = customtkinter.CTk()
root.title(f"Any Aspect Ratio Launcher {tool_version}")
root.geometry("450x800")

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")  
windowtitle = customtkinter.CTkLabel(master=root, font=(CTkFont, 20), text="Any Aspect Ratio Launcher {tool_version}")


def check_and_update_version(gui_dir, tool_name):
    # check_and_install_dependencies()
    gui_path = os.path.join(gui_dir, 'GUI.py')
    if os.path.exists(gui_dir):
        with open(gui_path, 'r') as file:
            for line in file:
                if line.startswith("tool_version"):
                    current_version = line.split('=')[1].strip().strip('"')
                    break
        # Download the GUI.py from the main branch on GitHub
        url = f'https://raw.githubusercontent.com/fayaz12g/{tool_name}-aar/main/GUI.py'
        response = requests.get(url)
        remote_version = None
        for line in response.text.splitlines():
            if line.startswith("tool_version"):
                remote_version = line.split('=')[1].strip().strip('"')
                break
        if remote_version and current_version < remote_version:
            print("New version available!")
            update_text("New version available!")
            return True
        else:
            return False
    else:
        return True
    
def update_app_data(gui_dir, aar_dir, tool_name):
    if os.path.exists(gui_dir):
        shutil.rmtree(gui_dir)

    # Download the contents of the GitHub repository
    update_text("Downloading the contents of the GitHub repository...")
    url = f'https://github.com/fayaz12g/{tool_name}-aar/archive/main.zip'
    response = requests.get(url)

    # Save the downloaded content as a zip file
    zip_file_path = os.path.join(aar_dir, f'{tool_name}-aar-main.zip')
    with open(zip_file_path, 'wb') as zip_file:
        zip_file.write(response.content)

    # Extract the zip file
    with ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(aar_dir)

    # Remove the downloaded zip file
    os.remove(zip_file_path)


def launch_tool(tool_name):
    
    if check_and_update_version(gui_dirs[tool_name], tool_name):
        update_app_data(gui_dirs[tool_name], aar_dir, tool_name)

    root.destroy()  # Assuming `root` is defined elsewhere in your code
    # Specify the path to the Python script you want to launch
    gui_script = os.path.join(gui_dirs[tool_name], 'GUI.py')

    # Get the path to the current executable (the PyInstaller-built application)
    current_executable = sys.executable

    # Build the command to execute the other Python script
    launch_command = [current_executable, gui_script]

    # Launch Using Old Method
    sys.path.append(gui_dirs[tool_name])

    # Use subprocess to launch the script
    try:
        import GUI
        # subprocess.run(launch_command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except subprocess.CalledProcessError as e:
        update_text(f"Error: {e}")

def update_text(new_text):
    text_box.config(state="normal")  # Set state to normal to enable editing
    text_box.delete(1.0, "end")  # Clear existing text
    text_box.insert("end", new_text)  # Insert new text
    text_box.config(state="disabled")  # Set state to disabled to make it read-only


# Automatically start the process
show_update_progress()

for tool in aar_tools:
    button = customtkinter.CTkButton(master=root, text=f"AAR for {tool["2"]}", command=lambda t=tool["1"]: launch_tool(t))
    button.pack(pady=20)


text_box = scrolledtext.ScrolledText(master=root, wrap="word", height=30, width=70)
text_box.pack(pady=20)

default_text = "Click the game you want to use the tool for!"
update_text(default_text)

root.mainloop()