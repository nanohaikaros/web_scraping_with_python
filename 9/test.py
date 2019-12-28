import requests

session = requests.Session()

params = {'username': 'Ryan', 'password': 'password'}
# r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', params)
s = session.post('http://pythonscraping.com/pages/cookies/welcome.php', params)
print('Cookie is set to:')
# print(r.cookies.get_dict())
print(s.cookies.get_dict())
print('---------------')
print("Going to profile page...")
# r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
# print(r.text)
s = session.get('http://pythonscraping.com/pages/cookies/profile.php')
print(s.text)