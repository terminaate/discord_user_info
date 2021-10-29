import json
from requests_tor import RequestsTor

rt = RequestsTor()
rt = RequestsTor(tor_ports=(9050,), tor_cport=9051)

with open('settings.json', 'r') as r:
    header = json.load(r)['header']

def get_mutual_guilds(profile_data):
    if profile_data['mutual_guilds']:
        profile_data['guilds'] = ""
        for mutual_guild in profile_data['mutual_guilds']:
            guild_data = json.loads(rt.get(
                f"https://discord.com/api/v9/guilds/{mutual_guild['id']}/preview",
                headers=header).text)
            profile_data['guilds'] += f"""\n
\tGuild ID : {mutual_guild['id']}
\tUser Guild Nick : {mutual_guild['nick']}
\tGuild name : {guild_data['name']}
\tGuild description : {guild_data['description']}\n"""
    else:
        profile_data['guilds'] = "None"
        
    return profile_data['guilds']
