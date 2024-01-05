import psycopg2
from config import pg_config


def create_schema():
    try:
        conn = psycopg2.connect(
            dbname=pg_config["dbname"],
            user=pg_config["user"],
            password=pg_config["password"],
            host=pg_config["host"],
            port=pg_config["port"],
        )
        conn.autocommit = True
        cursor = conn.cursor()
    except Exception as e:
        print("Could not create Pg Client", e)

    try:
        sql_file = open("./scripts/clothes.sql", mode="r")
        db_schema = sql_file.read()

        print("Updating DB Schema")
        if pg_config["recreate"]:
            cursor.execute("DROP DATABASE wardrobe;")
        cursor.execute("CREATE DATABASE wardrobe;")
        conn.autocommit = False

        cursor.execute(db_schema)
        conn.commit()
        print("DB Schema updated successfully")

        sql_file.close()
    except Exception as e:
        print("Could not update DB Schema", e)

    cursor.close()
    conn.close()


create_schema()
