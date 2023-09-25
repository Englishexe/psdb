<p align="center">
  <img src="https://raw.githubusercontent.com/Englishexe/psdb-program-resources/main/brand/psdb.png" />
</p>

# FIND ALL DOCUMENTATION ON THE [WIKI](https://github.com/Englishexe/psdb/wiki/_Home)
This documentation is out of date and has non-existing functions
# Python Simple Database <small><small><small>(PSDB)</small></small></small> Documentation
### **Contents:**
- [PSDB Info](#psdb-info)
- [Documentation](#documentation)
    - [1. The Basics](#1-the-basics)
        - [Preformance](#preformance)
        - [Modules](#modules)
        - [Database Layout](#database-layout)
    - [2. Using PSDB](#2-using-psdb)
    - [3. Customising PSDB](#3-customising-psdb)
    - [4. Creating Deleting and Changing Databases](#4-creating-deleting-and-changing-databases)
    - [Debugging & Error Codes](#0-debugging--error-codes)
        - [Error Table](#error-table)
        - [Dump Table](#dump-table)
- [Contact me](#contact-me)
- [Change log](#change-log)
- [More](#more)
    - [Future Updates](#future-updates)
    - [Link Placeholder](#sorry)
    - [About me](#about-me)
    - [CLT](#clt)
- [Legal](#legal)
    - [PSDB Legal](#psdb-legal)
    - [License / Copyright](#license)

⚠️ WARNING ⚠️\
This is moving the the [PSDB Wiki](https://github.com/Englishexe/psdb/wiki)

## PSDB Info
Python Simple Database is a Python module that allows data to be stored safely without complication, it requires no knowledge except basic Python skills. PSDB does all the heavy lifting for the programmer while keeping it human-readable. PSDB allows for customisation such as 'detailed scan' and 'output', these allow developers to choose what they see or what the end-user sees. PSDB is good for beginners or small projects as it has a very simple syntax and output. For more information refer to the [documentation](#documentation) or [Contact Me](#contact-me)
## Documentation
[1](#1-the-basics) **|** [2](#2-using-psdb) **|** [3](#3-customising-psdb) **|** [4](#4-creating-deleting-and-changing-databases) **|** [placeholder](#0-debugging--error-codes)
### 1. The Basics
In this chapter you can find the basic information about PSDB, even if you are an experienced Python developer reading this can help a lot.
#### <u>Preformance:</u>
Info: 10,000 databases running v0.1.4-alpha.6\
Startup: 1s\
Create: 30s
#### <u>Modules:</u>
Modules with a suffix of * are pre-installed
- os*
- time*
- requests\
To install a module run:
`pip install requests` or use your corrisponding package manager
#### <u>Database layout:</u>
```
database description,type(s),creator,v,cv,
{object_name
varible_name varible_value
}
```
'database description' can be blank or '-' in PSDB it will be replaced with 'No description'\
'type(s)' can be blank but **not** '-' (will be fixed - [status](#future-updates))\
'creator' can be blank but **not** '-' (will be fixed - [status](#future-updates))\
'v' can **not** be blank or '-' as it is required for checking compatability\
'cv' can **not** be blank or '-' as it is required for checking compatibility\
'object_name' can **not** be blank or '-' as it must be deleted\
'variable_name' can **not** be blank or '-' as it must be deleted\
'variable_value' can **not** be blank or '-' as it must be deleted

### 2. Using PSDB
Initializing PSDB is most likely the simplest thing you will do when using PSDB, to properly initialise you need 3 lines of code it is best to do this before your main script starts as it may take a few seconds to initialise.
```py
import pythondatabase
pythondatabase.settings(True, True)
pythondatabase.start()
```
`import pythondatabase` simply loads PSDB into your namespace\
`.settings(True, True)` configures the settings, these can be changed throughout PSDB on the go. [More](#3-customising-psdb)\
`.start()` starts PSDB correctly by scanning all databases, checking versions etc

### 3. Customising PSDB
When creating PSDB I decided to keep the settings minimal, meaning there are 3 settings you can control these are output, hide networking and debug. To change the first two settings use `pythonsimpledatabase.settings()` and pass in two arguments. Argument 0 is `HideNetworking` if `True` no networking alerts will appear looking nicer on small windows and keeping the terminal clear, if `False` (providing output is `True`) networking alerts will appear. Argument 1 is `output` this is a major setting as it controls all outputs to the terminal (depending on the type of output), if `True` an output will be printed to the terminal containing simple but important information, if `False` no output is printed excluding errors.
```py
import pythonsimpledatabase
pythonsimpledatabase.settings(True, True)
```
For more advanced users you can use `pythonsimpledatabase.debug()` to have extra information. This is useful for debugging yourself and checking what is happening in PSDB. `Warning: your terminal does become a lot more cluttered and PSDB slows.`
```py
import pythonsimpledatabase
pythonsimpledatabase.setdebug(True)
```
| Position(0-1) | Setting | Description |
| ------------- | ------------- | ------------- |
| 0 | HideNetworking  | If `True` no networking URLs will appear |
| 1 | Output  | Disable and enable output |

| Position(0) | Setting | Description |
| ------------- | ------------- | ------------- |
| 0 | debug  | Disables and enables debugging |
### 4. Creating, Deleting and Changing Databases:
| Function | Description | Arguments |
| ------------- | ------------- | ------------- |
|.create()|Creates a database file|`name`, `creator`|
|.createdb()| Deprecated - ^ | `name`, `type(s)`, `creator` |
|.delete()|Deletes a database file|`name`, `force`|
|.add()|Adds an object in the specified database|`name`, `objectname`|
|.change()|Changes an object value in the specified database|`name`, `objectname`, `newobjectname`
|.addvalue()|Adds a value in the specified database|`name`, `valuename`, `value`
|.remove()|Removes an object from the specified database|`name`, `objectname`|
|.
<u>Functions used:</u>
```py
import pythonsimpledatabase
# *Initalisation here*
pythonsimpledatabase.create()
pythonsimpledatabase.delete()
pythonsimpledatabase.add()
pythonsimpledatabase.change()
pythonsimpledatabase.remove()
```
### 0. Debugging & Error Codes
[Issues page](https://github.com/Englishexe/psdb/issues)
#### <u>Error Table:</u>
Whenever experiencing an error make an issue report to improve PSDB, and make sure to include the dump!
| Error # | severity (L/H) | Reason | Fix |
| ------------- | ------------- | ------------- | ------------- |
| 0 |  | Unknown error |  |
| 1 | HIGH | Failed to import modules | Read [The Basics](#1-the-basics) |
| 2 | LOW | Network did not return `200` | Reinstall PSDB |
| 3 | HIGH | Database directory not found | Make an [issue](https://github.com/Englishexe/psdb/issues) report |
| 4 | LOW | PSDB is not started properly | [How to use PSDB](#2-using-psdb) |
| 5 | LOW | Networking failed | Check internet connection or make a report |

**Dump:**\
When an error happens a long line of text is outputted below, this allows us to debug your error a lot faster as it contains vital information usually hidden from the user. This contains information from the version number to the CWD. When submitting an error please paste this text in (~ to ~) to speed up the debug process.
#### Dump table
Table in order of output, other symbols are used to show the difference between sections
| Display | Name | Description |
| ------------- | ------------- | ------------- |
|0.1.4-alpha| v | Version number |
|`Long Link`| rawurl | The base URL for PSDB resources |
|True| HideNetworking | Setting (`True`/`False`) |
|True| output | Setting (`True`/`False`) |
|1| len(databases) | Number count of databases in memory |
|[`db1name`]| databases | A list of databases in memory |
|True| started | Setting (`True`/`False`) |
|True| debug | Setting (`True`/`False`) |
|C:\PSDB| maindir | Contains the home directory of PSDB |
|C:\PSDB\databases| os.getcwd() | The CWD |
|#1| num | Error code number |
|12|tm_hour|Time|
|0|tm_min|Time|
|0|tm_sec|Time|
|1|tm_mday|Date|
|9|tm_mon|Date|
|2023|tm_year|Date|
|<s>user</s>|<s>os.getlogin()</s>|<s>current signed-in user for directory checking</s>|
|200|.status_code|The response code of [google](https://www.google.com)|



## Contact me
Email: <englishexe8910@gmail.com>\
Discord: [@englishexe](https://www.discord.com) (Not in use)
## Change log:
PSDB follows lightly with semantic versioning, read more [HERE](https://semver.org/) 
| Version       | Description   |
| ------------- | ------------- |
| V0.1-alpha    | Basic scripting of PSDB  |
| V0.1.2-alpha  | SEMVER introduced, Version checking |
| V0.1.3-alpha  | PSDBargs, bug fixes  |
| V0.1.4-alpha  | New documentation, Major work |
| V0.1.5-alpha (Not released)| [More](#future-updates) |
#### <u>V0.1-alpha</u>
```diff
+ Initialisation
+ Networking 
+ Basic scripting
```
#### <u>V0.1.2-alpha</u>
```diff
--- Following SEMVER
-   Removed 'rawurl'
+   Added copyright to 3-5
+   Added module sys
-   Removed copyright box
--- Moved copyright
+   Main.py runs when pythondatabase.py is run incorrectly
--- Fixed version checking
+   Prefixes added
---- Removed random comments
-   Removed PSDB.settings
```
#### <u>V0.1.3-alpha</u>
```diff
-   Removed random comments
--- Improved documentation
+   Added PSDBargs function
--- Cleaned header of pythondatabase.py
-   Removed .gitignore
```
#### <u>V0.1.4-alpha</u>
```diff
--- Fixed formatting error in docs (old)
-   Removed automatic main.py execution
-   Removed dir (not used)
+   Added "wrong execution" detection
+   Added psdbnet function (Deals with network requests)
-   Omitted prefixes (Still see some? Report it in issues)
--- Terminal simplified
--- Transitioned to using psdbnet
-   Omitted networking setting, maybe a future update
--- bypassconfirmation --> NoInput (Removes input dialogs)
+   dbcreate function
+   The great declutter, unlike my room I have removed everything useless
-   Remove most prints (Uses psdbp)
+   Added HideNetworking
--- debugging --> debug
-   Removed exampledatabase.psdb, useless + more clutter
-   Removed psdbargs
-   Removed sys
+   Added heavy optimization resulting in faster speeds
+   Added Dump, outputs advanced information on an error
+   Error Codes (Scroll up)
-   Deprecated createdb() - create()
```

## More
Extra information about PSDB
### Future Updates
```
dbdelete function
dbinfo function
formatting PSDBExecution
```
### About Me
I am [Englishexe](https://github.com/Englishexe), a driven and proficient programmer and an accomplished drone pilot. My journey in the world of programming commenced in 2021, and since then, I have passionately immersed myself in the intricate world of code. With a solid foundation in programming languages such as Python and C++, complemented by additional expertise in Batch and HTML5, I have evolved into a versatile and creative coder.

Currently pursuing my academic endeavours at a STEM-focused college, I am constantly honing my skills and expanding my horizons in the ever-evolving landscape of technology. My educational background in STEM not only reinforces my programming capabilities but also fuels my curiosity for innovation.

In my programming journey, I began by exploring languages like Batch, using them as a stepping stone to grasp the fundamentals of scripting and automation. As my passion grew, I delved deeper into Python and HTML, realising their immense potential for diverse applications. These languages allowed me to craft efficient solutions, from Raspberry Pi applications that seamlessly integrate hardware and software to the development of Folder Encryption that enhance data security.

By 2023, I had further broadened my skill set to include C++, a language renowned for its power and versatility in software development. This expansion has enabled me to tackle more complex projects and contribute to a wider array of technological domains.

Beyond coding, I possess a unique proficiency as a drone pilot, combining my technical prowess with a deep appreciation for aerial photography and videography. This skill adds a distinctive dimension to my abilities, allowing me to merge technology and artistry seamlessly.

My programming journey is characterised by a relentless pursuit of excellence, a commitment to continuous learning, and an insatiable curiosity about the limitless possibilities that technology offers. I look forward to leveraging my skills and experiences to contribute to innovative projects, collaborate with like-minded professionals, and make a meaningful impact in the ever-evolving world of technology and programming.

Thank you for taking the time to learn about me. If you have any questions contact me.

###  CLT
Change Log Template
#### <u>V0.0.0-alphabeta</u>
```diff
+ Added feature
- Removed Feature
--- Change feature
? Temporary fix (Most likely changed in the next version) 
```
### Sorry!
This link isn't working right now, if this is a bug report it in [issues](https://github.com/Englishexe/psdb/issues).\
Back to [Contents](#contents)
## Legal
#### As of 12/9/23 this is the official legal disclaimer for PSDB and other PSDB resources, versions and repositories.
Data Loss Risk:\
Python Simple Database (PSDB) is a database handler designed for simplicity and ease of use. Users should be aware that there is a risk of data loss when using PSDB. While every effort has been made to ensure data integrity, PSDB cannot guarantee the complete prevention of data loss or corruption. Users are advised to regularly back up their data to minimize this risk.

No Warranty:\
PSDB is provided "as is" and without warranty of any kind, either expressed or implied, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The developers and contributors of PSDB make no warranties regarding the functionality, accuracy, or performance of this software.

Use at Your Own Risk:\
The use of PSDB is entirely at the user's own risk. Users are responsible for verifying the suitability of PSDB for their intended purposes and ensuring that their data is adequately protected.

No Liability:\
In no event shall the developers, contributors, or maintainers of PSDB be liable for any damages, including, but not limited to, direct, indirect, special, incidental, or consequential damages, arising out of the use or inability to use PSDB, even if they have been advised of the possibility of such damages. Users acknowledge and agree that they assume all responsibility and risk for the use of PSDB.

Networking:\
PSDB may include networking features that allow it to interact with systems, databases and domains. Users are responsible for ensuring the security and integrity of data transmitted over networks and for complying with all applicable laws and regulations related to data privacy and security.

Infected Versions:\
Users are urged to download PSDB only from official and trusted sources. The developers of PSDB cannot be held responsible for any issues or damage caused by using infected or tampered versions of the software obtained from unauthorized sources. (Trustable sources: GitHub main repository)

By using PSDB, you acknowledge that you have read, understood, and agreed to this disclaimer. If you do not agree with any part of this disclaimer, do not use PSDB.

Please note PSDB is **unstable** and should not be used for any important data until specified in the documentation.

<u>14/9/23</u>\
<u>Englishexe</u>

Python Simple DataBase - PSDB\
Copyright (C) 2023 Englishexe\
GPL-3.0 License

# License
Read the GPL-3.0 License [HERE](https://raw.githubusercontent.com/Englishexe/psdb/main/LICENSE)
\
\
\
\
[Back To Contents](#contents)\
About this file:\
This file has been fact-checked as much as possible and no errors were found, if there is still an error, misspelt word or strange bug please tell us in issues.\
\
Written by Englishexe\
Programmed by Englishexe\
Logo by Commander\
README Version: 1
<!--- Documentation written over 22 days ---!>

