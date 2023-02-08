messages = ["Hey there!", "What's up?", "How are you?", "Good to see you!"]
sent_messages = []

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

send_messages(messages)

print(messages)
print(sent_messages)