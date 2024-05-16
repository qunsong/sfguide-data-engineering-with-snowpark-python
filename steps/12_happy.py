import snowflake.snowpark
from snowflake.snowpark import Session
from snowflake.snowpark.functions import sproc
 
connection_parameters = {
       "account": "uiiafux-dd04772",
       "user": "qsong",
       "password": "WWfreemind1!",
       "role": "ACCOUNTADMIN",  # optional
       "warehouse": "HOL_WH",  # optional
       "database": "HOL_DB",  # optional
       "schema": "ANALYTICS",  # optional
     }  

new_session = Session.builder.configs(connection_parameters).create()

new_session.add_packages('snowflake-snowpark-python')
 
@sproc
def add_sp(session_: snowflake.snowpark.Session, x: int, y: int) -> int:
    return session_.sql(f"select {x} + {y}").collect()[0][0]
