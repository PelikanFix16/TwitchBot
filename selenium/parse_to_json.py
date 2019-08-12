import ast
import json
lines = 0

with open('dict.txt','r') as f:
    lines = f.readlines()

dic = {}


for i in range(len(lines)):
    obj = ast.literal_eval(lines[i])
    dic[str(i)] = json.dumps(obj)

print(dic)

with open('person.json', 'w') as json_file:
  json.dump(dic, json_file)
