# NOT COMPLETE DO NOT USE
"""
Python Simple DataBase - PSDB
Copyright (C) 2023 Englishexe

Made by Englishexe
Started development: 01/09/23
Version 1.0.0: --/--/--

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
networking,autoupdatedatabases,output,detailedScan

Debug:({v}|{len(databases)}|{networking}|{autoupdatedatabases}|{output}|{detailedScan})

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
import sys
v = "0.1.2-alpha" # Editing this version will break networking and much more.
rawurl = "https://raw.githubusercontent.com/Englishexe/psdb-program-resources/main/"
dir = os.getcwd()
networking = True
autoupdatedatabases = True
output = True
detailedScan = True
databases = []
started = False
def psdbp(prefix, text): # Easier way to print and check if output is enabled.
    """
    Do not use
    """
    if output:
        print(f"[{prefix}] {text}")
    None
def start():
    """
    Initialise PSDB, no arguments are needed.
    """
    psdbp("    ", "Python Simple DataBase - PSDB\n[    ] Copyright (C) 2023 Englishexe\n[    ] GPL-3.0 License")
    psdbp("INFO", "Initializing databases")
    if "databases" not in os.listdir():
        psdbp("WARN", "'database' directory not found, making one now")
        os.mkdir("databases")
        os.chdir("databases")
        psdbp("INFO", "Making an example database.")
        psdbp("NETW", f"Network:\n[    ]     Requesting '{rawurl}exampledatabase.psdb'\n[    ]     Downloading to databases\exampledatabase.psdb")
        file =  requests.get(f"{rawurl}exampledatabase.psdb")
        f = open("exampledatabase.psdb", "w")
        f.write(file.text)
        f.close()
        os.chdir("..")
    psdbp("INFO", "Databases:")
    os.chdir("databases")
    for item in os.listdir():
        if os.path.isfile(item):
            if ".psdb" in item:
                global databases
                databases.append(item)
                psdbp(" ^^ ", f"    >{item}")
                if detailedScan:
                    f = open(item, "r")
                    file = f.read().split(",")
                    psdbp(" ^^ ", f"        ^Desc : {file[0]}")
                    psdbp(" ^^ ", f"        ^Owner: {file[2]}")
                    psdbp(" ^^ ", f"        ^Type : {file[1]}")
                    f.close()
            else:
                psdbp("WARN", f"    Illegal item in 'databases' ({item})")
        else:

            psdbp("WARN", f"    Illegal item in 'databases' ({item})")
    os.chdir("..")
    psdbp("INFO", "Initialized databases")
    psdbp("INFO", "Initializing version")
    if networking:
        # https://raw.githubusercontent.com/Englishexe/psdb-program-resources/main/versions/lastestversion
        global latestversion
        latestversion = f"{rawurl}versions/lastestversion"
        global latestdeveloper
        latestdeveloper = f"{rawurl}versions/latestdeveloper"
        global lateststable
        lateststable = f"{rawurl}versions/lateststable"
        psdbp("NETW", f"Requesting version information x3")
        psdbp("    ", f"    Requesting: {latestversion}")
        latestversion = requests.get(latestversion)
        latestversion = latestversion.text.strip()
        psdbp("    ", f"    Requesting: {latestdeveloper}")
        latestdeveloper = requests.get(latestdeveloper)
        latestdeveloper = latestdeveloper.text.strip()
        psdbp("    ", f"    Requesting: {lateststable}")
        lateststable = requests.get(lateststable)
        lateststable = lateststable.text.strip()
        psdbp("INFO", f"Version Information:")
        psdbp("    ", f"    Latest Stable Version: {lateststable} (Last patch)")
        psdbp("    ", f"    Latest Version: {latestversion} (Last major update)")
        psdbp("    ", f"    Latest Developer Version: {latestdeveloper} (Last push to github)")
        psdbp("    ", f"    Your Version: {v}")
        if v == lateststable:
            psdbp("GOOD", f"You are running the lastest stable version ({lateststable})")
        elif v == latestversion:
            psdbp("INFO", f"You are running the last major release, it is suggested you update to the last patch Your version: ({v}) - Last stable version: ({lateststable})")
        elif v == latestdeveloper:
            psdbp("WARN", f"You are running the last push to GitHub, this is not suggested. Your version: ({v}) - Last stable version: ({lateststable})")
        else:
            psdbp("FAIL", f"Could not determine version. Your version: ({v})")

    psdbp("GOOD", f"Initialized PSDB V{v}")
    psdbp("DEBU", f"Debug:({v}|{len(databases)}|{networking}|{autoupdatedatabases}|{output}|{detailedScan})")
    global started
    started = True
def createdb():
    """
    Not in use
    """
    if not started:
        psdbp("FAIL", "Action denied\nplease initalize PSDB with pythondatabase.start()")
        return False
def removedb():
    """
    Not in use
    """
    if not started:
        psdbp("FAIL", "Action denied\nplease initalize PSDB with pythondatabase.start()")
        return False
def readdb():
    """
    Not in use
    """
    if not started:
        psdbp("FAIL", "Action denied\nplease initalize PSDB with pythondatabase.start()")
        return False
def flagdb():
    """
    Not in use
    """
    if not started:
        psdbp("FAIL", "Action denied\nplease initalize PSDB with pythondatabase.start()")
        return False
def illegal():
    """
    Not in use
    """
    if not started:
        psdbp("FAIL", "Action denied\nplease initalize PSDB with pythondatabase.start()")
        return False
def settings(set0, set1, set2, set3):
    """
    0 - Networking\n
    1 - Auto Update Databases\n
    2 - Output\n
    3 - Detailed Scan\n
    Accepts True / False, 4 arguments required
    """
    if not set0:
        global networking
        networking = False
    if not set1:
        global autoupdatedatabases
        autoupdatedatabases = False
    if not set2:
        global output
        output = False
    if not set3:
        global detailedScan
        detailedScan = False
# --- WARNING ---
# Developer zone - Do not include these functions in your program, they will be removed later.
def debug():
    """
    Developer tool - DO NOT USE - (Prints debug info)
    """
    print(f"{len(databases)}{networking}{autoupdatedatabases}{output}{detailedScan}")
if __name__ == "__main__":
    print("This program must be imported. As this is an ALPHA build main.py will be started.")
    os.system("python main.py")
