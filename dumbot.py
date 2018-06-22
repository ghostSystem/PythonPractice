import os, slackclient, time
import random

# delay in seconds before checking for new events 
SOCKET_DELAY = 1

# slackbot environment variables
DUMBOT_SLACK_NAME = 'dumbot'
DUMBOT_SLACK_TOKEN = 'xoxb-2154537752-370236158289-KCUWSH6PwnAdIchYEtPuryuc'
DUMBOT_SLACK_ID = 'WAWNYHD4J'

dumbot_slack_client = slackclient.SlackClient(DUMBOT_SLACK_TOKEN)

# GLOBAL VARIABLES
grocery_list = []

# how the bot is mentioned on slack
def get_mention(user):
    return '<@{user}>'.format(user=user)

dumbot_slack_mention = get_mention(DUMBOT_SLACK_ID)


def post_message(message, channel):
    dumbot_slack_client.api_call('chat.postMessage', channel=channel, text=message, as_user=True)


def is_for_me(event):
    """Know if the message is dedicated to me"""
    # check if not my own event
    type = event.get('type')
    if type and type == 'message' and not(event.get('user')==DUMBOT_SLACK_ID):
        # in case it is a private message return true
        if is_private(event):
            return True
        # in case it is not a private message check mention
        text = event.get('text')
        channel = event.get('channel')
        if dumbot_slack_mention in text.strip().split():
            return True


def is_private(event):
    """Checks if private slack channel"""
    return event.get('channel').startswith('D')


# Main function for handling the chats
def handle_message(message, user, channel):
    
    if is_hi(message):
        reply = say_hi(user)
        post_message(message=reply, channel=channel)

    elif is_bye(message):
        reply = say_bye(user)
        post_message(message=reply, channel=channel)

    elif is_list_grocery(message):
        myList = add_to_grocery_list(message, channel)
        if len(myList) > 0:
            post_message(message="Updated List\n{}".format(str(myList)), channel=channel)
        else:
            post_message(message="Error while adding the Item", channel=channel)


def is_hi(message):
    tokens = [word.lower() for word in message.strip().split()]
    return any(g in tokens
               for g in ['hello', 'bonjour', 'hey', 'hi', 'sup', 'ssup', 'morning', 'hola', 'ohai', 'yo'])


def is_bye(message):
    tokens = [word.lower() for word in message.strip().split()]
    return any(g in tokens
               for g in ['bye', 'goodbye', 'revoir', 'adios', 'later', 'cya', 'ttyl'])


def say_hi(user_mention):
    """Say Hi to a user by formatting their mention"""
    response_template = random.choice(['Sup, {mention}...',
                                       'Yo!',
                                       'Hola {mention}',
                                       'Bonjour!'])
    return response_template.format(mention=user_mention)


def say_bye(user_mention):
    """Say Goodbye to a user"""
    response_template = random.choice(['see you later, alligator...',
                                       'adios amigo',
                                       'Bye {mention}!',
                                       'Au revoir!'])
    return response_template.format(mention=user_mention)


def is_list_grocery(message):
    tokens = [word.lower() for word in message.strip().split()]
    for item in tokens:
        if item == 'add':
            return True
    return False


def add_to_grocery_list(message, channel):
    tokens = [word.lower() for word in message.strip().split()]
    for i in range(0, len(tokens)):
        if tokens[i] == 'add' and len(tokens) > 1:
            grocery_list.append(tokens[i+1])
            post_message(message="Item {} was added Successfully".format(tokens[i+1]), channel=channel)
            break
        else:
            post_message(message="You need to mention what to add.\nAnd they call me dumb -_-", channel=channel)
    return grocery_list

def run():
    if dumbot_slack_client.rtm_connect():
        print('[.] dumbot is ON...')
        while True:
            event_list = dumbot_slack_client.rtm_read()
            if len(event_list) > 0:
                for event in event_list:
                    print(event)
                    if is_for_me(event):
                        handle_message(message=event.get('text'), user=event.get('user'), channel=event.get('channel'))
            time.sleep(SOCKET_DELAY)
    else:
        print('[!] Connection to Slack failed.')

if __name__=='__main__':
    run()






