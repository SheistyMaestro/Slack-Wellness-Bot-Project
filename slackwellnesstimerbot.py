import slack
import os
import schedule
import time

client=slack.WebClient(token=os.environ['wellnessbot_secretkey'])

def messageMe():
  print ("Ready")
  client.chat_postMessage(channel='#2023-hackathon-team-8',
  text="Test Message")

schedule.every(3).minutes.do(messageMe)
print('Script run test')

while True:
  schedule.run_pending()
  time.sleep(10)