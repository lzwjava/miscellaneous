with open('resume.txt', 'r') as file:
    lines = file.readlines()

cleaned_lines = [line.lstrip('*')
                 .lstrip('##')
                 .replace('](', ':')
                 .replace('[', '')
                 .replace(')', '') for line in lines]

with open('resume_after.txt', 'w') as file:
    file.writelines(cleaned_lines)
