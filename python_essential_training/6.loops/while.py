#!/usr/bin/env python3

secret = 'admin'
password = ''
auth = False
count = 0
max_attemp = 5

while password != secret:
    count += 1
    if count == 3:
        continue
    if count > max_attemp:
        break
    password = input(f"{count}: What's the secret word? ")

else:   # not "else" statement. This "else" executes only if the loop ends normally, not execute there is a break
    auth = True
print('Authorized' if auth else 'Calling the police ...')