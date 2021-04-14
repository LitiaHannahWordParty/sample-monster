import pandas as pd
import pyodbc
import gc

sql_conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=akpsqlbi01;DATABASE=Hubspot;Trusted_Connection=yes') 
query = "SELECT companyId, createdate, ynz_eplus_id, name FROM [Hubspot].[prod].[hb_company] hc"
df_company = pd.read_sql(query, sql_conn)

query = "SELECT vid, email,[associatedcompanyid], firstname FROM [Hubspot].[prod].[hb_contact] hc"
df_contact = pd.read_sql(query, sql_conn)

#del df
#gc.collect()

#df_company.head(10)

df_contact.head(10)

#df_company.head(123) - new line

df_contact.head(123)