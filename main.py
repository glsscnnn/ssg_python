import re
import glob
import markdown
import os
from utility_functions import utility as u


def main():
    # recursively list all items in the directory
    files = os.listdir('./docs')
    for file in files:
        file_path = "./docs/{0}".format(file)
        try:
            u.parse(file_path, file)
        except IsADirectoryError:
            print("There's a directory there please go fix your docs folder")

if __name__ == "__main__":
    main()


"""
with open("docs/index.md", "r") as f:
    index_string = f.read()
    matches = files.findall(index_string)
    for match in matches:
        file_path = "./docs/{0}".format(match)
        try:
            u.parse(file_path, u.get_file_name(match))
        except FileNotFoundError:
            print("Error that files doesn't exist: check index.md")
    f.close()
"""
