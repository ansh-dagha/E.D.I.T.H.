import os
import shutil

def create_intents(profile):
    src = r".\Model\intents.json"
    name = ".\Model\\"+profile+"_intents.json"
    dest = name
    path = shutil.copyfile(src,dest)
