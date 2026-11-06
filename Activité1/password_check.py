# Script Name : password_check.py

user_password = input("Please enter the password to check: \n")

def worst_500_passwords(password):
  
  #Download the SecList
  import requests
  print('Beginning check in 500 worst passwords')
  url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/500-worst-passwords.txt'
  retrieve = requests.get(url, timeout= 10)

  content = retrieve.content

  if str(password) in str(content):
    print("Your password is in 500 worst passwords... Change it immediately\n")
    exit(0)

def worst_10k_passwords(password):
 
  #Download the SecList
  import requests
  print('Beginning check in 10K worst passwords')
  url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt'
  retrieve = requests.get(url, timeout= 10)

  content = retrieve.content

  if str(password) in str(content):
    print("Your password is in 10K worst passwords... Change it immediately\n")
    exit(0)

if __name__ == "__main__":
  worst_500_passwords(user_password)
  worst_10k_passwords(user_password)
