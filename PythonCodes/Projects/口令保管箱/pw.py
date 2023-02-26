#! python3

import sys 
import pyperclip

PASSWORDS = {
    'email':'2453748904',
    'blog':'gledfish.netlify.com',
    'luggage':'123456'}

if len(sys.argv) < 2:
    print('error')
    exit()
account = sys.argv[1] # 账户名
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('account password copied successfully')
else:
    print("account password not copied successfully")