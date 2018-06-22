import os, slackclient

VALET_SLACK_NAME = 'dumbot'#os.environ.get('dumbot')
VALET_SLACK_TOKEN = 'xoxb-2154537752-370236158289-KCUWSH6PwnAdIchYEtPuryuc'#os.environ.get('')
VALET_SLACK_ID = 'WAWNYHD4J'

# initialize slack client
valet_slack_client = slackclient.SlackClient(VALET_SLACK_TOKEN)

# check if everything is alright
print(VALET_SLACK_NAME)
print(VALET_SLACK_TOKEN)
is_ok = valet_slack_client.api_call("users.list").get('ok')
print(is_ok)

# Getting the bot's id
if(is_ok):
    for user in valet_slack_client.api_call("users.list").get('members'):
        if user.get('name') == VALET_SLACK_NAME:
            print(user.get('id'))