from tools.userid2date import convert
from tools.accounts.connected_accounts import get_connected_accounts
from tools.mutual_guilds import get_mutual_guilds

def rendertext(profile_data):
    
    hypesquads = {256: "HypeSquad Balance", 64: "HypeSquad Bravery", 128: "HypeSquad Brilliance", 0 : "None"}
    
    profile_data['user']['hypesquad'] = hypesquads.get(profile_data['user']['public_flags'])
        
    profile_data['user']['nitro'] = bool(profile_data['premium_since'])
    
    bio = str(profile_data['user']['bio'])
    
    profile_data['user']['bio'] = bio.replace('```', '') if len(bio) > 0 else None
            
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
Mutual Guilds : {get_mutual_guilds(profile_data)}
Connected Accounts : {get_connected_accounts(profile_data)}
"""
