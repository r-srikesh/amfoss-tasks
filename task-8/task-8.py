import os
from github import Github   
user=Github().get_user("amfoss")   
for repo in user.get_repos():   
    print(repo.name)
    os.system('perceval git --json-line https://github.com/amfoss/'+repo.name+'>> task-8.json') 
os.system('cat task-8.json')
