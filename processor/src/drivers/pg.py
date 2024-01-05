import psycopg2
import psycopg2.extras

from .queries import clothes


class PgDriver:
    def __init__(self, pg_config):
        try:
            # Connect to your postgres DB
            self.conn = psycopg2.connect(
                dbname=pg_config["dbname"],
                user=pg_config["user"],
                password=pg_config["password"],
                host=pg_config["host"],
                port=pg_config["port"],
            )
            # Open a cursor to perform database operations
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("Could not create Pg Client", e)

    def read(self, ids_list):
        self.query_params = (ids_list,)
        self.query = clothes.base_queries["select"]

    def insert(self, items_list):
        self.query_params = items_list
        self.query = clothes.base_queries["insert"]
        self.execute_values()
        print("insert query obtained", self.query, self.query_params)

    def execute(self):
        # Execute a query
        self.cursor.execute(self.query, self.query_params)

    def execute_values(self):
        psycopg2.extras.execute_values(
            self.cursor, self.query, self.query_params, template=None, page_size=100
        )

    def fetch(self):
        return self.cursor.fetchall()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
