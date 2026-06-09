DECLARE
    v_table_name VARCHAR2(50);
    v_sql VARCHAR2(500);
BEGIN

    -- create table name with current date
    v_table_name := 'ACCOUNTS_' || TO_CHAR(SYSDATE,'DDMMYYYY');

    -- dynamic ddl query
    v_sql := 'CREATE TABLE ' || v_table_name || ' (
                Account_ID NUMBER PRIMARY KEY,
                Created_Date DATE,
                Value_Date DATE,
                Created_By VARCHAR2(50)
             )';

    -- execute the dynamic query
    EXECUTE IMMEDIATE v_sql;

END;
/