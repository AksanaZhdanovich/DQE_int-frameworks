*** Settings ***
Documentation   Robot resources and variables for all tests
Suite Setup       Connect To Database    pymssql    ${DBName}    ${DBUser}    ${DBPass}    ${DBHost}    ${DBPort}
Suite Teardown    Disconnect From Database
Library           DatabaseLibrary
Library           OperatingSystem


Resource  ../resources/Databaseconnection.robot

*** Test Cases ***


Check Person.Address.Addressline1 does not have NULL values
    [Tags]  №1, tbl = Person.Person.Address
    [Documentation]  Checking Addressline1 does not have NULL values
    ...  | * Test Steps *
    ...  | 1. Select count of rows in [Person].[Address]
    ...  | that have NULL values for Addressline1 column
    ...  | 2. Count number of rows returned
    ...  |
    ...  | * Expected result *
    ...  | 1. No rows return
    Check If Exists In Database  SELECT count(*) AS cnt_of_NULL FROM [Person].[Address] WHERE AddressLine1 is NULL  0


Check Person.Address.City does not have numeric values
    [Tags]  №2, tbl = Person.Person.Address
    [Documentation]  Checking City column for numeric values
    ...  | * Test Steps *
    ...  | 1. Select count of rows in [Person].[Address]
    ...  | that have NULL values for Addressline1 column
    ...  |
    ...  | * Expected results *
    ...  | 1. Number of returned rows = 0
    Row Count Is 0  SELECT City,count(*) AS Cnt FROM Person.Address WHERE City like '%[0-9]%' GROUP BY City


Check Production.Document table exists
    [Tags]  №3, tbl = Production.Production.Document
    [Documentation]  Checking that table 'Production.Document' exists in the database
    ...  | * Test Steps *
    ...  | 1. Check that table exists
    ...  |
    ...  | * Expected results *
    ...  | 1. Table exists
    Table Must Exist    Document


Check column names from Production.Document
    [Tags]  №4, tbl = Production.Production.Document
    [Documentation]  Checking that table Production.Document has all columns
    ...  | * Test Steps *
    ...  | 1. Check that all columns are in the table Document
    ...  |
    ...  | Expected results:
    ...  | 1. All columns from ${columns}  are in the Document table
     ${column_name}  query  select COLUMN_NAME from ${dbName}.INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'Document'
    should be true  ${column_name} == ${columns}



Check Production.UnitMeasure.UnitMeasureCode has only unique values
    [Tags]  №5, tbl = Production.UnitMeasure.UnitMeasureCode
    [Documentation]  Checking that column 'UnitMeasureCode' in Production.UnitMeasure table (has only unique values)
    ...  | * Test Steps *
    ...  | 1. Get number of unique values in 'UnitMeasureCode' column
    ...  | 2. Get total number of rows in Production.UnitMeasure table
    ...  |
    ...  | * Expected results *
    ...  | 1. Total number of records in Production.UnitMeasure table is equal to number
    ...  | of unique values in 'UnitMeasureCode' column
    @{results}  Query  SELECT COUNT (DISTINCT UnitMeasureCode) as d_cnt, COUNT(*) as t_cnt from Production.UnitMeasure
    should be equal as integers  ${results[0][0]}   ${results[0][1]}


Check Null value cannot be added in the Production.UnitMeasure.Name column
    [Tags]  №6, tbl = Production.UnitMeasure.Name
    [Documentation]  Checking that Null value for Name column cannot be inserted
    ...  | * Test Steps *
    ...  | 1. Insert Name=NUll in the UnitMeasure table
    ...  |
    ...  | * Expected results *
    ...  | 1. SQL script is executed with an error
    ${sql_query}  Get File  ../Resources/insert_unitmes.sql
    ${err_msg}=  Run Keyword And Expect Error  *  Execute SQL String    ${sql_query}
    Log    ${err_msg}
    Should Not Be Empty    ${err_msg}