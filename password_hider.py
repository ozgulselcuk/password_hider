import random
import json
import os
from collections import deque


def characters():
    data = "qwertyuıopğüasdfghjklşizxcvbnmöç1234567890"
    data = data + data.upper()
    dataList = deque(data)
    return dataList


def match_characters():
    dataList = characters()
    copy_dataList = dataList.copy()
    matchList = []
    while (len(dataList) and len(copy_dataList)) != 0 :
        value1 = random.choice(dataList)
        value2 = random.choice(copy_dataList)
        if value1 == value2:
            continue
        match = [value1, value2]
        matchList.append(match)
        dataList.remove(value1)
        copy_dataList.remove(value2)
    return matchList


def key_value():
    matchList = match_characters()
    dicti = {}
    for x in matchList:
        dicti[f'{x[0]}'] = x[1]
    return dicti


def file_control():
    fileLocation = os.getcwd()
    if os.path.exists(fileLocation+"\\"+"passwordİnfo.txt") is True:
        file = open("passwordİnfo.txt", "r", encoding="utf-8")
        fileList = file.readlines()
        newfile = []
        for x in fileList:
            result = json.loads(x)
            if type(result) == dict:
                newfile.append(result)
                continue
            newfile.append(result)
        file.close()
        return newfile
    else:
        fileDicti = key_value()
        newfile = [fileDicti, [], []]
        return newfile


def hider_update(newList):  # updates file when new password is entered
    file = open("passwordİnfo.txt", "w", encoding="utf-8")
    for k in range(0, 3):
        newList[k] = json.dumps(newList[k])
        file.write(newList[k])
        file.write("\n")
    file.close()


def encoder_func(name, password):  # The function encoding the passwords entered.
    fileList = file_control()
    hider = ""
    for x in password:
        hider = hider+fileList[0][x]
    fileList[1].append(name)
    fileList[2].append(hider)
    print(f'{name} password be encoded.')
    print(f'Disguised password = << {hider} >>')
    return hider_update(fileList)


def decoder_func():  # this function decrypts all stored passwords
    fileList = file_control()
    decoder = {}
    for x in fileList[0]:  # dictionary code algorithm
        decoder[fileList[0][x]] = x
    for crypto in fileList[2]:  # hider password list
        solver = ""
        for m in crypto:
            solver = solver+decoder[m]
        print(solver)
