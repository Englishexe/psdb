"""
Python Simple DataBase - PSDB
Copyright (C) 2023 Englishexe
GPL-3.0 License

Programmed by Englishexe
Logo design by Commander
Started development: 01/09/23
Version 1.0.0: --/--/--

Main repository: https://github.com/Englishexe/psdb/
Resource repository: https://github.com/Englishexe/psdb-program-resources/
Refer to the main GitHub repository for the legal agreement, documentation and more.
"""
try:
    import os
    import requests
    import time
except:
    print("[PSDB] Error 1")
    print("[PSDB] DUMP: False")
    exit()
v = "0.1.4-alpha"
rawurl = "https://raw.githubusercontent.com/Englishexe/psdb-program-resources/main/"
HideNetworking = True
output = True
databases = []
started = False
debug = False
maindir = os.getcwd()
def error(num):
    """
    Arguments: 1(int)\n
    Description: When used an error is raised (PSDB error) and DUMP text is printed\n
    In API docs? False
    """
    num = str(num)
    print(f"Error #{num}")
    print(f"[PSDB] DUMP: Advanced error information: \n~{v}'{rawurl}'{HideNetworking}{output}{len(databases)}{databases}{started}{debug}'{maindir}''{os.getcwd()}'#{num}-{time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}-{time.localtime().tm_mday}/{time.localtime().tm_mon}/{time.localtime().tm_year}-'{requests.get('https://www.google.com').status_code}'~")
def psdbp(text): 
    """
    Arguments: 1(str)\n
    Description: If output is enabled the inputted text is printed\n
    In API docs? True
    """
    if output:
        print(f"[PSDB] {text}")
def psdbd(text):
    """
    Arguments: 1(str)\n
    Description: If output is enabled argument0 (string) is printed\n
    In API docs? True
    """
    if output:
        if debug:
            print(f"[>>>>] {text}")
def psdbnet(url):
    """
    Arguments: 1(str)\n
    Description: Requests the given URL and returns the raw text provided.\n
    In API docs? True
    """
    if not HideNetworking:
        psdbp(f"Requesting '{url}'")
    try:
        result = requests.get(url)
    except:
        error(5)
        return "Network failed see error above"
    if result.status_code != 200:
        error(2)
    result = result.text
    return result
def setdebug(value):
    """
    Arguments: 1(bool)\n
    Description: If True is passed in debug is enabled anything else it is disabled\n
    In API docs? True
    """
    global debug
    if value == True:
        debug = True
    else:
        debug = False
def scandatabases():
    """
    Arguments: 0\n
    Description: Scans the database folder and loads databases into memory\n
    In API docs? True
    """
    os.chdir(maindir)
    try:
        os.chdir("databases")
    except:
        error(3)
        exit()
    global databases
    databases = []
    for item in os.listdir():
        if os.path.isfile(item):
            if ".psdb" in item:
                item = item.removesuffix(".psdb")
                databases.append(item)
    os.chdir("..")
def createdb(name, creator):
    """
    Arguments: 2(str, str)\n
    Description: Creates a database, make sure to scandatabases after\n
    In API docs? True
    """
    if not started:
        error(4)
        return False
    os.chdir(maindir)
    os.chdir("databases")
    f = open(f"{name}.psdb", "w")
    for item in database:
        if item == "^^DBDESC^^,":
            index = database.index("^^DBDESC^^,")
            database.pop(index)
            database.insert(index, f"{name} database,")
        if item == "^^TYPES^^,":
            index = database.index("^^TYPES^^,")
            database.pop(index)
            database.insert(index, f",")
        if item == "^^CRE^^,":
            index = database.index("^^CRE^^,")
            database.pop(index)
            database.insert(index, f"{creator},")
        if item == "^^V^^,":
            index = database.index("^^V^^,")
            database.pop(index)
            database.insert(index, f"{v},")
        if item == "^^CV^^,":
            index = database.index("^^CV^^,")
            database.pop(index)
            database.insert(index, f"{v},")
    databasecontent = ""
    for item in database:
        databasecontent = f"{databasecontent}{item}"
    f.write(databasecontent)
    f.close()
    psdbp(f"Wrote database ({name}.psdb)")
    os.chdir("..")
def delete(name):
    """
    Arguments: 1(str)\n
    Description: Deletes a database\n
    In API docs? True
    """
    if not started:
        error(4)
        return False
    if name in databases:
        psdbp("Name is in databases")
def start():
    """
    Arguments: 0\n
    Description: Starts PSDB\n
    In API docs? True
    """
    psdbp("Python Simple DataBase - PSDB")
    psdbp("Copyright (C) 2023 Englishexe")
    psdbp("GPL-3.0 License")
    psdbp("Initializing PSDB")
    global maindir
    maindir = os.getcwd()
    if "databases" not in os.listdir():
        os.mkdir("databases")
    scandatabases()
    psdbcheckversion()
    global database
    database = psdbnet(f"{rawurl}templatedatabase").split("|")
    psdbp(f"Initialized PSDB (v{v})")
    global started
    started = True
def settings(set0, set1):
    """
    0 - HideNetworking\n
    1 - Output\n
    Accepts True / False, 4 (3 if from 0) arguments required
    """
    if not set0:
        global HideNetworking
        HideNetworking = False
    if not set1:
        global output
        output = False
def psdbcheckversion():
    """
    Arguments: 0\n
    Description: Returns PSDB version and checks for new versions\n
    In API docs? True
    """
    global latestdeveloper
    latestdeveloper = f"{rawurl}versions/latestdeveloper" # Last push to GH (push no release)
    global lateststable
    lateststable = f"{rawurl}versions/lateststable" # Last patch on GH (release)
    latestdeveloper = psdbnet(latestdeveloper)
    lateststable = psdbnet(lateststable)
    if v == lateststable:
        psdbp(f"PSDB is running the latest stable version (Current:{v})->(Last:{lateststable})")
    elif v == latestdeveloper:
        psdbp(f"PSDB is running a test version, this may cause data loss, unexpected behaviour and bugs. (Current:{v})->(Last:{lateststable})")
    else:
        psdbp(f"PSDB is out of date. (Current:{v})->(Last:{lateststable})")
    return v

if __name__ == "__main__":
    print("[PSDB] Executed incorrectly.")
    f = open("PSDBExecution.py", "w")
    f.write(requests.get(f"{rawurl}PSDBExecution.py").text)
    f.close()
    try:
        os.system("python PSDBExecution.py")
    except:
        error(0)
    exit()