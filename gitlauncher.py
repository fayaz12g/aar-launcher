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

tool_version = "local git version"

username = getpass.getuser()
aar_dir = f'C:\\Users\\{username}\\AppData\\Roaming\\AnyAspectRatio'
    
totk_gui_dir = f'C:\\Users\\{username}\\Documents\\GithHub\\totk-aar'
smo_gui_dir = f'C:\\Users\\{username}\\Documents\\GithHub\\smo-aar'
mk8d_gui_dir = f'C:\\Users\\{username}\\Documents\\GithHub\\mk8d-aar'


root = customtkinter.CTk()
root.title(f"Any Aspect Ratio Launcher {tool_version}")
root.geometry("450x600")

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


def update_text(new_text):
    text_box.config(state="normal")  # Set state to normal to enable editing
    text_box.delete(1.0, "end")  # Clear existing text
    text_box.insert("end", new_text)  # Insert new text
    text_box.config(state="disabled")  # Set state to disabled to make it read-only


# Automatically start the process
show_update_progress()

mario_button = customtkinter.CTkButton(master=root, text="AAR for Mario Odyssey", command=launch_smo)
mario_button.pack(pady = 50)

totk_button = customtkinter.CTkButton(master=root, text="AAR for Tears of the Kingdom", command=launch_totk)
totk_button.pack(pady = 50)

mk8d_button = customtkinter.CTkButton(master=root, text="AAR for MarioKart 8 Deluxe", command=launch_mk8d)
mk8d_button.pack(pady = 50)

text_box = scrolledtext.ScrolledText(master=root, wrap="word", height=30, width=70)
text_box.pack(pady=20)

default_text = "Click the game you want to use the tool for!"
update_text(default_text)

root.mainloop()