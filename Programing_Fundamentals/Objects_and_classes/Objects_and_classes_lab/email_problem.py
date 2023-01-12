class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


e_mails = []
command = input()
while True:
    if command == "Stop":
        break
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    e_mails.append(email)
    command = input()

send_email = [e_mails[int(x)].send() for x in input().split(", ")]
for mail in e_mails:
    print(mail.get_info())
