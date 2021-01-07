import csv
import json

compromised_users = []

#  write a program that will read in the compromised usernames and passwords that are stored in a file called 'passwords.csv'
with open('passwords.csv', newline='') as password_file:
  password_csv =  csv.DictReader(password_file)

  for password_row in password_csv:
    compromised_users.append(password_row['Username'])

print(compromised_users)



with open('compromised_users.txt', 'w') as compromised_user_file:
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user)

# json
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {"recipient":"The Boss",
     "recipient" : "Mission Success"}
  json.dump(boss_message_dict, boss_message)

# remove the 'passwords.csv' completely
with open('new_passwords.csv', 'w') as new_passwords_obj:

  slash_null_sig = """
  / )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  new_passwords_obj.write(slash_null_sig)

