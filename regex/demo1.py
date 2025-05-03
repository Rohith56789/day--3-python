import re

pattern = r"(\d{3})-(\d{3})-(\d{4})"
text = "Rohith SSN id is 123-456-7890 and backup is 987-654-3210"

matches = re.finditer(pattern, text)

for match in matches:
    print("Match found:", match.group())
