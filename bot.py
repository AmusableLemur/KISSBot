import re, socket, ssl

from bs4 import BeautifulSoup
from urllib.request import urlopen

class Bot:
    def __init__(self, server, port, nick):
        self.server = server
        self.port = port
        self.nick = nick

    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.server, self.port))
        self.socket = ssl.wrap_socket(s)

        self.write("USER {nick} {nick} {nick} :I am a bot".format(nick = self.nick))
        self.write("NICK " + self.nick)

    def write(self, message):
        message = message + "\n"
        message = message.encode("UTF-8")
        self.socket.send(message)

    def ping(self):
        self.write("PONG :pingis")

    def send(self, message):
        self.write("PRIVMSG " + self.channel + " :" + message)

    def join(self, channel):
        self.write("JOIN " + channel)
        self.channel = channel

    def findtitle(self, link):
        soup = BeautifulSoup(urlopen(link))
        self.send("Title: " + soup.title.string)

    def receive(self):
        message = self.socket.recv(2048).decode("UTF-8")
        message = message.strip("\n\r")

        print(message)

        if message.find("PING :") != -1:
            self.ping()

        if message.find(":die " + self.nick) != -1:
            self.send("Goodbye!")
            sys.exit(0)

        if message.find("http") != -1:
            links = re.findall(r"(https?://\S+)", message)

            for link in links:
                self.findtitle(link)

if __name__ == "__main__":
    bot = Bot("destruktiv.se", 6697, "ircbot")
    bot.connect()
    bot.join("#test")

    while True:
        bot.receive()
