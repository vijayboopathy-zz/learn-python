#!/usr/bin/python3
import random, string, secrets

userInput = input('Characters in password:')

def genPass(userReq):
  password = ''.join(random.choices(string.ascii_letters + string.digits , k=int(userReq)))
  print(password)

genPass(userReq=userInput)


def secPass(userReq):
    password = secrets.token_hex(int(userReq))
    print(password)

secPass(userReq=userInput)
