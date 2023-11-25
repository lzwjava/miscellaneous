import re

with open('code.txt', 'r') as file:
    code = file.read()

# Find and remove all multiline comments
cleaned_code = re.sub(r'(?:^|\n)\s*""".*?"""', '', code, flags=re.DOTALL)

cleaned_code = re.sub(r'#.*', '', cleaned_code)

# Write cleaned code to new file
with open('cleaned_code.txt', 'w') as file:
    file.write(cleaned_code)
