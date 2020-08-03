#!/usr/bin/env python3
'''
Print out text messages
'''

sent_messages = []

def send_messages(messages):
    '''Function that prints out the messages and moves lists'''
    while messages:
        message_to_print = messages.pop()
        print(message_to_print)
        sent_messages.append(message_to_print)


messages = ['LOL', 'Call me back', 'Hello!']
send_messages(messages)

print(messages)
print(sent_messages)
