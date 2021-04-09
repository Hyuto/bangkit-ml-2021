#!/usr/bin/env python3
import os, reports, emails
from datetime import datetime

TEXT_PATH = 'supplier-data/descriptions'
PDF_PATH = '/tmp/processed.pdf'

def generate_report(path, title, content):
    reports.generate_report(path, title, '<br/>'.join(content))

def send_email_report():
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    message = emails.generate_email(sender, receiver, subject, body, PDF_PATH)
    emails.send_email(message)

if __name__ == "__main__":
    text_dirs = [(os.path.join(TEXT_PATH, x), x) for x in os.listdir(TEXT_PATH) if '.txt' in x]

    title = 'Processed Update on {}'.format(datetime.now().strftime('%B %d, %Y'))
    summary = []
    for path, name in text_dirs:
        with open(path) as f:
            text = f.read().split('\n')
            temp = 'name: {}<br/>weight: {}'.format(text[0], text[1])
            summary.append(temp)
        f.close()
    generate_report(PDF_PATH, title, summary)

    send_email_report()