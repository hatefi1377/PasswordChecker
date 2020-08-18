import requests
import hashlib
import sys

def request_be_stie (searched_word):
    url = "https://api.pwnedpasswords.com/range/" + searched_word
    req = requests.get(url)
    if req.status_code != 200:
        raise RuntimeError(f'Error fetching : {req.status_code}, check the api thanks!')
    return req

def get_my_password (hashes , hash_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes :
        if h == hash_check :
            return count
    return 0


def check_my_pass (password) :
    sha1tras = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    panjtash = sha1tras[:5]
    baghyash = sha1tras[5:]
    response = request_be_stie(panjtash)
    return get_my_password(response,baghyash)



print("You can give me as many password as you want by putting space between them.")
passwords = input("Here you can give me : ")
passwordclean = (passwords.split(' '))
for item in passwordclean :
    count = check_my_pass(item)
    if count:
        print(f'{item} was found {count} times ... You have to change it.')
    else :
        print("Yeah your password looks fine")