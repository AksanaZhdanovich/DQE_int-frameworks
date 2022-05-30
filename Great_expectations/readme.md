# start working with great expectation
pip install great_expectations
# add additional libraries
pip install notebook
pip install ipywidgets
pip install widgetsbextension
pip install sqlalchemy


#create a new project
great_expectations --v3-api init 

#create a new connection to the database
great_expectations datasource new
In interactive mode:
choose 2 - Relational database 
choose 6 - Do you have a working SQLAlchemy connection string?
In jupiter notebook - add connection string and datasource_name. Run all cells. 
<h4> Connection string:</h4>
mssql+pyodbc://username:password@127.0.0.1:1433/AdventureWorks2012?driver=ODBC Driver 17 for SQL Server&charset=utf&autocommit=true
(pyodbc should be installed)

#create new suite
great_expectations --v3-api suite new
In interactive mode:
1. choose 3, to generate expectations automatically, using a profiler
2. choose asset(index of the table)
3. give name to the Expectation suite
4. choose Y 
In jupyter notebook run all cells. In cell "Select columns" exclude columns for tests.  

#edit existing suite
For homework purpose prod_suite was created. To observe it or edit and run use the following command:
 1) great_expectations --v3-api suite edit product_suite
 2) run all cells in jupyter notebook(after saving all tests will run)

Created Expectations Suite is stored as json file in /expectations.product_suite.json

# checkpoint creation
To create checkpoint run the command:
1) great_expectations --v3-api checkpoint new <checkpoint_name>
2) created checkpoints are stored in /checkpoints/<checkpoint_name>.yml
3) to run existing checkpoints execute great_expectations --v3-api checkpoint run product_checkpoint
4) to uncomment cell with Run options


# Data Docs (report to validate results of ExpectationSuite execution)
Data Docs can be viewed from /uncomitted/validations/data_docs/local_site/index.html






