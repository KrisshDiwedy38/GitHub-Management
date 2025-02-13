import requests 
from github_token import gitHubToken


#Function to ask if user want to continue Managing GitHub
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


# Headers for Authorization
def get_headers(token): 
   return {
         'Authorization': f'Bearer {token}',
         "Accept": "application/vnd.github+json",
         "X-GitHub-Api-Version": "2022-11-28"
      }

#Creating Repositories
def create_repo(token):
   repo_name = input("Enter new repository name: ").strip()
   description = input("Enter repository description: ").strip()
   private_repo = input("Is this a private repository ? (y/n) : ").strip()

   #Repo Private OR Public
   if private_repo.lower() == 'n':
      private_repo = False
   else:
      private_repo = True


   url = "https://api.github.com/user/repos"
   headers = get_headers(token)

   data = { "name" : repo_name , "description" : description , 'homepage' : f"https://github.com/{repo_name}", "private" : private_repo}

   response = requests.post(url, headers=headers, json=data)

   if response.status_code == 201:
      print(f"{repo_name} Created successfully!")
   else:
      print(response.status_code)
      print(f"ERROR! {repo_name} could not be created.")


# Creating Issues in Specified Repository
def create_issue(token):
   username = input("Enter GitHub username: ").strip()
   repo_name = input("Enter Repository name: ").strip()
   issue_title = input("Enter Issue Title: ").strip()
   issue_desc = input("Enter Issues description: ").strip()

   url = f"https://api.github.com/repos/{username}/{repo_name}/issues"
   headers = get_headers(token)

   data = {'title' : issue_title , 'body' : issue_desc }

   response = requests.post(url, headers= headers, json = data)
   
   if response.status_code == 201:
      print(f" {issue_title} created successfully!")
   else:
      print(response.status_code)
      print(f"ERROR! {issue_title} could not be created.")


#Listing the existing repositories of user
def list_repo(token):
   url = "https://api.github.com/user/repos"
   headers = get_headers(token)

   repos = []
   
   while url:
      response = requests.get(url, headers = headers )
      if response.status_code == 200:
         repos.extend(response.json())
         url = response.links.get('next' , {}).get('url')   #Handling Pagination
      else:
         print(f"Failed to fetch repositories")
         return
   
   #Extracting Name and URL of Repositories from Stored JSON Data
   print("\n Your Repositories:")
   for repo in repos:
      print(f"-> Name: {repo['name']} | URL: ({repo['html_url']})")


#Deleting Repositories
def delete_repo(token):
   username = input("Enter GitHub username: ").strip()
   repo_name = input("Enter Repository to be deleted: ").strip()
   
   url = f"https://api.github.com/repos/{username}/{repo_name}"  
   headers = get_headers(token) 

   #Confirm is the user wants to deleted the repository
   confirmation = input(f"Are you sure you want to delete {repo_name}? (y/n) ")
   if confirmation == 'n':
      print("Deletion cancelled")
      return
   else:
      response = requests.delete(url, headers=headers)

      if response.status_code == 204:
         print(f" {repo_name} deleted successfully!")
      else:
         print(response.status_code)
         print(f"ERROR! {repo_name} could not be deleted.") 
   
def main():
   token = gitHubToken     #Import your github token here 
   
   while True:
      print("\nChoose an option:")
      print(" Create a Repository Press 1")
      print(" List Your Repositories Press 2")
      print(" Create an Issue Press 3")
      print(" Delete a Repository Press 4")
      
      task = int(input("Enter Your Choice: "))

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

      if cont() == False:
         return
      else:
         continue
      


if __name__ == "__main__":
   main()
