<h1>Robot Framework</h1>
<h3>Before running tests in Robot Framework</h3>
<h6>Run in the command line:</h6>
<br>
<code>
pip install robotframework <br>
pip install robotframework-databaselibrary <br>
pip install pymssql
</code><br>
<br>

<h3>Project structure</h3><br>
<b>Pytest</b><br>
&nbsp;&nbsp;&nbsp;&nbsp;     |-- test.robot<br>
<b>Resources</b><br>
&nbsp;&nbsp;&nbsp;&nbsp;     |-- Databaseconnection.robot<br>
&nbsp;&nbsp;&nbsp;&nbsp;     |-- insert_unitmes.sql<br>
log.html<br>
output.xml<br>
readme.md<br>
report.html<br>

test.robot - executed file, consisted all Test Cases
Databaseconnection.robot - settings for the  project (connection to db, variables)<br>
The following files are created by Robotframework:<br>
log.html - Test statistics, Test Execution Log<br>
report.html - Test report, Test Details <br>
output.xml - output<br>



<h4>Pay attention - password to connect to DB is not saved in the Databaseconnection.robot file.</h4>
<h4>To run test.robot  user should create they own user and password to connect to AdventureWorks2012 DB.</h4>

