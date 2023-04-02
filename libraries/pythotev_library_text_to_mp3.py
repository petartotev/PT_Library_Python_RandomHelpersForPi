"""This Pythotev script reads a string and reads it in a mp3 file with gTTs library"""

import os
from gtts import gTTS

def read_string_into_mp3_file(string, directory, file_name):
    """This function reads a string into mp3 file"""
    if directory[-1] != "/":
        directory = directory + "/"
    if ".mp3" not in file_name:
        file_name = file_name + ".mp3"
    file_path = f'{directory}{file_name}'
    def_lang = 'en'
    gtts_object = gTTS(text = string, lang = def_lang, slow = False)
    gtts_object.save(file_path)
    return file_path

def play_mp3_file(file_path):
    """This function plays a mp3 file using omxplayer"""
    os.system(f'omxplayer -o alsa {file_path}')
