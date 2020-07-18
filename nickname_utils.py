import os
from dotenv import load_dotenv
import json

load_dotenv()
filename = os.getenv('NICKFILEPATH')

def loadnicks():
    return json.loads(open(filename,"r").read())

def writenicks(namedict):
    open(filename,"w+").write(json.dumps(namedict))

def addnick(namedict, mainname, nick):
    #adds nickname to runtime dict, also writes to dict file...
    #returns false if the mainname is NOT in the nickname file(aka spelled wrong or we need to add mainname...)
    if mainname not in namedict.keys():
        return False
    namedict[mainname].append(nick)
    writenicks(namedict)
    return True

def addmaintonick(namedict, mainname): #call this to add mainname to nickname dict, and then do addnick to add in nickname
    if mainname in namedict.keys():
        return False #we cant overrwite an existing mainname list...
    namedict[mainname] = []
    writenicks(namedict)
    return True

def removenick(namedict, mainname, nick):
    if mainname not in namedict.keys():
        return False #cant remove if mainname doesnt exist
    if nick not in namedict[mainname]:
        return False #cant remove if nick doesnt exist in mainname list
    namedict[mainname].remove(nick)
    writenicks(namedict)
    return True
    

def getnicks(namedict, mainname): # TODO need to make sure we check if NONE is returned........
    #returns a list of nicks associated with mainname, or NONE if mainname DNE
    if mainname not in namedict.keys():
        return None
    return namedict[mainname]