import json

adrs = input('tests.json address ')
adrs2 = input('values.json address ')

with open(adrs) as f:
  tests = json.load(f)
with open(adrs2) as g:
  values = json.load(g)

val = values['values']
test = tests['tests']

print()
newdict = {}
for i in val:
  newdict[i['id']] = i['value']

def recurs(dict):
  
  try:
    for i in dict['values']:
      recurs(i)
      i['value'] = newdict[i['id']]
  except KeyError:
    print(end = '')


for i in test:
  try:
    i['value'] = newdict[i['id']]
  except KeyError:
    print()
  recurs(i)

report = json.dumps(dict(tests = test))
print(report)

with open ('report.json', 'w') as newfile:
  newfile.write(report)
