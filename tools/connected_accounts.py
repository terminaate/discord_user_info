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


def get_connected_accounts(profile_data):
    if profile_data['connected_accounts']:
        profile_data['accounts'] = ""
        for connected_account in profile_data['connected_accounts']:
            profile_data['accounts'] += f"""\n
\tAccount ID : {connected_account['id']}
\tAccount Name : {connected_account['name']}
\tAccount service : {connected_account['type']}"""

            for i, b in account_types:
                account_type = 'id' if not b else 'name'
                if connected_account['type'] == i:
                    account_url = f"{services[i]}{connected_account[account_type]}"
                    profile_data['accounts'] += f"\n\tAccount url : {account_url}"
                    if i == 'steam':
                        profile_data['accounts'] += f"\n\tSteam info : https://steamid.pro/lookup/{connected_account['id']}"
                    elif i == 'youtube':
                        profile_data['accounts'] += f"\n\tYoutube info : https://socialblade.com/youtube/c/{connected_account['id']}"
    else:
        profile_data['accounts'] = "None"
        
    return profile_data['accounts']
