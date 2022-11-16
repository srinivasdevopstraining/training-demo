import requests 
import os 
import date 

print('This is the sameple python file')

response = requests.get('user_urs', auth=('username', 'password'))

print(response)

print('To give the xample of stash apply')

print('some text')
print('Added this line to test the merge')
