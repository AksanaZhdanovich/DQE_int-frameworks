*** Settings ***

Library  OperatingSystem
Library  String
Library  DatabaseLibrary



*** Variables ***
${dbName}  AdventureWorks2012
${dbUser}  testuser
${dbPass}
${dbHost}  localhost
${dbPort}  1433

${columns1}=    [('DocumentNode',), ('DocumentLevel',), ('Title',), ('Owner',), ('FolderFlag',), ('FileName',),
${columns2}=    ('FileExtension',), ('Revision',), ('ChangeNumber',), ('Status',), ('DocumentSummary',),  ('Document',),
${columns3}=    ('rowguid',), ('ModifiedDate',)]

${columns}=  ${columns1}${columns2}${columns3}



