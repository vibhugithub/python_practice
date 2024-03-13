"""
Q1. Make a function named copyFileContent which takes 2 filenames
(filename1, filename2) as an argument. Copy the content of filename1 to
filename2.

"""

import os


def copyFileContent(file, copyfile):
    try:
        with open(file, "r") as f:
            data = f.read()
            with open(copyfile, "w") as fi:
                fi.write(data)
                print(data)
            f.close()

            fi.close()
    except FileNotFoundError:
        print("Error: One or both files not found.")
    except IOError:
        print("Error: An I/O error occurred.")
    except Exception as e:
        print(f"ERROR-----{e}")


filename = "".join([os.getcwd(), "/Assignments/Week6/text.txt"])
copyfilename = "".join([os.getcwd(), "/Assignments/Week6/new.txt"])
print("path----",filename,"   ", copyfilename)
copyFileContent(filename, copyfilename)
