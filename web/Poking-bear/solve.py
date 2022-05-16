import requests

for id in range(351, 777):
    x = requests.get(f'http://chals1.ais3.org:8987/bear/{id}')
    s = x.content
    a = s.find(b"not even")
    if a == -1:
        print(id)
        break
    print("Search id ...", id)



# 499