1. In order to use this, you must disable the safety
measure in your Google account. Here are the steps:
- Open your Google Admin console (admin.google.com).
- Click Security > Basic settings .
- Under Less secure apps, select Go to settings for less secure apps .
- In the subwindow, select the Enforce access to less secure apps for all users radio button. ...
- Click the Save button.

2. You must also enable 2-step-verification on your sender email

notes/challenges:
- Do not name your file "email.py", this interferes with "from email.message import EmailMessage"
- Install dotenv via command line: pip3 install python-dotenv

# Load .env file using:
from dotenv import load_dotenv
load_dotenv()

# Use the variable with:
import os
os.getenv("ACCESS_KEY")