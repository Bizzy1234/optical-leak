import json
from subprocess import call 
import threading
from termcolor import colored
import json as jsond  # json
from keyauth import api

import time  # sleep before exit

import binascii  # hex encoding

import requests  # https requests

from uuid import uuid4  # gen random guid

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
# aes + padding, sha256

import webbrowser
import platform
import subprocess
import datetime
import sys
import os

from requests_toolbelt.adapters.fingerprint import FingerprintAdapter

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class PythonNotInstalled(Exception):

    def __init__(self, message="Python is not installed"):
        self.message = message
        super().__init__(self.message)


while True:
    print("Checking Servers")
    cls()
    response = subprocess.check_output(sys.executable + " -m pip --version", shell=True, universal_newlines=True)

    if "No module named" in response:
        print("Installing Libraries")
        os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
        os.system(f"{sys.executable} get-pip.py")
        os.system("del get-pip.py")
    try:
        import asyncio
        import aiohttp
        import easygui
        import requests
        import fade
        import hashlib
        import concurrent.futures
        import ctypes
        from datetime import datetime
        from time import sleep
        import re
        import configparser
        import requests_toolbelt

        break

    except ModuleNotFoundError as e:
        module = e.name
        print(f"{module} not found")
        subprocess.Popen([sys.executable, "-m", "pip", "install", module]).wait()


config = configparser.ConfigParser()


def login():
    ctypes.windll.kernel32.SetConsoleTitleW("Optical")
    print(colored("Connecting to servers..",'green'))
    sleep(1.2)
    cls()

    login_text = ("""\n
 ▒█████   ██▓███  ▄▄▄█████▓ ██▓ ▄████▄   ▄▄▄       ██▓    
▒██▒  ██▒▓██░  ██▒▓  ██▒ ▓▒▓██▒▒██▀ ▀█  ▒████▄    ▓██▒    
▒██░  ██▒▓██░ ██▓▒▒ ▓██░ ▒░▒██▒▒▓█    ▄ ▒██  ▀█▄  ▒██░    
▒██   ██░▒██▄█▓▒ ▒░ ▓██▓ ░ ░██░▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░    
░ ████▓▒░▒██▒ ░  ░  ▒██▒ ░ ░██░▒ ▓███▀ ░ ▓█   ▓██▒░██████▒
░ ▒░▒░▒░ ▒▓▒░ ░  ░  ▒ ░░   ░▓  ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░
  ░ ▒ ▒░ ░▒ ░         ░     ▒ ░  ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░
░ ░ ░ ▒  ░░         ░       ▒ ░░          ░   ▒     ░ ░   
    ░ ░                     ░  ░ ░            ░  ░    ░  ░
                               ░                          """)

    faded_login = fade.purpleblue(login_text)
    print(faded_login)

    def getchecksum():
        path = os.path.basename(__file__)
        if not os.path.exists(path):
            path = path[:-2] + "exe"
        md5_hash = hashlib.md5()
        a_file = open(path, "rb")
        content = a_file.read()
        md5_hash.update(content)
        digest = md5_hash.hexdigest()
        return digest

    keyauthapp = api(
    name = "optical fortnite",
    ownerid = "SnGFieyCFz",
    secret = "05f0d2188a160afdd989a6fa3a11f66b3d10d62b8882237bc87167ed016f8a55",
    version = "1.0",
    hash_to_check = getchecksum()
)

    def write_file():
        config.write(open('config.ini', 'w'))
    print(colored('[!] Choose Option (1 or 2)','cyan')) 
    print("""
  1: Login
    """)
    print("""  2: Exit
  """)
    chosen = False
    while not chosen:
        ans = input(colored("Select Option: ",'cyan'))
        if ans == "1":
            chosen = True
            key = input('Enter your license:')
            keyauthapp.license(key)
        if ans == "2":
            exit()
        if ans == "":
            print(colored("Not Valid Option",'red'))
        sleep(1.0)
        os.system('cls')
login()


path = "lib/config"

print(colored(" [Optical] Please make your x and y sens the same",'cyan'))
def prompt(str):
        valid_input = False
        while not valid_input:
            try:
                number = float(input(str))
                valid_input = True
            except ValueError:
                print(colored("[!] Invalid Input. Make sure to enter only the number (e.g. 6.9)",'cyan'))
        return number

xy_sens = prompt("Enter your X and Y sens from Fortnite: ")
targeting_sens = prompt("Enter your targeting sensitivity from Fortnite: ")

print("Optical Make your targeting sens and scoped sense the same")
sensitivity_settings = {"xy_sens": xy_sens, "targeting_sens": targeting_sens, "xy_scale": 10/xy_sens, "targeting_scale": 1000/(targeting_sens * xy_sens)}

with open('lib/config/config.json', 'w') as outfile:
    json.dump(sensitivity_settings, outfile)
    print(colored("Optical Sensitivity configuration complete",'cyan'))


import dearpygui.dearpygui as dpg
import json
import os
import sys
import threading
import time
from pynput import keyboard
from pynput.keyboard import Key, Controller
from termcolor import colored
import subprocess
import keyboard
from subprocess import call 
import psutil
from lib.events import Aimbot



dpg.create_context()
dpg.create_viewport(title='Optical', width=600, height=300, decorated=True, always_on_top=False, clear_color=(255, 255, 255, 255))
def on_insert():
    print('insert was pressed')
    dpg.set_viewport_always_top(True)
    keyboard.add_hotkey('insert', on_insert)


def on_del():
    print('delete was pressed')
    dpg.set_viewport_always_top(False)
    dpg.minimize_viewport
    keyboard.add_hotkey('delete', on_del)

dpg.show_imgui_demo
dpg.set_viewport_max_height(240)
dpg.set_viewport_max_width(500)
dpg.set_viewport_min_height(240)
dpg.set_viewport_min_width(500)
def print_me(sender):
    keyboard = Controller() 
    keyboard.press(Key.f2)#press f2 to close earlier instance of the nn windows
    keyboard.release(Key.f2)
def aimkey_alt():
    global aimkey
    aimkey = "alt"
    print(aimkey)
def aimkey_shift():
    global aimkey
    aimkey = "shift"
    print(aimkey)
def aimkey_leftMouse():
    global aimkey
    aimkey = "leftMouse"
    print(aimkey)
def aimkey_rightMouse():
    global aimkey
    aimkey = "rightMouse"
    print(aimkey)
def aimkey_ctrl():
    global aimkey
    aimkey = "ctrl"
    print(aimkey)
def aimkey_mouse5():
    global aimkey
    aimkey = "mouse5"
    print(aimkey)
def strenght(Sender):
    global aim_strenght
    print(dpg.get_value(Sender))
    aim_strenght = dpg.get_value(Sender)
def detection_threshhold(Sender):
    global dt_value
    print(dpg.get_value(Sender))
    dt_value = (dpg.get_value(Sender))
def fovcolor(Sender):
    print(dpg.get_value(Sender))
def aimbot_toggle(Sender):
    Aimbot.aimbot_status = colored("DISABLED", 'red')


def getAimkeyString(Sender):
    global aimkey
    dpg.get_value(Sender)
    print(dpg.get_value(Sender))
    confAimkey = dpg.get_value(Sender)
    print("Your Aimkey is",confAimkey)
    if confAimkey == "LEFT ALT":
        print("Your Aimkey is LEFT  ALT")
        aimkey = "leftAlt"
    elif confAimkey == "LEFT SHIFT":
        print("Your Aimkey is really LEFT SHIFT")
        aimkey = "leftShift"
    elif confAimkey == "RIGHT CLICK":
        print("Your Aimkey is really RIGHT MOUSE")
        aimkey = "rightMouse"
    elif confAimkey == "LEFT CLICK":
        print("Your Aimkey is really LEFT MOUSE")
        aimkey = "leftMouse"
    elif confAimkey == "MOUSE 4":
        print("Your Aimkey is really MOUSE4")
        aimkey = "mouse4"
    elif confAimkey == "MOUSE 5":
        print("Your Aimkey is really MOUSE5")
        aimkey = "mouse5"
    elif confAimkey == "CNTRL":
        print("Your Aimkey is really CNTRL")
        aimkey = "cntrl"
    elif confAimkey == "`":
        print("Your Aimkey is really `")
        aimkey = "`"
    elif confAimkey == "1":
        print("Your Aimkey is really 1")
        aimkey = "1"
    elif confAimkey == "2":
        print("Your Aimkey is really 2")
        aimkey = "2"
    elif confAimkey == "3":
        print("Your Aimkey is really 3")
        aimkey = "3"
    elif confAimkey == "4":
        print("Your Aimkey is really 4")
        aimkey = "4"
    elif confAimkey == "5":
        print("Your Aimkey is really 5")
        aimkey = "5"
    elif confAimkey == "6":
        print("Your Aimkey is really 6")
        aimkey = "6"
    elif confAimkey == "7":
        print("Your Aimkey is really 7")
        aimkey = "7"
    elif confAimkey == "8":
        print("Your Aimkey is really 8")
        aimkey = "8"
    elif confAimkey == "9":
        print("Your Aimkey is really 9")
        aimkey = "9"
    elif confAimkey == "0":
        print("Your Aimkey is really 0")
        aimkey = "0"
    elif confAimkey == "-":
        print("Your Aimkey is really -")
        aimkey = "-"
    elif confAimkey == "=":
        print("Your Aimkey is really =")
        aimkey = "="
    elif confAimkey == "Q":
        print("Your Aimkey is really Q")
        aimkey = "Q"
    elif confAimkey == "W":
        print("Your Aimkey is really W")
        aimkey = "W"
    elif confAimkey == "E":
        print("Your Aimkey is really E")
        aimkey = "E"
    elif confAimkey == "R":
        print("Your Aimkey is really R")
        aimkey = "R"
    elif confAimkey == "T":
        print("Your Aimkey is really T")
        aimkey = "T"
    elif confAimkey == "Y":
        print("Your Aimkey is really Y")
        aimkey = "Y"
    elif confAimkey == "U":
        print("Your Aimkey is really U")
        aimkey = "U"
    elif confAimkey == "I":
        print("Your Aimkey is really I")
        aimkey = "I"
    elif confAimkey == "O":
        print("Your Aimkey is really O")
        aimkey = "O"
    elif confAimkey == "P":
        print("Your Aimkey is really P")
        aimkey = "P"
    elif confAimkey == "[":
        print("Your Aimkey is really [")
        aimkey = "["
    elif confAimkey == "]":
        print("Your Aimkey is really ]")
        aimkey = "]"
    elif confAimkey == "A":
        print("Your Aimkey is really A")
        aimkey = "A"
    elif confAimkey == "S":
        print("Your Aimkey is really S")
        aimkey = "S"
    elif confAimkey == "D":
        print("Your Aimkey is really D")
        aimkey = "D"
    elif confAimkey == "F":
        print("Your Aimkey is really F")
        aimkey = "F"
    elif confAimkey == "G":
        print("Your Aimkey is really G")
        aimkey = "G"
    elif confAimkey == "H":
        print("Your Aimkey is really H")
        aimkey = "H"
    elif confAimkey == "J":
        print("Your Aimkey is really J")
        aimkey = "J"
    elif confAimkey == "K":
        print("Your Aimkey is really K")
        aimkey = "K"
    elif confAimkey == "L":
        print("Your Aimkey is really L")
        aimkey = "L"
    elif confAimkey == ";":
        print("Your Aimkey is really ;")
        aimkey = ";"
    elif confAimkey == "@":
        print("Your Aimkey is really @")
        aimkey = "@"
    elif confAimkey == "#":
        print("Your Aimkey is really #")
        aimkey = "#"
    elif confAimkey == "Z":
        print("Your Aimkey is really Z")
        aimkey = "Z"
    elif confAimkey == "'":
        print("Your Aimkey is really '")
        aimkey = "'"
    elif confAimkey == "X":
        print("Your Aimkey is really X")
        aimkey = "X"
    elif confAimkey == "C":
        print("Your Aimkey is really C")
        aimkey = "C"
    elif confAimkey == "V":
        print("Your Aimkey is really V")
        aimkey = "V"
    elif confAimkey == "B":
        print("Your Aimkey is really B")
        aimkey = "B"
    elif confAimkey == "N":
        print("Your Aimkey is really N")
        aimkey = "N"
    elif confAimkey == "M":
        print("Your Aimkey is really M")
        aimkey = "M"
    elif confAimkey == ",":
        print("Your Aimkey is really ,")
        aimkey = ","
    elif confAimkey == ".":
        print("Your Aimkey is really .")
        aimkey = "."
    elif confAimkey == "/":
        print("Your Aimkey is really /")
        aimkey = "/"
    elif confAimkey == "CAPS LOCK":
        print("Your Aimkey is really CAPS LOCK")
        aimkey = "capsLock"
    elif confAimkey == "\ ":
        print("Your Aimkey is really \ ")
        aimkey = "\ "

def thread_second():
    call(["python", "extension.py"])
    processThread = threading.Thread(target=thread_second)
    processThread.start()
def close():
    exit()
        
def setsens():
    os.system('python setSens.py')
def fov_state(Sender): #returns 1 or 0 under fov_dis depending on the state of the checkbox
    global fov_dis
    print(dpg.get_value(Sender))
    if dpg.get_value(Sender) == True:
        print("FOV circle is activated")
        fov_dis = 1
    elif dpg.get_value(Sender) == False:
        print("FOV circle is deactivated")
        fov_dis = 0
def save():
    configuration = {"aimkey": aimkey,"fovsize": fovsize,"strenght": aim_strenght,"confidence":dt_value}
    with open('lib/config/guiconf.json', 'w') as outfile:
     json.dump(configuration, outfile)

def on_button_clicked(sender, app_data, user_data):
        exe_path = "splhook.exe"
        if dpg.get_value(sender) == True:
           subprocess.run(exe_path)


def start():
    keyboard = Controller() 
    keyboard.press(Key.f2)
    keyboard.release(Key.f2)
    import json
    import os
    import sys
    import threading
    import time
    from pynput import keyboard
    from termcolor import colored
    
    def on_release(key):
        try:
            if key == keyboard.Key.f1:
                Aimbot.update_status_aimbot()
            if key == keyboard.Key.f2:
                Aimbot.clean_up()
        except NameError:
            pass   
    
    def lunar():
        global lunar
        lunar = Aimbot(collect_data = "collect_data" in sys.argv)
        lunar.start()
    
    def setup():
        path = "lib/config"
        if not os.path.exists(path):
            os.makedirs(path)
    
        print("[OPTICAL] In-game X and Y sensitivity have to be the same!")
        def prompt(str):
            valid_input = False
            while not valid_input:
                try:
                    number = float(input(str))
                    valid_input = True
                except ValueError:
                    print("[!] Invalid Input. Make sure to enter only the number (e.g. 6.9)")
            return number
    
        xy_sens = prompt("X-Axis and Y Sensitivity (from in-game settings): ")
        targeting_sens = prompt("Targeting Sensitivity (from in-game settings): ")
    
        print("[OPTICAL] Your in-game targeting sensitivity must be the same as your scoping sensitivity")
        sensitivity_settings = {"xy_sens": xy_sens, "targeting_sens": targeting_sens, "xy_scale": 8/xy_sens, "targeting_scale": 800/(targeting_sens * xy_sens)}
    
        with open('lib/config/config.json', 'w') as outfile:
            json.dump(sensitivity_settings, outfile)
        print("[OPTICAL] Sensitivity configuration complete")
    
    if __name__ == "__main__":
        os.system('cls' if os.name == 'nt' else 'clear')
        os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
        path_exists = os.path.exists("lib/config/config.json")
        if not path_exists or ("setup" in sys.argv):
            if not path_exists:
                print("[OPTICAL] Ingame sensitivity hasnt been configurated yet...")
            setup()
        path_exists = os.path.exists("lib/data")
        if "collect_data" in sys.argv and not path_exists:
            os.makedirs("lib/data")
        from lib.events import Aimbot
        listener = keyboard.Listener(on_release=on_release)
        listener.start()
        lunar()

        

with dpg.theme() as global_theme:
        with dpg.theme_component(0):
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
            dpg.add_theme_color(dpg.mvThemeCol_TextDisabled, (112, 112, 112, 255))
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (0,0,0))
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (0, 0, 0, 0))
            dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (80, 80, 80, 840))
            dpg.add_theme_color(dpg.mvThemeCol_Border, (255,255,255))
            dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (0, 0, 0, 0))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (28, 28, 28, 255))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (81,81,81))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (0,0,0))
            dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (255,255,255))
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (0,0,0))
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed, (0, 0, 0, 130))
            dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, (28, 28, 28, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (15, 15, 15, 135))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (0,0,0))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (0,0,0))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (0, 0, 0, 0))
            dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (255, 255, 255, 255))
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (255,255,255))
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (255,255,255))
            dpg.add_theme_color(dpg.mvThemeCol_Button, (255,255,255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (255,255,255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (82,139,139))
            dpg.add_theme_color(dpg.mvThemeCol_Header, (47,79,79))
            dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (47,79,79))
            dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (255,255,255))
            dpg.add_theme_color(dpg.mvThemeCol_Separator, (54, 54, 54, 255))
            dpg.add_theme_color(dpg.mvThemeCol_SeparatorHovered, (255,255,255))
            dpg.add_theme_color(dpg.mvThemeCol_SeparatorActive, (0, 46, 130, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ResizeGrip, (54, 54, 54, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ResizeGripHovered, (47,79,79))
            dpg.add_theme_color(dpg.mvThemeCol_ResizeGripActive, (82,139,139))
            dpg.add_theme_color(dpg.mvThemeCol_Tab, (47,79,79))
            dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (47,79,79))
            dpg.add_theme_color(dpg.mvThemeCol_TabActive, (47,79,79))
            dpg.add_theme_color(dpg.mvThemeCol_TabUnfocused, (18, 26, 38, 247))
            dpg.add_theme_color(dpg.mvThemeCol_TabUnfocusedActive, (36, 66, 107, 255))
            dpg.add_theme_color(dpg.mvThemeCol_DockingPreview, (102, 102, 230, 80))
            dpg.add_theme_color(dpg.mvThemeCol_DockingEmptyBg, (51, 51, 51, 255))
            dpg.add_theme_color(dpg.mvThemeCol_PlotLines, (255,255,255))
            dpg.add_theme_color(dpg.mvThemeCol_PlotLinesHovered, (255, 110, 89, 255))
            dpg.add_theme_color(dpg.mvThemeCol_PlotHistogram, (230, 179, 0, 255))
            dpg.add_theme_color(dpg.mvThemeCol_PlotHistogramHovered, (255, 153, 0, 255))
            dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (47,79,79))
            dpg.add_theme_color(dpg.mvThemeCol_TableBorderStrong, (47,79,79))
            dpg.add_theme_color(dpg.mvThemeCol_TableBorderLight, (82,139,139))
            dpg.add_theme_color(dpg.mvThemeCol_TableRowBg, (28, 28, 28, 255))
            dpg.add_theme_color(dpg.mvThemeCol_TableRowBgAlt, (35, 35, 35, 255))
            dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg, (82,139,139))
            dpg.add_theme_color(dpg.mvThemeCol_DragDropTarget, (82,139,139))
            dpg.add_theme_color(dpg.mvThemeCol_NavHighlight, (66, 150, 250, 255))
            dpg.add_theme_color(dpg.mvThemeCol_NavWindowingHighlight, (255, 255, 255, 179))
            dpg.add_theme_color(dpg.mvThemeCol_NavWindowingDimBg, (204, 204, 204, 51))
            dpg.add_theme_color(dpg.mvThemeCol_ModalWindowDimBg, (204, 204, 204, 89))
            dpg.add_theme_color(dpg.mvPlotCol_FrameBg, (28, 28, 28, 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_PlotBg, (0, 0, 0, 128), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_PlotBorder, (47,79,79), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_LegendBg, (28, 28, 28, 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_LegendBorder, (47,79,79), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_LegendText, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_TitleText, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_InlayText, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_XAxis, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_XAxisGrid, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxis, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxisGrid, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxis2, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxisGrid2, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxis3, (255, 255, 255, 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_YAxisGrid3, (255, 255, 255, 50), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_Selection, (66, 150, 250, 89), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_Query, (107, 38, 130, 255), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_Crosshairs, (255, 255, 255, 128), category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (28, 28, 28, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundHovered, (107, 38, 130, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundSelected, (180, 140, 54, 220), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeOutline, (47,79,79), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvThemeCol_Button, (36,36,36))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (81,81,81))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (82,139,139))
            dpg.add_theme_color(dpg.mvNodeCol_TitleBar, (47,79,79), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_TitleBarHovered, (135, 92, 38, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_TitleBarSelected, (140, 92, 38, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_Link, (61, 133, 224, 200), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_LinkHovered, (66, 150, 250, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, (66, 150, 250, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_Pin, (53, 150, 250, 180), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_PinHovered, (53, 150, 250, 255), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_BoxSelector, (61, 133, 224, 30), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_BoxSelectorOutline, (61, 133, 224, 150), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_GridBackground, (40, 40, 50, 200), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_GridLine, (200, 200, 200, 40), category=dpg.mvThemeCat_Nodes)

dpg.bind_theme(global_theme)


dpg.window(no_background=True)

with dpg.window(label="                               Optical",width=520,height=200,no_move=True,no_resize=True,no_close=True,no_collapse=True):
     dpg.add_input_text(label="Aimkey",uppercase=True,callback=getAimkeyString)
     dpg.add_slider_float(label="Strength",min_value=1, default_value=6, max_value=10,callback = strenght)
     dpg.add_slider_float(label="Confidence", min_value=0.2, default_value=0.6, max_value=0.8,callback = detection_threshhold)
     #dpg.add_text("Select FOV Size")
     


     #with dpg.menu(label="FOV size"):
        #dpg.add_menu_item(label="Small", callback=fovsize_small)
        #dpg.add_menu_item(label="Medium", callback=fovsize_medium)
        #dpg.add_menu_item(label="Big", callback=fovsize_big)
     dpg.add_separator()
     dpg.add_checkbox(label="Enable Aimbot", callback=aimbot_toggle)
     dpg.add_button(label="Start",callback=start)
     dpg.add_button(label="Save", callback=save)
     dpg.add_button(label="Exit", callback=close)
     

     
     
    # with dpg.menu_bar():
        #with dpg.menu(label="Aimbot"):
         #with dpg.menu(label="Config"):
                   # dpg.add_menu_item(label="", callback=print_me)
                    #dpg.add_menu_item(label="Save Config", callback=print_me)    
        #with dpg.menu(label=""):
           # dpg.add_checkbox(label=")", callback=fov_state,default_value=False)
           # dpg.add_color_picker(label="Select Colour", width=90, height=90, callback=fovcolor)
        #with dpg.menu(label=""):
           # dpg.add_text("")
  


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
