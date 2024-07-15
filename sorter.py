#!/usr/bin/env python3
import os
import shutil
import sys

def sort_folder(path):

    extensions = {"mp4": 'Videos',
                  "mov": 'Videos',
                  "webm": 'Videos',
                  "avi": 'Videos',
                  "mkv": 'Videos',
                  "wmv": 'Videos',
                  "jpg": 'Pictures',
                  "png": 'Pictures',
                  "jpeg": 'Pictures',
                  "webp": 'Pictures',
                  "bmp": 'Pictures',
                  "gif": 'Pictures',
                  "pdf": 'Documents',
                  "doc": 'Documents',
                  "docx": 'Documents',
                  "xls": 'Documents',
                  "xlsx": 'Documents',
                  "ppt": 'Documents',
                  "pptx": 'Documents',
                  "zip": 'Archive',
                  "rar": 'Archive',
                  "7z": 'Archive',
                  "tar": 'Archive',
                  "mp3": 'Music',
    }

    for filename in os.listdir(path):

        if os.path.isfile(os.path.join(path, filename)):
            file_extension = filename.split(".")[-1].lower()

            if file_extension in extensions:
                target_folder = extensions[file_extension]
                target_path = os.path.join(path, target_folder)

                if not os.path.exists(target_path):
                    os.mkdir(target_path)

                shutil.move(os.path.join(path, filename), os.path.join(target_path, filename))



if len(sys.argv) > 1:
    sort_folder(sys.argv[-1].replace("~", f"/home/{os.getlogin()}"))
else:
    sort_folder(os.getcwd())

