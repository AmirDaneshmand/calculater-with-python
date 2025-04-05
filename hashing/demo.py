import bcrypt

password = b"thisismypassword"
salt = b"ssq83hc"
hashpass = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashpass)

entered = input()
entered = entered.encode()

if bcrypt.checkpw(entered, hashpass):
    print('ok')   