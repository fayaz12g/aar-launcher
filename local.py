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




#######################
#### Create Window ####
#######################

tool_version = "2.2"

username = getpass.getuser()
aar_dir = f'C:\\Users\\{username}\\Documents\\GitHub'
    
totk_gui_dir = f'C:\\Users\\{username}\\Documents\\GitHub\\totk-aar'
smo_gui_dir = f'C:\\Users\\{username}\\Documents\\GitHub\\smo-aar'
sm3dw_gui_dir = f'C:\\Users\\{username}\\Documents\\GitHub\\sm3dw-aar'
mk8d_gui_dir = f'C:\\Users\\{username}\\Documents\\GitHub\\mk8d-aar'
mm2_gui_dir = f'C:\\Users\\{username}\\Documents\\GitHub\\mm2-aar'
ssbu_gui_dir = f'C:\\Users\\{username}\\Documents\\GitHub\\ssbu-aar'
mvdk_gui_dir = f'C:\\Users\\{username}\\Documents\\GitHub\\mvdk-aar'

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


def launch_totk():
    
    root.destroy()
    # Specify the path to the Python script you want to launch
    totk_gui = os.path.join(totk_gui_dir, 'GUI.py')

    # Get the path to the current executable (the PyInstaller-built application)
    current_executable = sys.executable

    # Build the command to execute the other Python script
    launch_totk_command = ["python", totk_gui]

    # Launch Using Old Method
    sys.path.append(totk_gui_dir)

    # Use subprocess to launch the script
    try:
        import GUI
        # subprocess.run(launch_totk_command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except subprocess.CalledProcessError as e:
        update_text(f"Error: {e}")

        
def launch_mvdk():
    
    root.destroy()
    # Specify the path to the Python script you want to launch
    mvdk_gui = os.path.join(mvdk_gui_dir, 'GUI.py')

    # Get the path to the current executable (the PyInstaller-built application)
    current_executable = sys.executable

    # Build the command to execute the other Python script
    launch_mvdk_command = ["python", mvdk_gui]

    # Launch Using Old Method
    sys.path.append(mvdk_gui_dir)

    # Use subprocess to launch the script
    try:
        import GUI
        # subprocess.run(launch_mvdk_command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except subprocess.CalledProcessError as e:
        update_text(f"Error: {e}")


def launch_mk8d():
    
    root.destroy()
    # Specify the path to the Python script you want to launch
    mk8d_gui = os.path.join(mk8d_gui_dir, 'GUI.py')

    # Get the path to the current executable (the PyInstaller-built application)
    current_executable = sys.executable

    # Build the command to execute the other Python script
    launch_mk8d_command = ["python", mk8d_gui]
   
    # Launch Using Old Method
    sys.path.append(mk8d_gui_dir)

    # Use subprocess to launch the script
    try:
        import GUI
        # subprocess.run(launch_mk8d_command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except subprocess.CalledProcessError as e:
        update_text(f"Error: {e}")
    


def launch_smo():

    root.destroy()
    # Specify the path to the Python script you want to launch
    smo_gui = os.path.join(smo_gui_dir, 'GUI.py')
    # Get the path to the current executable (the PyInstaller-built application)
    current_executable = sys.executable

    # Build the command to execute the other Python script
    launch_smo_command = ["python", smo_gui]
   
    # Launch Using Old Method
    sys.path.append(smo_gui_dir)

    # Use subprocess to launch the script
    try:
        import GUI
        # subprocess.run(launch_smo_command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except subprocess.CalledProcessError as e:
        update_text(f"Error: {e}")

def launch_sm3dw():
    root.destroy()
    
    # Specify the path to the Python script you want to launch
    sm3dw_gui = os.path.join(sm3dw_gui_dir, 'GUI.py')
    # Get the path to the current executable (the PyInstaller-built application)
    current_executable = sys.executable

    # Build the command to execute the other Python script
    launch_sm3dw_command = ["python", sm3dw_gui]
   
    # Launch Using Old Method
    sys.path.append(sm3dw_gui_dir)

    # Use subprocess to launch the script
    try:
        import GUI
        # subprocess.run(launch_sm3dw_command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except subprocess.CalledProcessError as e:
        update_text(f"Error: {e}")

def launch_mm2():
    root.destroy()
    
    # Specify the path to the Python script you want to launch
    mm2_gui = os.path.join(mm2_gui_dir, 'GUI.py')
    # Get the path to the current executable (the PyInstaller-built application)
    current_executable = sys.executable

    # Build the command to execute the other Python script
    launch_mm2_command = ["python", mm2_gui]
   
    # Launch Using Old Method
    sys.path.append(mm2_gui_dir)

    # Use subprocess to launch the script
    try:
        import GUI
        # subprocess.run(launch_mm2_command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except subprocess.CalledProcessError as e:
        update_text(f"Error: {e}")

def launch_ssbu():
    root.destroy()
    
    # Specify the path to the Python script you want to launch
    ssbu_gui = os.path.join(ssbu_gui_dir, 'GUI.py')
    # Get the path to the current executable (the PyInstaller-built application)
    current_executable = sys.executable

    # Build the command to execute the other Python script
    launch_ssbu_command = ["python", ssbu_gui]
   
    # Launch Using Old Method
    sys.path.append(ssbu_gui_dir)

    # Use subprocess to launch the script
    try:
        sys.path.append(ssbu_gui)
        sys.path.append(ssbu_gui_dir)
        import GUI
        # subprocess.run(launch_ssbu_command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except subprocess.CalledProcessError as e:
        update_text(f"Error: {e}")


def update_text(new_text):
    text_box.config(state="normal")  # Set state to normal to enable editing
    text_box.delete(1.0, "end")  # Clear existing text
    text_box.insert("end", new_text)  # Insert new text
    text_box.config(state="disabled")  # Set state to disabled to make it read-only


# Automatically start the process
show_update_progress()

mario_button = customtkinter.CTkButton(master=root, text="AAR for Mario Odyssey", command=launch_smo)
mario_button.pack(pady = 20)

totk_button = customtkinter.CTkButton(master=root, text="AAR for Tears of the Kingdom", command=launch_totk)
totk_button.pack(pady = 20)

mk8d_button = customtkinter.CTkButton(master=root, text="AAR for MarioKart 8 Deluxe", command=launch_mk8d)
mk8d_button.pack(pady = 20)

sm3dw_button = customtkinter.CTkButton(master=root, text="AAR for Super Mario 3D World + Bowser's Fury", command=launch_sm3dw)
sm3dw_button.pack(pady = 20)

mm2_button = customtkinter.CTkButton(master=root, text="AAR for Super Mario Maker 2", command=launch_mm2)
mm2_button.pack(pady = 20)

ssbu_button = customtkinter.CTkButton(master=root, text="AAR for Super Smash Brothers Ultimate", command=launch_ssbu)
ssbu_button.pack(pady = 20)

ssbu_button = customtkinter.CTkButton(master=root, text="AAR for Mario VS Donkey Kong", command=launch_mvdk)
ssbu_button.pack(pady = 20)

text_box = scrolledtext.ScrolledText(master=root, wrap="word", height=30, width=70)
text_box.pack(pady=20)

default_text = "Click the game you want to use the tool for!"
update_text(default_text)

root.mainloop()