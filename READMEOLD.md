<p>⚠️: This file will NOT be updated past 0.1.3-alpha | Refer to the new README file.</p>
<h2 align="center">Python Simple DataBase - PSBD</h2>
<p align="center">Made by Englishexe - In Development</p>
<p align="center"><u><b>Latest <s>stable</s> release: V0.1.4-alpha</b></u></p>
<h3><u>About PSDB:</u></h3>
<p>Python Simple DataBase is a python module that allows data  to be stored without complication, it does all the heavy  lifting with the databases, to start it simply type two lines <code>import pythonsimpledatabase</code> and <code>pythondatabase.start()</code></p>
<h3><u>Why PSDB:</u></h3>
<p>PSDB is much simpler then SQL, mongo DB and other database handlers but less powerfull as PSDD is meant for small simplified databases.</p>
<h3><u>How PSDB works:</u></h3>
<p><u>Note: PSDB is in ALPHA meaning alot of things could change.</u><br> PSDB works by a folder named "<code>databases</code>" filled with files, each file is a database (Find out about database files in the Docs). Once a database is opened with <code>pythondatabase.opendb()</code> it is loaded into memory until closed (<code>pythondatabase.closedb()</code>) or another database is opened.</p>
<h3><u>Documentation:</u></h3>
<p><b>Preformance</b><br><small>12,000 10kb databases running V0.1.1-alpha</small><br>Detailed scan: 2m<br>List scan: 9s<br>No output: 4s<p>
<p><b>Modules</b><br><small>* are pre-installed</small><br>os*<br>sys*<br>requests<p>
<p><b>Databases</b><br><small>Note: As of 0.1.4-alpha you can not "open" databases</small><br>Databases are in the format of <pre>
database description,type(s),creator,v,cv,
{object_name
varible_name varible_value
}</pre></p>databases description can be a blank <code>-</code> same with the creator. Type(s) is the type of database (Not in use for now), creator for the database owner / author and finally v is the version the database was created on and cv the current version working on that database.<br><br>
<p><b>Debugging</b><br>Debugging is marked as DEBU in the output, you must have output enabled to see debugging prompts.<br><u>#001</u><br> version | databases | networking | bypassconfirmation | output | detailedScan</p>
<p><b>How to read the output</b><br>At first the terminal can be hard to read, to understand it below a resource in embeded.
<pre>
<b>Outline</b>

Section Title / Output
^Section Output
<^Sub-section Output
<<^Sub-Sub-Section Output (Debug)
-Developer note

<b>Example</b>
Databases
^ exampledatabase.psdb
<^Desc  : Just a few cats
<^Owner : Englishexe
<^Type  : EXA/NOO
^Illegal item in 'databases' (Random_File)
</pre>
<h3><u>Security and Disclaimers:</u></h3>
<p><b>Functions:</b></p>
<p>Any function reprix</p>
<p><b>Networking:</b></p>
<p>PSDB will always alert you when making a request of anykind over the internet, to completely disable this configure your PSDB.settings file.</p>
<p><b>PSDB.settings</b><br>If settings are not defined all settings will be set to <code>True</code></p>
<p><b><s>Data Loss Risk</b>:<br>PSDB is a software project under development and may not be entirely stable or free from errors. There is a risk of data loss when using this software. Please do not use it for storing or managing critical important information.<br><br><b>No Warranty</b>:<br>The developers and maintainers of PSDB make no warranties regarding the performance, reliability, or suitability of this software for any particular purpose.<br><br><b>Use at Your Own Risk</b>: <br>Users are encouraged to exercise caution and use PSDB solely for non-critical and non-essential data. It is advisable to regularly backup any data used with this software.<br><br><b>No Liability</b>:<br>The developers and maintainers of PSDB shall not be held liable for any direct, indirect, incidental, special, or consequential damages or losses that may arise from the use or misuse of this software.<br><br>Please be aware that PSDB is continually evolving, and improvements and bug fixes are actively being worked on. Users are encouraged to report any issues or concerns to the github page <u><a href="https://github.com/Englishexe/psdb">HERE</s></a></u>.

Start of new LEGAL document: VVVVVVVVVVVVVVVV

Data Loss Risk:
Python Simple Database (PSDB) is a database handler designed for simplicity and ease of use. Users should be aware that there is a risk of data loss when using PSDB. While every effort has been made to ensure data integrity, PSDB cannot guarantee the complete prevention of data loss or corruption. Users are advised to regularly back up their data to minimize this risk.

No Warranty:
PSDB is provided "as is" and without warranty of any kind, either expressed or implied, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The developers and contributors of PSDB make no warranties regarding the functionality, accuracy, or performance of this software.

Use at Your Own Risk:
The use of PSDB is entirely at the user's own risk. Users are responsible for verifying the suitability of PSDB for their intended purposes and ensuring that their data is adequately protected.

No Liability:
In no event shall the developers, contributors, or maintainers of PSDB be liable for any damages, including, but not limited to, direct, indirect, special, incidental, or consequential damages, arising out of the use or inability to use PSDB, even if they have been advised of the possibility of such damages. Users acknowledge and agree that they assume all responsibility and risk for the use of PSDB.

Networking:
PSDB may include networking features that allow it to interact with other systems and databases. Users are responsible for ensuring the security and integrity of data transmitted over networks and for complying with all applicable laws and regulations related to data privacy and security.

Infected Versions:
Users are urged to download PSDB only from official and trusted sources. The developers of PSDB cannot be held responsible for any issues or damage caused by using infected or tampered versions of the software obtained from unauthorized sources.

By using PSDB, you acknowledge that you have read, understood, and agreed to this disclaimer. If you do not agree with any part of this disclaimer, do not use PSDB.

Please note PSDB is **unstable** and should not be used for any important data as of 0.1.4-alpha until specified in the documentation.
</p>
<h3>Change log:</h3>
<p><small>From v0.1.2 SEMVER is introduced lightly<br>Versions may be skipped<br>Documentation will be changed accordingly for each update unless stated.<br>Each push to GitHub will result in a updated version number</small></p>
<p><code>V?.?-alphabeta</code><b> V </b>
<pre>+ Added feature
- Removed feature
= Changed feature
? Tempory fix / change
T used during development, marks things that need doing or will be fixed in the next push.</pre>
<p><code>V0.1 ALPHA</code><b> V </b>
<pre>+ Initalisation<br>
+ Networking</pre>
<p><code>V0.1.2-alpha</code><b> V </b>
<pre>+ Following SEMVER
- 'rawurlv' removed (Replaced by 'rawurl') Note: Changed script accordingly
+ Added copyright to ln 3-5
+ Added 'import sys'
- Removed copyright box
= Moved copyright
+ Main.py runs when pythondatabase.py is ran incorrectly (Developer feature)
+ Fixed version checking
+ Prefixes added (In progress 8:30 6/9/23)
T Remove comments that have no purpose
+ Removed PSDB.settings</pre>
<p><code>V0.1.3-alpha</code><b> V </b><br><small>Notes: Small update 0.1.4-alpha will be for creating, deleting and managing databases. </small>
<pre>- Removed random comments
= Improved documenation
+ Added psdbargs function
= Cleaned header of pythondatabase.py
- Removed .gitignore - not needed
= Changed documentation layout, formatting and other
</pre>
<p><code>V0.1.4-alpha</code><b> V </b>
<pre>= Fixed formatting error in docs
+ Added info function with "started" detection
- Removed automatic main.py execution
- Removed dir (not used)
+ Added "wrong execution" detection
+ autoupdatedatabases --> bypassconfirmation (Bypasses the Are you sure? Dialogs)
+ Added psdbnet function (Deals with requests)
- Ommitted prefixes (Still see some? Report it in issues)
T Terminal simplified
= Transitoning to using psdbnet
- Ommited networking setting, may be a future update
T Added createdb function
T Added deletedb function
T Added infodb function
T Correct formatting PSDBExecution</pre>
<p>Ignore everything below this line, it is for future updates</p>
<h3>About PSDB - Ignore this</h3>
<p>PSDB is a python module to easily store data using simple semi-human readble databases, version X.X.X-alphabeta<b>-N</b> has no networking capability providing a more secure enviroment. See the (link here) table for version information</p>
<h3>Why PSDB - Ignore this</h3>
<p>Why should you choose PSDB over other database handlers like SQL or mongoDB? PSDB is a great starting database handler for beginners or small projects as it has a very simple syntax and output.</p>