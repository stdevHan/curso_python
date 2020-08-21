import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
email_txt = os.path.join(BASE_DIR, 'templates', 'email.txt')

content = ""

with open(email_txt, 'r') as f:
    content = f.read()

print(content.format(name=sys.argv[1]))
