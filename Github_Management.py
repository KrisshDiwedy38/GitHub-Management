import requests 
import os 
import sys
from github_token import gitHubToken

def cont():
   while True:
      ask = input("Want to continue (y/n)? ")
      if ask == 'n':
         print("----- Exiting -----")
         return False
      elif ask == 'y':
         return True
      else:
         print("Wrong input")
         cont()

def get_headers(token):
   # Getting Headers for Authorization 
   return {
         "Authorization": f"Bearer {token}",
         "Accept": "application/vnd.github+json",
         "X-GitHub-Api-Version": "2022-11-28"
      }

def create_repo(token):
   repo_name = input("Enter new repository name: ")
   description = input("Enter repository description: ")
   private_repo = input("Is this a private repository ? (y/n) : ")

   if private_repo.lower() == 'n':
      private_repo = False
   else:
      private_repo = True


   url = "https://api.github.com/user/repos"
   headers = get_headers(token)

   data = { "name" : repo_name , "description" : description , "private" : private_repo}

   pass

def create_issue(token):
   url = f"https://api.github.com/repos/{username}/{repo_name}"
   headers = get_headers(token)
   pass

def list_repo(token):
   url = "https://api.github.com/user/repos"
   headers = get_headers(token)
   pass

def delete_repo(token):
   url = f"https://api.github.com/repos/{username}/{repo_name}"  
   headers = get_headers(token) 
   pass

def menu_system(token):
   print("\nChoose an option:")
   print(" Create a Repository Press 1")
   print(" List Your Repositories Press 2")
   print(" Create an Issue Press 3")
   print(" Delete a Repository Press 4")
    
   task = int(input("Enter Your Choice"))

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
   repeating = cont()
   if repeating:
      menu_system()
   else:
      return


if __name__ == "__main__":
   main()
