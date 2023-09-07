<h2 align="center">Python Simple DataBase - PSBD</h2>
<p align="center">Made by Englishexe - In Development</p>
<p align="center"><u><b>Latest <s>stable</s> release: V0.1.2-alpha</b></u></p>
<h3><u>About PSDB:</u></h3>
<p>Python Simple DataBase or PSDB for short is a simple python module used for storing data in a semi readable format keeping it simple <small >(as of version 0.2 may change)</small></p>
<h3><u>Why PSDB:</u></h3>
<p>No information to show</p>
<h3><u>How PSDB works:</u></h3>
<p><u>Note: PSDB is in ALPHA meaning alot of things could change.</u><br> PSDB works by a folder named "<code>databases</code>" filled with files, each file is a database (Find out about database files in the Docs). Once a database is opened with <code>pythondatabase.opendb()</code> it is loaded into memory until closed (<code>pythondatabase.closedb()</code>) or another database is opened.</p>
<h3><u>Documentation:</u></h3>
<p><b>Preformance</b><br><small>12,000 10kb databases running V0.1.1-alpha</small><br>Detailed scan: 2m<br>List scan: 9s<br>No output: 4s<p>
<p><b>Modules</b><br><small>* are pre-installed</small><br>os*<br>sys*<br>requests<p>
<p><b>Databases</b><br>Databases are in the format of <pre>
database description,type(s),creator,v,cv,
{object_name
varible_name varible_value
}</pre></p>databases description can be a blank <code>-</code> same with the creator. Type(s) is the type of database (Not in use for now), creator for the database owner / author and finally v is the version the database was created on and cv the current version working on that database.<br><br>
<p><b>Debugging</b><br>Debugging is marked as DEBU in the output, you must have output enabled to see debugging prompts.<br><u>#001</u><br> version | databases | networking | autoupdatedatabases | output | detailedScan</p>
<h3><u>Security and Disclaimers:</u></h3>
<p><b>Networking:</b></p>
<p>PSDB will always alert you when making a request of anykind over the internet, to completely disable this configure your PSDB.settings file.</p>
<p><b>PSDB.settings</b><br>If settings are not defined all settings will be set to <code>True</code></p>
<p><b>Data Loss Risk</b>:<br>PSDB is a software project under development and may not be entirely stable or free from errors. There is a risk of data loss when using this software. Please do not use it for storing or managing critical important information.<br><br><b>No Warranty</b>:<br>The developers and maintainers of PSDB make no warranties regarding the performance, reliability, or suitability of this software for any particular purpose.<br><br><b>Use at Your Own Risk</b>: <br>Users are encouraged to exercise caution and use PSDB solely for non-critical and non-essential data. It is advisable to regularly backup any data used with this software.<br><br><b>No Liability</b>:<br>The developers and maintainers of PSDB shall not be held liable for any direct, indirect, incidental, special, or consequential damages or losses that may arise from the use or misuse of this software.<br><br>Please be aware that PSDB is continually evolving, and improvements and bug fixes are actively being worked on. Users are encouraged to report any issues or concerns to the github page <u><a href="https://github.com/Englishexe/psdb">HERE</a></u>.</p>
<h3>Change log:</h3>
<p><small>From v0.1.2 SEMVER is introduced<br>Versions may be skipped<br>Documentation will be changed accordingly for each update unless stated.<br>Each push to GitHub will result in a updated version number</small></p>
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
<p><code>V0.1.3-alpha</code><b> V </b><br><small>Notes: Small update 0.1.4-alpha will be for creating, deleting and managing databases.
<pre>- Removed random comments
= Improved documenation
+ Added psdbargs function
= Cleaned header of pythondatabase.py
- Removed .gitignore - not needed
= Changed documentation layout, formatting and other
</pre>
