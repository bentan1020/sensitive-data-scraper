import smtplib
from email.message import EmailMessage
import ssl #adds a layer of security

import os 
from dotenv import load_dotenv

import csv

load_dotenv()

email_sender = "example@gmail.com"
email_password = os.getenv("EMAIL_PASSWORD")

print(email_password)

subject = "Information about your data"
body = """
We are sorry to inform you that your data has been breached. If you are receiving this email, your data will be delete soon.
"""

context = ssl.create_default_context()

def send_email(emailReceiver):
  # parameters: from, to, message
  em = EmailMessage()
  em["From"] = email_sender
  em["To"] = emailReceiver
  em["Subject"] = subject
  em.set_content(body)

  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email_sender, email_password)
    server.sendmail(email_sender, emailReceiver, em.as_string())

# converts csv from firstname, lastname, John, Smith -> into {firstname: John, lastname:Smith}
def dic_list_gen(list1,list2):
  new = []
  for i in list2:
    newDict = {}
    for z in range(len(list1)):
      newDict.update({list1[z]:i[z]})
    new.append(newDict)
  return new

def load_data(filename):
  with open(filename,'r') as f:
    reader = csv.reader(f)
    for row in reader:
      header = row
      break
    data = []
    for row in reader:
      data.append(row)
    retval = dic_list_gen(header,data)
    return retval

csvfile_to_dict = load_data("data.csv")

for dict in csvfile_to_dict:
  if dict["SSN"] != ("None" or "none"):
    print(f"email is sending to {dict['FirstName']}")
    send_email(dict["Email"])
