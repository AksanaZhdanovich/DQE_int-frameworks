import pymssql
from datetime import datetime
import json
import os

connect = pymssql.connect(host='host.docker.internal',
                          database='AdventureWorks2012',
                          user='testuser',
                          password='test')
jsonpath = 'pytest/Database/DB.json'
reportFile = open('pytest/report/report' + datetime.now().strftime("%Y%m%d-%H%M%S") + '.txt', 'w+')
cursor = connect.cursor()
with open('pytest/cases.txt') as info_file:
    lines_in_file = info_file.readlines()


def add_info_in_the_report_file(start_position):
    for line_number in range(start_position, start_position + 11):
        reportFile.write(lines_in_file[line_number])
    reportFile.write('\nRESULT:---------------------------\n')


def test_check_null_values():
    json_file = open(jsonpath, 'r')
    json_data = json_file.read()
    obj = json.loads(json_data)
    json_attr = obj['NullFieldsCheck']
    add_info_in_the_report_file(0)

    for i in range(len(json_attr)):
        query = "select count(*) from {0}.{1} where {2} is NULL;" \
            .format(json_attr[i].get("SchemaName"),
                    json_attr[i].get("TableName"),
                    json_attr[i].get("NotNullField"))

        cursor.execute(query)

        for result in cursor.fetchall():
            assert result == (0,), 'Table has NULL values'
            if result == (0,):
                reportFile.write("check_null_values test is PASSED\n\n")
            else:
                reportFile.write("check_null_values test is FAILED\n\n")


def test_check_numeric_values():
    json_file = open(jsonpath, 'r')
    json_data = json_file.read()
    obj = json.loads(json_data)
    json_attr = obj['NumericValuesCheck']
    add_info_in_the_report_file(12)

    for i in range(len(json_attr)):
        query = "select count(*) from {0}.{1} where {2} like '%[0-9]%';" \
            .format(json_attr[i].get("SchemaName"),
                    json_attr[i].get("TableName"),
                    json_attr[i].get("CheckField"))

        cursor.execute(query)

        for result in cursor.fetchall():
            assert result == (0,), 'Column has numeric values'
            if result == (0,):
                reportFile.write("check_numeric_values test is PASSED\n\n")
            else:
                reportFile.write("check_numeric_values test is FAILED\n\n")


def test_check_table_exists():
    json_file = open(jsonpath, 'r')
    json_data = json_file.read()
    obj = json.loads(json_data)
    json_attr = obj['TableExistCheck']
    add_info_in_the_report_file(23)
    for i in range(len(json_attr)):
        query = "select count(*) from {0}.{1};" \
            .format(json_attr[i].get("SchemaName"),
                    json_attr[i].get("TableName"))
        cursor.execute(query)
        for result in cursor.fetchall():
            assert result[0] >= 0, 'Table exists'
            if result[0] >= 0:
                reportFile.write("check_table_exists test is PASSED\n\n")
            else:
                reportFile.write("check_table_exists test is FAILED\n\n")


def test_check_all_columns():
    list_of_columns = [('DocumentNode',), ('DocumentLevel',), ('Title',), ('Owner',), ('FolderFlag',), ('FileName',), (
        'FileExtension',), ('Revision',), ('ChangeNumber',), ('Status',), ('DocumentSummary',), ('Document',), (
                           'rowguid',), ('ModifiedDate',)]
    json_file = open(jsonpath, 'r')
    json_data = json_file.read()
    obj = json.loads(json_data)
    json_attr = obj['ColumnsNamesCheck']
    add_info_in_the_report_file(35)
    for i in range(len(json_attr)):
        query = "select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = '{1}';" \
            .format(json_attr[i].get("SchemaName"),
                    json_attr[i].get("TableName"))
        cursor.execute(query)
        result_query = cursor.fetchall()
        assert result_query == list_of_columns, 'Table has unexpected fields'
        if result_query == list_of_columns:
            reportFile.write("check_all_columns test is PASSED\n\n")
        else:
            reportFile.write("check_all_columns test is FAILED\n\n")


def test_check_unique_values():
    json_file = open(jsonpath, 'r')
    json_data = json_file.read()
    obj = json.loads(json_data)
    json_attr = obj['UniqueValueCheck']
    add_info_in_the_report_file(47)
    for i in range(len(json_attr)):
        query = "SELECT COUNT (DISTINCT {2}) as d_cnt, COUNT(*) as t_cnt from {0}.{1}" \
            .format(json_attr[i].get("SchemaName"),
                    json_attr[i].get("TableName"),
                    json_attr[i].get("Field"))
        cursor.execute(query)
        result_query = cursor.fetchall()
        assert result_query[0][0] == result_query[0][1], 'Table has duplicates'
        if result_query[0][0] == result_query[0][1]:
            reportFile.write("check_unique_values test is PASSED\n\n")
        else:
            reportFile.write("check_unique_values test is FAILED\n\n")


def test_check_insert_NULL():
    json_file = open(jsonpath, 'r')
    json_data = json_file.read()
    obj = json.loads(json_data)
    json_attr = obj['InsertValueCheck']
    add_info_in_the_report_file(59)
    for i in range(len(json_attr)):
        query = "INSERT INTO {0}.{1} ({2},{3}) VALUES ('AAA',NULL);" \
            .format(json_attr[i].get("SchemaName"),
                    json_attr[i].get("TableName"),
                    json_attr[i].get("Field1"),
                    json_attr[i].get("Field2"))
        try:
            cursor.execute(query)
            reportFile.write("check_insert_NULL test is FAILED\n\n")
            assert False
        except:
            reportFile.write("check_insert_NULL test is PASSED\n\n")
            assert True
