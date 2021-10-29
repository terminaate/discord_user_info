from tools.userid2date import convert
from requests_tor import RequestsTor
import json

rt = RequestsTor()
rt = RequestsTor(tor_ports=(9050,), tor_cport=9051)

with open('settings.json', 'r') as r:
    header = json.load(r)['header']

def rendertext(profile_data):
    
    hypesquads = {256: "HypeSquad Balance", 64: "HypeSquad Bravery", 128: "HypeSquad Brilliance", 0 : "None"}
    
    profile_data['user']['hypesquad'] = hypesquads.get(profile_data['user']['public_flags'])
        
    profile_data['user']['nitro'] = bool(profile_data['premium_since'])
    
    bio = str(profile_data['user']['bio'])
    
    profile_data['user']['bio'] = bio.replace('```', '') if len(bio) > 0 else None

    if profile_data['mutual_guilds']:
        profile_data['guilds'] = ""
        for mutual_guild in profile_data['mutual_guilds']:
            guild_data = json.loads(rt.get(
                f"https://discord.com/api/v9/guilds/{mutual_guild['id']}/preview",
                headers=header).text)
            profile_data['guilds'] += f"""\n
    Guild ID : {mutual_guild['id']}
    User Guild Nick : {mutual_guild['nick']}
    Guild name : {guild_data['name']}
    Guild description : {guild_data['description']}\n"""
    else:
        profile_data['guilds'] = "None"
            
    services = {
        'steam': 'https://steamcommunity.com/profiles/',
        'github': 'https://github.com/',
        'twitch': 'https://www.twitch.tv/',
        'youtube': 'https://www.youtube.com/channel/'
    }
    
    account_types = [
        ('steam', 'id'),
        ('github', 'name'),
        ('twitch', 'name'),
        ('youtube', 'id')
    ]
            
    if profile_data['connected_accounts']:
        profile_data['accounts'] = ""
        for connected_account in profile_data['connected_accounts']:
            profile_data['accounts'] += f"""\n
    Account ID : {connected_account['id']}
    Account name : {connected_account['name']}
    Account service : {connected_account['type']}\n"""
            
            for i, b in account_types:
                account_type = 'id'
                if b:
                    account_type = 'name'
                if connected_account['type'] == i:
                    profile_data['accounts'] += f"Account url : {services[i]}{connected_account[account_type]}\n"
            
            
            
    return f"""
ID : {profile_data['user']['id']}
Username : {profile_data['user']['username']}#{profile_data['user']['discriminator']}
When account created : {convert(profile_data['user']['id'])}
Avatar : https://cdn.discordapp.com/avatars/{profile_data['user']['id']}/{profile_data['user']['avatar']}
HypeSquad : {profile_data['user']['hypesquad']}
Nitro : {profile_data['user']['nitro']}
When buy nitro : {profile_data['premium_since']}
When boost server : {profile_data['premium_guild_since']}
Banner : https://cdn.discordapp.com/banners/{profile_data['user']['id']}/{profile_data['user']['banner']}?size=1024
Banner color : {profile_data['user']['banner_color']}
Accent color : {profile_data['user']['accent_color']}
Bio : {profile_data['user']['bio']}
Mutual Guilds : {profile_data['guilds']}
"""
