#!/usr/bin/env python3
import os
import shutil


def sorting(path):

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
                  "pptx": 'Documnets',
                  "zip": 'Archive',
                  "rar": 'Archive',
                  "7z": 'Archive',
                  "tar": 'Archive',
                  "mp3": 'Music',
    }

    for filename in os.listdir(path):

        if os.path.isfile(os.path.join(path, filename)):
            file_extension = filename.split(".")[-1]

            if file_extension in extensions:
                target_folder = extensions[file_extension]
                target_path = os.path.join(path, target_folder)

                if target_folder not in os.listdir(path):
                    os.mkdir(target_path)

                shutil.move(os.path.join(path, filename), os.path.join(target_path, filename))


location = input("Are you in the directory you want to sort(y/n): ")

if location.lower() == "y":
    sorting(os.getcwd())

else:
    directory_path = input("Enter the path to the directory: ")
    sorting(directory_path)
