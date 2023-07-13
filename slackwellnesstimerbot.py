#For proper function, make sure pip is enabled during Python install otherwise uninstall/reinstall with it enabled
#Before running, open a desktop command/terminal prompt and run several pip commands
#pip install slackclient
#pip install schedule
#pip install dotenv

import slack
import os
import schedule
import time

from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client=slack.WebClient(token=os.environ['SLACK_TOKEN'])

def messageMe():
  print ("Ready")
  client.chat_postMessage(channel='#2023-hackathon-team-8',
  text="Test Message")

schedule.every(3).minutes.do(messageMe)
print('Script run test')

while True:
  schedule.run_pending()
  time.sleep(10)