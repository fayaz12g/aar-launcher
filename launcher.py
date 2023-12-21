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
import subprocess
import sys
import os




#######################
#### Create Window ####
#######################

tool_version = "2.0"

username = getpass.getuser()
aar_dir = f'C:\\Users\\{username}\\AppData\\Roaming\\AnyAspectRatio'
    
totk_gui_dir = f'C:\\Users\\{username}\\AppData\\Roaming\\AnyAspectRatio\\totk-aar-main'
smo_gui_dir = f'C:\\Users\\{username}\\AppData\\Roaming\\AnyAspectRatio\\smo-aar-main'
mk8d_gui_dir = f'C:\\Users\\{username}\\AppData\\Roaming\\AnyAspectRatio\\mk8d-aar-main'


# Create a Tkinter window to display the update progress
def show_update_progress():
    global aar_dir

    # Check if the directory exists
    if not os.path.exists(aar_dir):
        print(f"Directory '{aar_dir}' does not exist. Creating the directory...")
        os.makedirs(aar_dir)


show_update_progress()

root = customtkinter.CTk()
root.title(f"Any Aspect Ratio Launcher {tool_version}")
root.geometry("450x600")

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")  
windowtitle = customtkinter.CTkLabel(master=root, font=(CTkFont, 20), text="Any Aspect Ratio Launcher {tool_version}")



#TOTK Stuff

def check_and_update_version_totk(totk_gui_dir):
    gui_path = os.path.join(totk_gui_dir, 'GUI.py')
    if os.path.exists(totk_gui_dir):
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
            print("New version available!")
            return True
        else:
            return False
    else:
        return True
    
def update_app_data_totk(totk_gui_dir, aar_dir):
    if os.path.exists(totk_gui_dir):
        shutil.rmtree(totk_gui_dir)

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
    
#MK8D Stuff
    
def check_and_update_version_mk8d(totk_gui_dir):
    gui_path = os.path.join(totk_gui_dir, 'GUI.py')
    if os.path.exists(totk_gui_dir):
        with open(gui_path, 'r') as file:
            for line in file:
                if line.startswith("tool_version"):
                    current_version = line.split('=')[1].strip().strip('"')
                    break
        # Download the GUI.py from the main branch on GitHub
        url = 'https://raw.githubusercontent.com/fayaz12g/mk8d-aar/main/GUI.py'
        response = requests.get(url)
        remote_version = None
        for line in response.text.splitlines():
            if line.startswith("tool_version"):
                remote_version = line.split('=')[1].strip().strip('"')
                break
        if remote_version and current_version < remote_version:
            print("New version available!")
            return True
        else:
            return False
    else:
        return True
    
def update_app_data_mk8d(totk_gui_dir, aar_dir):
    if os.path.exists(totk_gui_dir):
        shutil.rmtree(totk_gui_dir)

    # Download the contents of the GitHub repository
    print("Downloading the contents of the GitHub repository...")
    url = 'https://github.com/fayaz12g/mk8d-aar/archive/main.zip'
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

#SMO Stuff
    
def check_and_update_version_smo(totk_gui_dir):
    gui_path = os.path.join(totk_gui_dir, 'GUI.py')
    if os.path.exists(totk_gui_dir):
        with open(gui_path, 'r') as file:
            for line in file:
                if line.startswith("tool_version"):
                    current_version = line.split('=')[1].strip().strip('"')
                    break
        # Download the GUI.py from the main branch on GitHub
        url = 'https://raw.githubusercontent.com/fayaz12g/smo-aar/main/GUI.py'
        response = requests.get(url)
        remote_version = None
        for line in response.text.splitlines():
            if line.startswith("tool_version"):
                remote_version = line.split('=')[1].strip().strip('"')
                break
        if remote_version and current_version < remote_version:
            print("New version available!")
            return True
        else:
            return False
    else:
        return True
    
def update_app_data_smo(totk_gui_dir, aar_dir):
    if os.path.exists(totk_gui_dir):
        shutil.rmtree(totk_gui_dir)

    # Download the contents of the GitHub repository
    print("Downloading the contents of the GitHub repository...")
    url = 'https://github.com/fayaz12g/smo-aar/archive/main.zip'
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


def launch_totk():
    # Check if an update is required
    if check_and_update_version_totk(totk_gui_dir):
        update_app_data_totk(totk_gui_dir, aar_dir)

    # Specify the path to the Python script you want to launch
    totk_gui = os.path.join(totk_gui_dir, 'GUI.py')

    # Get the path to the current executable (the PyInstaller-built application)
    current_executable = sys.executable

    # Build the command to execute the other Python script
    launch_totk_command = ["python", totk_gui]

    # Use subprocess to launch the script
    try:
        root.destroy()
        subprocess.run(launch_totk_command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    root.destroy()

def launch_mk8d():
    if check_and_update_version_mk8d(mk8d_gui_dir):
        update_app_data_mk8d(mk8d_gui_dir, aar_dir)

    # Specify the path to the Python script you want to launch
    mk8d_gui = os.path.join(mk8d_gui_dir, 'GUI.py')

    # Get the path to the current executable (the PyInstaller-built application)
    current_executable = sys.executable

    # Build the command to execute the other Python script
    launch_mk8d_command = ["python", mk8d_gui]

    # Use subprocess to launch the script
    try:
        root.destroy()
        subprocess.run(launch_mk8d_command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    
    root.destroy()


def launch_smo():
    if check_and_update_version_smo(smo_gui_dir):
        update_app_data_smo(smo_gui_dir, aar_dir)

    # Specify the path to the Python script you want to launch
    smo_gui = os.path.join(smo_gui_dir, 'GUI.py')
    # Get the path to the current executable (the PyInstaller-built application)
    current_executable = sys.executable

    # Build the command to execute the other Python script
    launch_smo_command = ["python", smo_gui]

    # Use subprocess to launch the script
    try:
        root.destroy()
        subprocess.run(launch_smo_command, check=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")




# Automatically start the process
show_update_progress()

mario_button = customtkinter.CTkButton(master=root, text="AAR for Mario Odyssey", command=launch_smo)
mario_button.pack(pady = 50)

totk_button = customtkinter.CTkButton(master=root, text="AAR for Tears of the Kingdom", command=launch_totk)
totk_button.pack(pady = 50)

mk8d_button = customtkinter.CTkButton(master=root, text="AAR for MarioKart 8 Deluxe", command=launch_mk8d)
mk8d_button.pack(pady = 50)

text_box = customtkinter.CTkLabel(master=root, text=f"If there is an update, or you have not downloaded the program before, \nit may take up to a minute and say not responding when launching. \nPlease just wait. Also, ensure you have Python installed." )
text_box.pack(pady=50)

root.mainloop()