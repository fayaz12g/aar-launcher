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
from keystone import *
import pyautogui
import zstandard
import tkinter as tk
from tkinter import ttk

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

#######################
#### Create Window ####
#######################

tool_version = "6.7"

username = getpass.getuser()
aar_dir = f'C:\\Users\\{username}\\Documents\\GitHub'

aar_tools = [
    {'1': 'home', '2': 'Home Menu'},
    {'1': 'totk', '2': 'Tears of the Kingdom'},
    {'1': 'botw', '2': 'Breath of the Wild'},
    {'1': 'smo', '2': 'Super Mario Odyssey'},
    {'1': 'sm3dw', '2': 'Super Mario 3D World'},
    {'1': 'mk8d', '2': 'MarioKart 8 Deluxe'},
    {'1': 'mm2', '2': 'Super Mario Maker 2'},
    {'1': 'ssbu', '2': 'Super Smash Brothers Ultimate'},
    {'1': 'mvdk', '2': 'Mario vs. Donkey Kong'},
    {'1': '12switch', '2': '1-2 Switch'},
    {'1': 'splatoon3', '2': 'Splatoon 3'},
    {'1': 'splatoon2', '2': 'Splatoon 2'},
    {'1': 'ppst', '2': 'Princess Peach: Showtime!'},
    {'1': 'nss', '2': 'Nintendo Switch Sports'},
    {'1': 'ttyd', '2': 'Paper Mario: The Thousand Year Door'},
    {'1': 'pmtok', '2': 'Paper Mario: The Origami King'}
]

customtkinter.deactivate_automatic_dpi_awareness()

gui_dirs = {}

for tool in aar_tools:
    gui_dirs[tool['1']] = f'C:\\Users\\{username}\\Documents\\GitHub\\{tool["1"]}-aar'

# Create a Tkinter window to display the update progress
def show_update_progress():
    global aar_dir

    # Check if the directory exists
    if not os.path.exists(aar_dir):
        print(f"Directory '{aar_dir}' does not exist. Creating the directory...")
        os.makedirs(aar_dir)

root = customtkinter.CTk()
root.title(f"Any Aspect Ratio Local Launcher {tool_version}")
root.geometry("400x450")

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")  
windowtitle = customtkinter.CTkLabel(master=root, font=(CTkFont, 20), text="Any Aspect Ratio Launcher {tool_version}")

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

def launch_tool(event):
    full_tool_name = combo.get()
    update_notification = customtkinter.CTkLabel(text="Fetching contents, please wait...", master = root)
    update_notification.pack(pady=5)
    if full_tool_name != "Select a Game":
        tool_name = tool_name_map[full_tool_name]
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