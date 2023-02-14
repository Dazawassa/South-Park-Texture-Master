#Imported to create files and directories.
import os

#Function to open textures.
def opentexturefile():
    global file
    #Exists for error check.
    file = "0"
    file = open(south_park_textures)
    if file != "0":
        input("Textures found.")
    create_directory()

#Creates folder to rip to.
def create_directory():
    #Name of the folder.
    folder_name = "Ripped Textures"
    #If folder isn't present make it.
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        input(f"Folder '{folder_name}' created successfully.")
    else:
        #If it is present then don't.
        input(f"Folder '{folder_name}' already exists.")
    write_files()

def write_files():
    texture_list = 100

#Defines location for texture file. Later this will be a user input.
global south_park_textures
south_park_textures = "win32.tex"
#Runs function to open texture.
opentexturefile()