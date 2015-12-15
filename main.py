import serial # if you have not already done so
import time
import json
import twitter #using python-twitter library
import re
import serial.tools.list_ports

class Politician(object):
    name = ""
    screen_name = ""
    statuses = []
    processed_tweets = 0
    terror_count = 0
    terrorism_count = 0
    terrorist_count = 0

    def __init__(self, name, screen_name):
        self.name = name
        self.screen_name = screen_name
        self.statuses = []
        self.processed_tweets = 0;
        self.terror_count = 0
        self.terrorist_count = 0
        self.terrorism_count = 0

    def setTerrorCount(self, count):
        self.terror_count = count

    def increaseTerrorCount(self, amount):
        self.terror_count = self.terror_count + amount

    def setTerrorismCount(self, count):
        self.terrorism_count = count

    def increaseTerrorismCount(self, amount):
        self.terrorism_count = self.terrorist_count + amount

    def setTerroristCount(self, count):
        self.terrorist_count = count

    def increaseTerroristCount(self, amount):
        self.terrorist_count = self.terrorist_count + amount

    def setStatuses(self, statuses):
        self.statuses = statuses

    def findWholeWord(self,w,str):
        exactMatch = re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE)
        matches= len(exactMatch.findall(str))
        if(matches is None):
            matches = 0
        print(self.name+" had "+matches.__str__()+" for "+w+" found in tweet: "+str)
        return matches

    def countStatus(self):
        for s in self.statuses:
            print s.text
            self.processed_tweets+=1;
            self.increaseTerrorCount(self.findWholeWord('terror', s.text))
            self.increaseTerroristCount(self.findWholeWord('terrorist', s.text))
            self.increaseTerrorismCount(self.findWholeWord('terrorism', s.text))
        # Once all statuses for a user are processed add them to the average counters then send over serial



starttime=time.time()
print(list(serial.tools.list_ports.comports()))

#[('COM4', 'Arduino Uno (COM4)', 'USB VID:PID=2341:0043 SNR=5533330393435121A151')]

#api = twitter.Api(consumer_key='',
#                  consumer_secret='',
 #                 access_token_key='',
  #                access_token_secret='')

print api.VerifyCredentials()

s = serial.Serial('COM4', 9600, timeout=5)

donald = Politician("Donald Trump", "realDonaldTrump")
marco = Politician("Marco Rubio","marcorubio")
lindsey = Politician("Lindsey Graham", "LindseyGrahamSC")
ben = Politician("Ben Carson", "RealBenCarson")


# Twitter is rate limited for searches at 180 Queries per 15 mins

while True:
    print("Refreshing Twitter Statuses")
    donald.statuses = api.GetUserTimeline(screen_name=donald.screen_name)
    donald.countStatus()
    s.open()
    s.write("Trump (Terror): "+(donald.terror_count/donald.processed_tweets))
    time.sleep(10)
    s.write("Trump (Terrorist): "+(donald.terrorist_count/donald.processed_tweets))
    time.sleep(10)
    s.write("Trump (Terrorism): "+(donald.terrorism_count/donald.processed_tweets))
    s.close()
    time.sleep(60);

    marco.statuses = api.GetUserTimeline(screen_name=marco.screen_name)
    marco.countStatus()

    lindsey.statuses = api.GetUserTimeline(screen_name=lindsey.screen_name)
    lindsey.countStatus()

    ben.statuses = api.GetUserTimeline(screen_name=ben.screen_name)
    ben.countStatus()

    print("Sleeping")
    time.sleep(600.0 - ((time.time() - starttime) % 600.0))






