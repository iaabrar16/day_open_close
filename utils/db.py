import psycopg2
import json
import os

class Database:
    def __init__(self, config_path="utils/config.json"):
        with open(config_path, "r") as f:
            config = json.load(f)
        db_conf = config["db"]

        self.conn = psycopg2.connect(
            host=db_conf["host"],
            port=db_conf["port"],
            dbname=db_conf["dbname"],
            user=db_conf["user"],
            password=db_conf["password"]
        )
        self.cursor = self.conn.cursor()

    def execute(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print("✅ Query executed successfully")
        except Exception as e:
            print(f"❌ Error executing query: {e}")
            self.conn.rollback()

    def close(self):
        self.cursor.close()
        self.conn.close()
