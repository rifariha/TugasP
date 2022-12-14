# Nama          : Ridho Fariha
# NIM           : 227056014
# Matakuliah    : Pemrograman untuk data science dan kecerdasan buatan


import pymysql


class Connection:

    def connect(self):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
        )
        return conn

    def select_database(self, conn, db_name):
        cursor = conn.cursor()
        cursor.execute("USE " + db_name)
        return cursor

    def create_database(self, conn):
        cursor = conn.cursor()

        cursor.execute("create database if not exists football_player")
        # print("Database create successfully")

    def create_table(self, conn):
        cursor = self.select_database(conn, "football_player")
        cursor.execute(
            "CREATE TABLE if not exists players (id int(10) primary key AUTO_INCREMENT, name VARCHAR(255), age INTEGER(5), nationality CHAR(3), born_year INTEGER(4), squad VARCHAR(255))")
        # print("Table create successfully")
