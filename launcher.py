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
import subprocess
import packaging
import psutil
from keystone import *
import pyautogui

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
tool_version = "8.0"

# Platform-specific directory setup
if sys.platform == 'win32':
    username = os.environ.get('USERNAME')
    aar_dir = f'C:\\Users\\{username}\\AppData\\Roaming\\AnyAspectRatio'
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
    {'1': 'home', '2': 'Home Menu'},
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

        # Search bar
        self.search_var = customtkinter.StringVar()
        self.search_var.trace('w', self.filter_games)
        self.search_entry = customtkinter.CTkEntry(
            self.main_container,
            placeholder_text="Search games...",
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
        
        # Create game cards
        self.create_game_cards()

        # Open AAR Folder button at bottom
        self.folder_button = customtkinter.CTkButton(
            self.main_container,
            text="Open AAR Folder",
            command=self.open_aar_folder
        )
        self.folder_button.grid(row=3, column=0, pady=(20, 0))

        # Bind window resize event
        self.bind("<Configure>", self.on_window_resize)

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
        
        # Load and resize game image
        image_path = os.path.join("./images", f"{game_info['1']}.jpg")
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

        # Bind hover events and change cursor
        card.bind("<Enter>", lambda e: self.on_card_hover(card, title_label, True))
        card.bind("<Leave>", lambda e: self.on_card_hover(card, title_label, False))
        card.bind("<Button-1>", lambda e: self.launch_tool(game_info['1']))

        # Make the entire card and its children show pointer cursor
        for widget in [card, image_label, title_label]:
            widget.bind("<Enter>", lambda e, w=widget: (self.on_card_hover(card, title_label, True), 
                                                      self.configure(cursor="hand2")))
            widget.bind("<Leave>", lambda e, w=widget: (self.on_card_hover(card, title_label, False), 
                                                      self.configure(cursor="")))

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
        update_notification = customtkinter.CTkLabel(
            self.main_container,
            text="Fetching contents, please wait..."
        )
        update_notification.grid(row=4, column=0, pady=5)
        
        if check_and_update_version(gui_dirs[tool_name], tool_name):
            newthread(aar_dir, tool_name)
            
        gui_script = os.path.join(gui_dirs[tool_name], 'GUI.py')
        sys.path.append(gui_dirs[tool_name])
        self.destroy()
        
        try:
            import GUI
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

    def open_aar_folder(self):
        os.startfile(aar_dir)

if __name__ == "__main__":
    show_update_progress()
    # check_and_install_dependencies()
    app = GameLauncher()
    app.mainloop()