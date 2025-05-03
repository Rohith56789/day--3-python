import re

text ='Conatct me at dev@rx.live.com or admin@rx.org'
pattern = r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'

emails = re.findall(pattern, text)
print("Email addresses found:", emails)