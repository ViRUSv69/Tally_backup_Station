import shutil as s
import os
import logging
import tkinter as tk
from tkinter import messagebox as msg
import json

root = tk.Tk()
root.withdraw()

logging.basicConfig(
    filename="Instant_O.log",
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%d-%m-%y %I:%M %p'
)

jsonLocator = open('config.json', 'r')
jsonData = jsonLocator.read()
obj = json.loads(jsonData)

place = list = obj['DRIVE_1']
destination = list = obj['DESTINATION']
if os.path.exists(place): # -------[DRIVE]-------
    for files in os.listdir(place):
        if files.startswith('Tally'):
            print("true")
            s.copytree(place+files,destination+files, dirs_exist_ok=True)
    logging.info("BACK-UP SUCCESSFUL")
    msg.showinfo("SUCCESS", "BACK-UP SUCCESSFUL")

else: # -------[NO DRIVE]-------
    logging.error("NO DRIVE WAS FOUND")
    msg.showinfo("ERROR", "NO DRIVE WAS FOUND")
    
# os.startfile('Instant_O.log')