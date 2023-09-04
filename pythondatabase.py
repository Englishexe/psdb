# NOT COMPLETE DO NOT USE
"""
Made by Englishexe
Started development: 01/09/23
Version 1: --/--/--

<----------------------------------------->

Developer notes:

<------>
database description,type1/type2/type3,owner,v,cv,
{object_name
varible_name varible_value
}
<------>

description is the database description if empty default to "-"
types will be renamed to flags
types is to enter custom modes for making the database
    -e for an example database (EXA) - Not used
    -d for a developer database (DEV) - Not used
    -o for an old database (OLD) - Not used
    -n for no overwrites (NOO) - Do not allow overwrites
    -p protected database - Make deletion harder
owner is the database creator, if empty default to "-"
v is the version of when it was made*
cv is the current version it is running*



PSDB.settings
networking,autoupdatedatabases,output,detailedscan

Debug:({v}|{len(databases)}|{networking}|{autoupdatedatabases}|{output}|{detailedscan})

<----------------------------------------->

Preformance:

12,000 11kb (144mb) databases takes
settings - time
1,1,1,1 - 2m 47s
1,1,0,1 - 9s
1,1,1,0 - 6s
1,1,0,0 - ^s
"""
import os
import requests
v = "0.1" # Editing this version will break networking and much more.
gv = "https://raw.githubusercontent.com/Englishexe/versions/main/pythonsimpledatabase"
rawurl = "https://raw.githubusercontent.com/Englishexe/psdb-program-resources/main/"
rawurlv = f"https://raw.githubusercontent.com/Englishexe/psdb-program-resources/main/v{v}/"
rawlegalurl = "https://raw.githubusercontent.com/Englishexe/psdb/main/LICENSE"
dir = os.getcwd()
networking = True
autoupdatedatabases = True
output = True
detailedscan = True
databases = []
started = False
if v < 1:
    print("Warning, you are running a APLHA version.")
def license():
    p("""X-------------------------------------------------------------------------------X
|                         Python Simple DataBase - PSDB                         |
|                         Copyright (C) 2023 Englishexe                         |
|                                                                               |
|     This program is free software: you can redistribute it and/or modify      |
|     it under the terms of the GNU General Public License as published by      |
|     the Free Software Foundation, either version 3 of the License, or         |
|     (at your option) any later version.                                       |
|                                                                               |
|     This program is distributed in the hope that it will be useful,           |
|     but WITHOUT ANY WARRANTY; without even the implied warranty of            |
|     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             |
|     GNU General Public License for more details.                              |
|                                                                               |
|     You should have received a copy of the GNU General Public License         |
|                                                                               |
|    along with this program.  If not, see https://www.gnu.org/licenses/.       |
x-------------------------------------------------------------------------------x""")
def tc():
    p(f"Please visit the LICENSE here:\n{rawlegalurl}")
def p(text): # Easier way to print and check if output is enabled.
    """
    May not work as intended, used throughout the module to print.
    Do not include this in your program, it may be removed at a future date
    (Checks if output is enabled in PSDB.settings if yes it will print the provided text.)
    """
    if output:
        print(text)
def start():
    """
    Initialise PSDB, no arguments are needed.
    """
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
    if not output:
        print("PSDB - Output is disabled, make sure you read the legal T&Cs & Documenation before using.")
    p("Initialized PSDB.settings\nInitializing legal")
    license()
    tc()
    p("Initialized legal\nInitializing databases")
    if "databases" not in os.listdir():
        p("'database' directory not found, making one now")
        os.mkdir("databases")
        os.chdir("databases")
        p("Making an example database.")
        p(f"Network:\n    Requesting '{rawurl}exampledatabase.psdb'\n    Downloading to databases\exampledatabase.psdb")
        file =  requests.get(f"{rawurl}exampledatabase.psdb")
        f = open("exampledatabase.psdb", "w")
        f.write(file.text)
        f.close()
        os.chdir("..")
    p("Databases:")
    os.chdir("databases")
    for item in os.listdir():
        if os.path.isfile(item):
            if ".psdb" in item:
                global databases
                databases.append(item)
                p(f"    >{item}")
                if detailedscan:
                    f = open(item, "r")
                    file = f.read().split(",")
                    p(f"        ^Desc : {file[0]}")
                    p(f"        ^Owner: {file[2]}")
                    p(f"        ^Type : {file[1]}")
                f.close()
            else:
                p(f"    Illegal item in 'databases' ({item})")
        else:

            p(f"    Illegal item in 'databases' ({item})")
    os.chdir("..")
    p("Initialized databases")
    p("Initializing version")
    if networking:
        global gv
        gv = requests.get(gv)
        gv = gv.text.strip()
        if v == gv:
            p("PSDB up to date")
        else:
            if gv > v:
                p("Newer version of PSDB available, please update.")
    p(f"Initialized PSDB V{v}\nDebug:({v}|{len(databases)}|{networking}|{autoupdatedatabases}|{output}|{detailedscan})")
    global started
    started = True
def createdb():
    """
    Not in use
    """
    if not started:
        p("Action denied\nplease initalize PSDB with pythondatabase.start()")
        return False
def removedb():
    """
    Not in use
    """
    if not started:
        p("Action denied\nplease initalize PSDB with pythondatabase.start()")
        return False
def readdb():
    """
    Not in use
    """
    if not started:
        p("Action denied\nplease initalize PSDB with pythondatabase.start()")
        return False
def flagdb():
    """
    Not in use
    """
    if not started:
        p("Action denied\nplease initalize PSDB with pythondatabase.start()")
        return False
def illegal():
    """
    Not in use
    """
    if not started:
        p("Action denied\nplease initalize PSDB with pythondatabase.start()")
        return False
def settings(set0, set1, set2, set3):
    """
    0 - Networking\n
    1 - Auto Update Databases\n
    2 - Output\n
    3 - Detailed Scan\n
    Accepts True / False, 4 arguments required
    """
    f = open("PSDB.settings", "w")
    if set0:
        f.write("1")
    else:
        f.write("0")
    f.write(",")
    if set1:
        f.write("1")
    else:
        f.write("0")
    f.write(",")
    if set2:
        f.write("1")
    else:
        f.write("0")
    f.write(",")
    if set3:
        f.write("1")
    else:
        f.write("0")
# --- WARNING ---
# Developer zone - Do not include these functions in your program, they will be removed later.
def debug():
    """
    Developer tool - DO NOT USE - (Prints debug info)
    """
    print(f"{len(databases)}{networking}{autoupdatedatabases}{output}{detailedscan}")
if __name__ == "__main__": # This code is because I keep running the module not main script. 0_0
    print("This program must be imported") # , or install our database manager
