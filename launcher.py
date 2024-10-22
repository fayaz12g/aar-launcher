import os
import shutil
import requests
from zipfile import ZipFile
import sys
import subprocess
from threading import Thread
import getpass
import webbrowser
from tkinter import *
from tkinter import scrolledtext
from tkinter.filedialog import askdirectory
import customtkinter
from customtkinter import *
from PIL import Image, ImageTk
import subprocess
import packaging
import psutil
from keystone import *
import pyautogui
import time

# Keep your original dependencies list
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

# Keep all your original helper functions
def is_pip_installed():
    try:
        subprocess.run(["pip", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def install_pip():
    try:
        subprocess.run(["python", "-m", "ensurepip", "--default-pip"], check=True)
        print("pip has been successfully installed.")
    except subprocess.CalledProcessError:
        print("Failed to install pip. Please install it manually.")

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

def install_dependency(dependency):
    try:
        subprocess.run(["python", "-m", "pip", "install", dependency], check=True)
        print(f"{dependency} has been successfully installed.")
    except subprocess.CalledProcessError:
        print(f"Failed to install {dependency}. Please install it manually.")

def show_update_progress():
    global aar_dir
    if not os.path.exists(aar_dir):
        print(f"Directory '{aar_dir}' does not exist. Creating the directory...")
        os.makedirs(aar_dir)

# Keep your version and directory setup
tool_version = "8.0.1"

# Platform-specific directory setup
if sys.platform == 'win32':
    username = os.environ.get('USERNAME')
    aar_dir = f'C:\\Users\\{username}\\AppData\\Roaming\\AnyAspectRatio'
    images_dir = f'C:\\Users\\{username}\\AppData\\Roaming\\AnyAspectRatio\\perm\\images'
elif sys.platform == 'darwin':
    username = os.getenv('USER') or os.getenv('LOGNAME')
    aar_dir = f'/Users/{username}/Library/Application Support/AnyAspectRatio'
elif sys.platform.startswith('linux'):
    username = os.getenv('USER') or os.getenv('LOGNAME')
    aar_dir = f'/home/{username}/.config/AnyAspectRatio'
else:
    raise NotImplementedError("Unsupported platform")

# Keep your original tools list
aar_tools = [
    {'1': 'totk', '2': 'Tears of the Kingdom'},
    {'1': 'botw', '2': 'Breath of the Wild'},
    {'1': 'eow', '2': 'Echoes of Wisdom'},
    {'1': 'zla', '2': "Link's Awakening"},
    {'1': 'won', '2': 'Super Mario Wonder'},
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
    {'1': 'pmtok', '2': 'Paper Mario: The Origami King'},
    {'1': 'acnh', '2': 'Animal Crossing New Horizons'},
    {'1': 'ctt', '2': 'Captain Toad Treasure Tracker'},
    {'1': 'home', '2': 'Home Menu'},
]

# Setup gui_dirs
gui_dirs = {}
for tool in aar_tools:
    gui_dirs[tool['1']] = os.path.join(aar_dir, f'{tool["1"]}-aar-main')

# Keep your version checking and update functions
def check_and_update_version(gui_dir, tool_name):
    gui_path = os.path.join(gui_dir, 'GUI.py')
    if os.path.exists(gui_dir):
        with open(gui_path, 'r') as file:
            for line in file:
                if line.startswith("tool_version"):
                    current_version = line.split('=')[1].strip().strip('"')
                    break
        url = f'https://raw.githubusercontent.com/fayaz12g/{tool_name}-aar/main/GUI.py'
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

def update_app_data(gui_dir, aar_dir, tool_name):
    if os.path.exists(gui_dir):
        shutil.rmtree(gui_dir)

    print("Downloading the contents of the GitHub repository...")
    url = f'https://github.com/fayaz12g/{tool_name}-aar/archive/main.zip'
    response = requests.get(url)

    zip_file_path = os.path.join(aar_dir, f'{tool_name}-aar-main.zip')
    with open(zip_file_path, 'wb') as zip_file:
        zip_file.write(response.content)

    with ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(aar_dir)

    os.remove(zip_file_path)

def newthread(aar_dir, tool_name):
    t = Thread(target=update_app_data, args=(gui_dirs[tool_name], aar_dir, tool_name))
    t.start()



def download_and_extract_images(images_dir):
    try:
        # Create images directory if it doesn't exist
        os.makedirs(images_dir, exist_ok=True)
        
        # Download the images.zip file
        url = 'https://github.com/fayaz12g/aar-files/raw/main/images.zip'
        response = requests.get(url)
        
        # Save the zip file temporarily
        temp_zip = os.path.join(images_dir, 'temp_images.zip')
        with open(temp_zip, 'wb') as f:
            f.write(response.content)
        
        # Extract the zip file
        with ZipFile(temp_zip, 'r') as zip_ref:
            zip_ref.extractall(images_dir)
        
        # Remove the temporary zip file
        os.remove(temp_zip)
        return True
            
    except Exception as e:
        print(f"Error downloading images: {e}")
        return False

class LoadingWindow(customtkinter.CTkToplevel):
    def __init__(self, parent, title="Loading..."):
        super().__init__(parent)
        self.title(title)
        
        # Get parent window size and position
        parent_x = parent.winfo_x()
        parent_y = parent.winfo_y()
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()
        
        # Calculate position for center alignment
        width = 300
        height = 150
        x = parent_x + (parent_width - width) // 2
        y = parent_y + (parent_height - height) // 2
        
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Create main frame
        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.frame.grid_columnconfigure(0, weight=1)
        
        # Loading label
        self.label = customtkinter.CTkLabel(
            self.frame,
            text="Loading...",
            font=customtkinter.CTkFont(size=16, weight="bold")
        )
        self.label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # Progress bar
        self.progressbar = customtkinter.CTkProgressBar(self.frame)
        self.progressbar.grid(row=1, column=0, padx=20, pady=(0, 20))
        self.progressbar.set(0)
        
        # Status label
        self.status_label = customtkinter.CTkLabel(
            self.frame,
            text="",
            font=customtkinter.CTkFont(size=12)
        )
        self.status_label.grid(row=2, column=0, padx=20)
        
        self.update()

    def update_progress(self, value, status_text):
        self.progressbar.set(value)
        self.status_label.configure(text=status_text)
        self.update()

# New Modern UI Class
class GameLauncher(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title(f"Any Aspect Ratio Launcher {tool_version}")
        self.geometry("900x700")
        
        # Enable window resizing
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("blue")

        # Create main container
        self.main_container = customtkinter.CTkFrame(self)
        self.main_container.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.main_container.grid_columnconfigure(0, weight=1)
        self.main_container.grid_rowconfigure(2, weight=1)  # Make the scrollable frame expand

        # Title
        self.title_label = customtkinter.CTkLabel(
            self.main_container,
            text=f"Any Aspect Ratio Launcher {tool_version}",
            font=customtkinter.CTkFont(size=24, weight="bold")
        )
        self.title_label.grid(row=0, column=0, pady=(0, 20))

        # Search bar with updated placeholder
        self.search_var = customtkinter.StringVar()
        self.search_var.trace('w', self.filter_games)
        self.search_entry = customtkinter.CTkEntry(
            self.main_container,
            placeholder_text="Search for a game...",  # Updated placeholder text
            width=300,
            textvariable=self.search_var
        )
        self.search_entry.grid(row=1, column=0, pady=(0, 20))

        # Create scrollable frame for game cards
        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self.main_container,
            width=700,
            height=400
        )
        self.scrollable_frame.grid(row=2, column=0, sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # Grid for game cards
        self.grid_frame = customtkinter.CTkFrame(self.scrollable_frame, fg_color="transparent")
        self.grid_frame.grid(row=0, column=0, sticky="nsew")
        self.grid_frame.grid_columnconfigure((0, 1, 2), weight=1)  # Make columns expand equally

        # Store game cards for filtering
        self.game_cards = []
        
        # Check for missing images before creating cards
        self.check_and_download_images()

        # Initialize game cards after everything else
        self.initialize_game_cards()

        # Open AAR Folder button at bottom
        self.folder_button = customtkinter.CTkButton(
            self.main_container,
            text="Open AAR Folder",
            command=self.open_aar_folder
        )
        self.folder_button.grid(row=3, column=0, pady=(20, 0))

        # Bind window resize event
        self.bind("<Configure>", self.on_window_resize)

        # Add a flag to prevent multiple launches
        self.launching = False


    def check_and_download_images(self):
        missing_images = False
        for game in aar_tools:
            if game['1'] == 'home':  # Skip checking for home image
                continue
            image_path = os.path.join(images_dir, f"{game['1']}.jpg")
            if not os.path.exists(image_path):
                missing_images = True
                break
        
        if missing_images:
            loading_window = LoadingWindow(self, "Downloading Cover Art")
            
            def download_process():
                success = download_and_extract_images(images_dir)
                
                def update_ui():
                    if success:
                        loading_window.update_progress(1.0, "Cover art download complete!")
                        self.after(1000, loading_window.destroy)
                        # Initialize game cards after successful download
                        self.after(1100, self.initialize_game_cards)
                    else:
                        loading_window.status_label.configure(text="Error downloading cover art")
                        loading_window.progressbar.configure(progress_color="red")
                        self.after(2000, loading_window.destroy)
                        # Initialize game cards even if download failed
                        self.after(2100, self.initialize_game_cards)
                
                self.after(0, update_ui)
            
            Thread(target=download_process, daemon=True).start()
            loading_window.update_progress(0.5, "Downloading and extracting cover art...")
        else:
            # If no images are missing, initialize cards immediately
            self.initialize_game_cards()

    def initialize_game_cards(self):
        # Clear existing cards if any
        for card in self.game_cards:
            card['frame'].destroy()
        self.game_cards = []
        
        # Create new cards
        self.create_game_cards()

    def create_game_card(self, game_info, row, col):
        # Create frame for card
        card = customtkinter.CTkFrame(
            self.grid_frame,
            width=150,
            height=150,
            fg_color=("gray90", "gray16")
        )
        card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        card.grid_propagate(False)
        
        # Load and resize game image using images_dir
        image_path = os.path.join(images_dir, f"{game_info['1']}.jpg")
        try:
            img = Image.open(image_path)
            img = img.resize((150, 150), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            
            # Image label
            image_label = customtkinter.CTkLabel(
                card,
                image=photo,
                text=""
            )
            image_label.image = photo
            image_label.pack(pady=(10, 5))
            
        except FileNotFoundError:
            # Fallback if image not found
            image_label = customtkinter.CTkLabel(
                card,
                text="No Image",
                width=150,
                height=150,
                fg_color=("gray80", "gray20")
            )
            image_label.pack(pady=(10, 5))

        # Game title
        title_label = customtkinter.CTkLabel(
            card,
            text=game_info['2'],
            font=customtkinter.CTkFont(weight="bold")
        )
        title_label.pack(pady=(0, 10))

        # Create a single click handler for the card
        def card_click(event):
            if not self.launching:  # Check if already launching
                self.launch_tool(game_info['1'])

        # Bind click events to all components
        for widget in [card, image_label, title_label]:
            widget.bind("<Button-1>", card_click)
            widget.bind("<Enter>", lambda e, w=widget: (
                self.on_card_hover(card, title_label, True),
                self.configure(cursor="hand2")
            ))
            widget.bind("<Leave>", lambda e, w=widget: (
                self.on_card_hover(card, title_label, False),
                self.configure(cursor="")
            ))

        return {
            'frame': card,
            'title': game_info['2'],
            'shortname': game_info['1'],
            'row': row,
            'col': col
        }

    def create_game_cards(self):
        cols = 3  # Number of columns in the grid
        for i, game in enumerate(aar_tools):
            row = i // cols
            col = i % cols
            card_info = self.create_game_card(game, row, col)
            self.game_cards.append(card_info)

    def on_card_hover(self, card, title_label, entering):
        if entering:
            card.configure(fg_color=("gray80", "gray20"))
            title_label.configure(fg_color=("gray80", "gray20"))
        else:
            card.configure(fg_color=("gray90", "gray16"))
            title_label.configure(fg_color=("gray90", "gray16"))

    def filter_games(self, *args):
        search_text = self.search_var.get().lower()
        visible_cards = []
        
        # First, remove all cards from grid
        for card in self.game_cards:
            card['frame'].grid_remove()
        
        # Then, add back only the matching ones in a compact grid
        for card in self.game_cards:
            if search_text in card['title'].lower():
                visible_cards.append(card)
        
        # Reposition visible cards in a compact grid
        cols = 3
        for i, card in enumerate(visible_cards):
            row = i // cols
            col = i % cols
            card['frame'].grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

    def on_window_resize(self, event):
        # Update the layout when the window is resized
        width = self.winfo_width()
        # Adjust number of columns based on window width
        cols = max(1, width // 250)  # 250 is approximate minimum width for each card
        
        # Reconfigure grid columns
        for i in range(cols):
            self.grid_frame.grid_columnconfigure(i, weight=1)
        
        # Reposition all visible cards
        visible_cards = [card for card in self.game_cards if card['frame'].winfo_viewable()]
        for i, card in enumerate(visible_cards):
            row = i // cols
            col = i % cols
            card['frame'].grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

    def launch_tool(self, tool_name):
        if self.launching:  # Prevent multiple launches
            return
            
        self.launching = True
        
        try:
            # Create loading window
            loading_window = LoadingWindow(self, "Launching Game...")
            loading_window.update_progress(0.2, "Checking for updates...")
            
            def launch_process():
                try:
                    # Check for updates
                    if check_and_update_version(gui_dirs[tool_name], tool_name):
                        loading_window.update_progress(0.4, "New version found. Downloading...")
                        update_app_data(gui_dirs[tool_name], aar_dir, tool_name)
                        loading_window.update_progress(0.6, "Download complete. Installing...")
                    else:
                        loading_window.update_progress(0.4, "No updates needed...")

                    loading_window.update_progress(0.8, "Preparing to launch...")
                    
                    # Get the path to the GUI script
                    gui_dir = gui_dirs[tool_name]
                    gui_script = os.path.join(gui_dir, 'GUI.py')
                    
                    # Get the correct Python interpreter path
                    if getattr(sys, 'frozen', False):
                        # If we're in a PyInstaller bundle
                        python_path = os.path.join(sys._MEIPASS, 'python.exe') if sys.platform == 'win32' else 'python3'
                    else:
                        # If we're running from script
                        python_path = sys.executable

                    loading_window.update_progress(1.0, "Launch complete!")
                    
                    # Launch the new process with full path specification
                    try:
                        if sys.platform == 'win32':
                            startupinfo = subprocess.STARTUPINFO()
                            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                            process = subprocess.Popen(
                                [python_path, gui_script],
                                startupinfo=startupinfo,
                                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
                                env=os.environ.copy(),  # Pass current environment
                                cwd=gui_dir  # Set working directory to script location
                            )
                        else:
                            process = subprocess.Popen(
                                [python_path, gui_script],
                                start_new_session=True,
                                env=os.environ.copy(),
                                cwd=gui_dir
                            )
                        
                        # Wait briefly to ensure process started
                        time.sleep(1)
                        if process.poll() is None:  # Process is running
                            loading_window.destroy()
                            self.destroy()
                            os._exit(0)
                        else:
                            raise Exception("Failed to start process")
                            
                    except Exception as launch_error:
                        print(f"Launch error: {launch_error}")
                        raise
                    
                except Exception as e:
                    self.launching = False
                    loading_window.status_label.configure(text=f"Error: {str(e)}")
                    loading_window.progressbar.configure(progress_color="red")
                    self.after(2000)
                    loading_window.destroy()
                    print(f"Error launching tool: {e}")

            # Start the launch process
            Thread(target=launch_process, daemon=True).start()
            
        except Exception as e:
            self.launching = False
            print(f"Error creating loading window: {e}")

    def open_aar_folder(self):
        os.startfile(aar_dir)


show_update_progress()
# check_and_install_dependencies()
app = GameLauncher()
app.mainloop()