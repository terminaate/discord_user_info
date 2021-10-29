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
\tGuild ID : {mutual_guild['id']}
\tUser Guild Nick : {mutual_guild['nick']}
\tGuild name : {guild_data['name']}
\tGuild description : {guild_data['description']}\n"""
    else:
        profile_data['guilds'] = "None"
            
    services = {
        'steam': 'https://steamcommunity.com/profiles/',
        'spotify': 'https://open.spotify.com/user/',
        'youtube': 'https://www.youtube.com/channel/',
        'twitch': 'https://www.twitch.tv/',
        'github': 'https://github.com/',
        'reddit': 'https://www.reddit.com/user/',
        'twitter': 'https://twitter.com/'
    }
    
    account_types = [
        ('steam', 0),
        ('spotify', 0),
        ('youtube', 0),
        ('twitch', 1),
        ('github', 1),
        ('reddit', 1),
        ('twitter', 1)
    ]
            
    if profile_data['connected_accounts']:
        profile_data['accounts'] = ""
        for connected_account in profile_data['connected_accounts']:
            profile_data['accounts'] += f"""\n
\tAccount ID : {connected_account['id']}
\tAccount Name : {connected_account['name']}
\tAccount service : {connected_account['type']}"""
    
            for i, b in account_types:
                account_type = 'id'
                if b:
                    account_type = 'name'
                if connected_account['type'] == i:
                    account_url = f"{services[i]}{connected_account[account_type]}"
                    profile_data['accounts'] += f"\n\tAccount url : {account_url}"
    else:
        profile_data['accounts'] = "None"
            
            
            
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
Connected Accounts : {profile_data['accounts']}
"""
