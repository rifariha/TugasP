import connection
import filtering


def import_data(df):
    conn = connection.connect()

    connection.create_database(conn)
    connection.create_table(conn)

    cursor = connection.select_database(conn, "football_player")

    cursor.execute("select count(*) from players")

    jumlah = 0
    for row in cursor:
        jumlah = row[0]
        break

    if jumlah <= 0:
        sql = """insert into `players` (name, age, nationality,born_year, squad) values (%s, %s, %s, %s, %s)"""
        for i in df.index:
            cursor.execute(sql, (df['name'][i], df['age'][i], df['nationality'][i], df['born_year'][i], df['squad'][i]))
            conn.commit()

    conn.close()


def main():
    df = filtering.result('2022_2023_Football_Player_Stats.csv')
    import_data(df)


if __name__ == '__main__':
    main()
