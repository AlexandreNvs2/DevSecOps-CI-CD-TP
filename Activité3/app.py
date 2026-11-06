# app.py
import os
import subprocess

user_input = input("Enter a Directory: ")


#os.system("ls " + user_input)
subprocess.run(["ls", "--", user_input], check=False)
