import requests

url_base = "https://api.clashofclans.com/v1/players/%23"

headers = {
    'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjAyZjdhOTQ1LTkzMDEtNGMwZi1iYzdiLTM4NThiMGRjZjAxOCIsImlhdCI6MTY0MzU1NjM3OCwic3ViIjoiZGV2ZWxvcGVyLzgwZWFlY2JhLWVjNTYtODA1OC00NzA3LWMwZWVlMjAxNmFkOCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjM2LjIuMTY3LjU2Il0sInR5cGUiOiJjbGllbnQifV19.0jpnfXBJNN9pPA-dEf3BzqG-fS_F5iH5sHuMoXMG_9YifdIoiQqRpbx50PpZn2-H0PsCWyEBw2ZyYyt7tQEcsQ',
    'Accept':'application/json'
}


PlayerListA = ['299J0L22U', 'Q99UL2CR', '9PYLUG0J']
PlayerListB = ['2JVYRCJC', 'YRQGQLPV', '22PLULRL0']
PlayerListC = ['9RCLGPYL8', 'YU8V0JYJ', '2YYG89RY2']
PlayerListD = ['28GGLG28C', 'J2JLJPJV', '82CVYGYJ0']
PlayerListE = ['PPVYC88R', 'P9RL20YYC', 'LRYGVGLLU']
PlayerListF = ['RGV0J022', 'JGPYRPUQ', '29R90LULL']
PlayerListG = ['Y8QPRGC0C', 'QU2UVQ9R', 'G2L8R8QY']
PlayerListH = ['222UCUQLV', '22GR80Q8R', 'PV9RQ0J2']


print()
print("チームA")
for PlayerA in PlayerListA:
    response = requests.get(
    url_base + PlayerA, headers=headers)
    user_json = response.json()
    print(user_json['trophies'], user_json['bestTrophies'], user_json['name'])

print()
print("チームB")
for PlayerB in PlayerListB:
    response = requests.get(
    url_base + PlayerB, headers=headers)
    user_json = response.json()
    print(user_json['trophies'], user_json['bestTrophies'], user_json['name'])

print()
print("チームC")
for PlayerC in PlayerListC:
    response = requests.get(
    url_base + PlayerC, headers=headers)
    user_json = response.json()
    print(user_json['trophies'], user_json['bestTrophies'], user_json['name'])

print()
print("チームD")
for PlayerD in PlayerListD:
    response = requests.get(
    url_base + PlayerD, headers=headers)
    user_json = response.json()
    print(user_json['trophies'], user_json['bestTrophies'], user_json['name'])

print()
print("チームE")
for PlayerE in PlayerListE:
    response = requests.get(
    url_base + PlayerE, headers=headers)
    user_json = response.json()
    print(user_json['trophies'], user_json['bestTrophies'], user_json['name'])

print()
print("チームF")
for PlayerF in PlayerListF:
    response = requests.get(
    url_base + PlayerF, headers=headers)
    user_json = response.json()
    print(user_json['trophies'], user_json['bestTrophies'], user_json['name'])

print()
print("チームG")
for PlayerG in PlayerListG:
    response = requests.get(
    url_base + PlayerG, headers=headers)
    user_json = response.json()
    print(user_json['trophies'], user_json['bestTrophies'], user_json['name'])

print()
print("チームH")
for PlayerH in PlayerListH:
    response = requests.get(
    url_base + PlayerH, headers=headers)
    user_json = response.json()
    print(user_json['trophies'], user_json['bestTrophies'], user_json['name'])
