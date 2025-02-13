import requests 
import os 
import sys
from github_token import gitHubToken

def cont():
   while True:
      ask = input("Want to exit (y/n)? ")
      if ask == 'y':
         print("----- Exiting -----")
         return False
      elif ask == 'n':
         return True
      else:
         print("Wrong input")
         cont()

def get_headers(token):
   # Getting Headers for Authorization 
   return {
         "Authorization": f"Bearer {token}",
         "Accept": "application/vnd.github+json"
      }

def create_repo(token):
   pass

def create_issue(token):
   pass

def list_repo(token):
   pass

def delete_repo(token):
   pass

def menu_system(token):
   print("\nChoose an option:")
   print(" Create a Repository Press 1")
   print(" List Your Repositories Press 2")
   print(" Create an Issue Press 3")
   print(" Delete a Repository Press 4")
    
   task = input("Enter Your Choice").lower().strip()

   if task == 1:
      create_repo(token)
   elif task == 2:
      list_repo(token)
   elif task == 3:
      create_issue(token)
   elif task == 4:
      delete_repo(token)
   else:
      print("Wrong Input")
      menu_system()


def main():
   token = gitHubToken     #Import your github token here 
   menu_system(token)
   cont()


if __name__ == "__main__":
   main()
