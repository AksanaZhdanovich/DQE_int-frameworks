<h1>Pytest</h1>
<h3>Before running tests in Pytest</h3>
<h6>Run in the command line:</h6>
<br>
<code>
python -m pip install pytest 
</code>
<h3>Project structure</h3><br>
<b>Pytest</b><br>
&nbsp;&nbsp;&nbsp;&nbsp;     |--cases.txt <br>
&nbsp;&nbsp;&nbsp;&nbsp;     |-- readme.md<br>
&nbsp;&nbsp;&nbsp;&nbsp;     |-- test_cases.py<br>
<b>Database</b><br>
&nbsp;&nbsp;&nbsp;&nbsp;     |--DB.json <br>
<b>Report</b><br>
&nbsp;&nbsp;&nbsp;&nbsp;     |--reportYYYYMMDD-HHMMSS.txt <br>
<br>
cases.txt - file-helper consists the test-cases structure(content will be added into the report file<br>
test_cases.py -  executed file with test for pytest<br>
DB.json - file with the table names and fields for sql queries<br>
<br>
reportYYYYMMDD-HHMMSS.txt - report file - additional file with the results of running tests with test cases. New file is created for every run of the test_cases.py<br>
<h3>To run tests in Pytest:</h3><br>
In command line(ALT+F12 in Pycharm) run: pytest -v test_cases.py<br>
Pay attention - running file should be in an active directory<br>
<br>
2 options to analyze results: 
1. Terminal window(provides by pytest)
2. Report file.<br>


