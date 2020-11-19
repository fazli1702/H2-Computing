import csv


with open('NAMES.txt') as f:
    data = f.readlines()
    names = [name.strip() for name in data]


with open('CONTACTS.txt') as f:
    data = f.readlines()
    contacts = [contact.strip().split() for contact in data]


with open('ACCOUNTS.txt') as f:
    data = f.readlines()
    accounts = [account.strip().split(',') for account in data]

with open('ACCOUNTS.txt', 'a') as f:
    f.write('AceOfCoders,YIJC1234\n')
