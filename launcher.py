import os
import sys
import shutil
import requests
from zipfile import ZipFile
from threading import Thread
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

#######################
## Helper Functions ###
#######################

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
        print("pip has been successfully installed.")
    except subprocess.CalledProcessError:
        print("Failed to install pip. Please install it manually.")


# Function to check and install dependencies
def check_and_install_dependencies():
    if not is_pip_installed():
        print("pip is not installed. Attempting to install pip...")
        install_pip()
        
    for dependency in dependencies:
        try:
            __import__(dependency)
            print(f"{dependency} is already installed.")
        except ImportError:
            print(f"{dependency} is not installed. Attempting to install...")
            install_dependency(dependency)

# Function to install a specific dependency using pip
def install_dependency(dependency):
    try:
        subprocess.run(["python", "-m", "pip", "install", dependency], check=True)
        print(f"{dependency} has been successfully installed.")
    except subprocess.CalledProcessError:
        print(f"Failed to install {dependency}. Please install it manually.")

# Create a Tkinter window to display the update progress
def show_update_progress():
    global aar_dir

    # Check if the directory exists
    if not os.path.exists(aar_dir):
        print(f"Directory '{aar_dir}' does not exist. Creating the directory...")
        os.makedirs(aar_dir)



#######################
#### Create Window ####
#######################

tool_version = "6.0"

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

    
show_update_progress()

root = customtkinter.CTk()
root.title(f"Any Aspect Ratio Launcher {tool_version}")
root.geometry("400x450")

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
            print("New version available!")
            return True
        else:
            return False
    else:
        return True
    
def update_app_data(gui_dir, aar_dir, tool_name):
    if os.path.exists(gui_dir):
        shutil.rmtree(gui_dir)

    # Download the contents of the GitHub repository
    print("Downloading the contents of the GitHub repository...")
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


titlebar = customtkinter.CTkLabel(text="Select a Game, then Click the Launch AAR Button:", master = root)
titlebar.pack(pady=50)

# Update the button's state when a tool is selected
def update_button_state(choice):
    if choice != "Select a Game":
        launch_button.configure(state=tkinter.NORMAL)
    else:
        launch_button.configure(state=tkinter.DISABLED)

# Create a dropdown menu
combo = customtkinter.CTkComboBox(root, state="readonly", values = [tool["2"] for tool in aar_tools], width = 250, hover=True, command = update_button_state)
combo['values'] = [tool["2"] for tool in aar_tools]
combo.pack(pady=20)

combo.set("Select a Game")

# Create a dictionary that maps full tool names to short tool names
tool_name_map = {tool["2"]: tool["1"] for tool in aar_tools}

# Create a button to launch the selected tool
launch_button = customtkinter.CTkButton(root, text="Launch AAR", state=tkinter.DISABLED, hover=True, text_color="white")
launch_button.pack(pady=20)

def newthread(aar_dir, tool_name):
    t = Thread(target=update_app_data(gui_dirs[tool_name], aar_dir, tool_name))
    t.start() 

def launch_tool(event):
    full_tool_name = combo.get()
    if full_tool_name != "Select a Game":
        tool_name = tool_name_map[full_tool_name]
        update_notification = customtkinter.CTkLabel(text="Fetching contents, please wait...", master = root)
        update_notification.pack(pady=5)
        if check_and_update_version(gui_dirs[tool_name], tool_name):
            newthread(aar_dir, tool_name)
        gui_script = os.path.join(gui_dirs[tool_name], 'GUI.py')

        # Get the path to the current executable (the PyInstaller-built application)
        current_executable = sys.executable

        # Build the command to execute the other Python script
        launch_command = [current_executable, gui_script]

        # Launch Using Old Method
        sys.path.append(gui_dirs[tool_name])
        root.destroy() 
        # Use subprocess to launch the script
        try:
            import GUI
            # subprocess.run(launch_command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

launch_button.bind("<Button-1>", launch_tool)

def open_aar_folder():
    os.startfile(aar_dir)

open_folder_button = customtkinter.CTkButton(root, text="Open AAR Folder", command=open_aar_folder)
open_folder_button.pack(pady=20)

# Automatically start the process
show_update_progress()

root.mainloop()