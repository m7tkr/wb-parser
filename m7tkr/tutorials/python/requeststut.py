import requests

# r = requests.get('https://imgs.xkcd.com/comics/krypton.png')

# print(r.content)
# print(r.status_code)
# print(r.ok)  # True for everything less than 400
# pritn(r.headers)

# with open('./filedir/xkcd1.png', 'wb') as f:
#     f.write(r.content)

# ---------------------
# payload = {'page': 25, 'count': 2}
# r = requests.get('https://httpbin.org/get', params=payload)

payload = {'username': 'mhmmd', 'password': 'notspecify'}
r = requests.post('https://httpbin.org/post', data=payload)

# print(r.json)

r_dict = r.json()
print(r_dict)
