from utils.snowflake_conn import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT CURRENT_VERSION()")
print("Connected to Snowflake, version:", cursor.fetchone()[0])
cursor.close()
conn.close()
