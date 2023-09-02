import os
import requests
v = "0.1"
rawurl = "https://raw.githubusercontent.com/Englishexe/psdb-program-resources/main/"
rawurlv = f"https://raw.githubusercontent.com/Englishexe/psdb-program-resources/main/v{v}/"
dir = os.getcwd()
networking = True
autoupdatedatabases = True
output = True
detailedscan = True
databases = []
def p(text): # Easier way to print and check if output is enabled.
    if output:
        print(text)
def start():
    if "PSDB.settings" not in os.listdir():
        p("PSDB.settings not found, creating one now")
        p(f"Network:\n    Requesting '{rawurlv}PSDB.settings'\n    Downloading to PSDB.settings")
        try:
            file =  requests.get(f"{rawurlv}PSDB.settings")
            f = open("PSDB.settings", "w")
            f.write(file.text)
            f.close()
        except:
            p("    Failed to download, check your network connection or download manually.")
    f = open("PSDB.settings", "r")
    settings = f.read().split(",")
    f.close()
    if settings[0] == "0":
        global networking
        networking = False
    if settings[1] == "0":
        global autoupdatedatabases
        autoupdatedatabases = False
    if settings[2] == "0":
        global output
        output = False
    if settings[3] == "0":
        global detailedscan
        detailedscan = False
    p("Initialized PSDB.settings\nInitializing databases")
    if "databases" not in os.listdir():
        p("'database' directory not found, making one now")
        os.mkdir("databases")
        os.chdir("databases")
        p("Making an example database.")
        p(f"Network:\n    Requesting '{rawurl}exampledatabase.psdb'\n    Downloading to exampledatabase.psdb")
        file =  requests.get(f"{rawurl}exampledatabase.psdb")
        f = open("exampledatabase.psdb", "w")
        f.write(file.text)
        f.close()
        os.chdir("..")
    p("Databases:")
    os.chdir("databases")
    for item in os.listdir():
        if os.path.isfile(item):
            global databases
            databases.append(item)
            p(f"    >{item}")
            if detailedscan:
                f = open(item, "r")
                file = f.read().split(",")
                p(f"        ^Desc:  {file[0]}")
                p(f"        ^Owner: {file[2]}")
            f.close()
        else:
            p(f"    Illegal item in 'databases' ({item})")
    p("Databases scanned")
# --- WARNING ---
# Developer zone - Do not include these functions in your script! They may be removed.

"""
file is the database file name*
description is the database description if empty default to -
types is to enter custom modes for making the database
    -e for an example database (EXA)
    -d for a developer database (DEV)
    -o for an old database (OLD)
    -n for no overwrites (NOO)
owner is the database creator, if empty default to -
v is the version of when it was made*
cv is the current version it is running*

no object nesting 
"""

def databaseinfo():
    None

if __name__ == "__main__": # This code is because I keep running it 0_0
    print("This program must be imported") # , or install our database manager
