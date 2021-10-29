from tools.accounts.account_types import *

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
    else:
        profile_data['accounts'] = "None"
        
    return profile_data['accounts']
