import csv

html_output = ''
names = []

with open('patrons.csv','r') as patrons_file:
    csv_read = csv.DictReader(patrons_file)

    #dropping the first of bad rows since we do not need this dat
    next(csv_read)

    for line in csv_read:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'
html_output += '/n<ul>'
for name in names:
    html_output += f'/n/t<li>{name}</li>'

html_output += '/n<ul>'
print(html_output)