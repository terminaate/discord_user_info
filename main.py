from requests_tor import RequestsTor
import json
from os import system as console
from tools.rendertext import rendertext
import argparse
import sys

rt = RequestsTor()
rt = RequestsTor(tor_ports=(9050,), tor_cport=9051)

with open('settings.json', 'r') as r:
    user_header = json.load(r)['header']

parser = argparse.ArgumentParser(description="Information of Discord users")
parser.add_argument('--userid', type=str, metavar="User id")
parser.add_argument('--sherlock', type=bool, metavar="Activate sherlock")
parser.add_argument('--txt', type=bool, metavar="Write data in txt file?")

args = parser.parse_args()
userid = args.userid
sherlock = args.sherlock
write_txt = args.txt

console("clear")

def create_txt(name : str):
    f = open(f"{name}.txt", 'a')
    f.close()
     
<<<<<<< HEAD
=======
     
>>>>>>> e06d4b1 (Maybe final release)
def get_profile_data(userid):
    profile_data = rt.get(
        f"https://discord.com/api/v9/users/{userid}/profile?with_mutual_guilds=true",
        headers=user_header
    )
    
    if profile_data.status_code != 200:
        print("\nInvalid userid")
        exit()
    
    profile_data = json.loads(profile_data.text)

    print(profile_data)
        
    print(rendertext(profile_data))
    
    if sherlock:
        main_username = profile_data['user']['username']
        profile_data['usernames'] = f'"{main_username}"'

        for mutual_guild in profile_data['mutual_guilds']:
            if mutual_guild['nick'] != None:
                guild_nicknames = mutual_guild['nick']
                profile_data['usernames'] += f' "{guild_nicknames}" '
        
        print("Please wait. We are analyz nicknames")
        console(f"python3 ./sherlock/sherlock --timeout 1 {profile_data['usernames']}")
        
    if write_txt:
        create_txt(f"{profile_data['user']['username']}_discord")

        with open(f"{profile_data['user']['username']}_discord.txt", 'w') as w:
            w.write(f"{rendertext(profile_data)}")
        
        print(f"\nGet info complete! info is loaded in {profile_data['user']['username']}_discord.txt")
    else:
        print("Here is your information. ;)")
    
if __name__ == '__main__':
    if not userid:
        parser.print_help()
        sys.exit(1)
    
    if len(userid) != 18 or userid.isnumeric() == False:
        print("Invalid userid")
        exit()
        
    get_profile_data(userid)
    
