import connection
import main
import pandas as pd


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


def select_operator():
    print("1. Equal")
    print("2. Not Equal")
    print("3. Contains")
    print("4. Not Contain")
    print("5. Greater Than")
    print("6. Less Than")
    print("7. Equal and Greater Than")
    print("8. Equal and Less Than")
    operator_option = input("Select operator : ")
    return operator_option


def insert_data(name, age, nationality, born_year, squad):
    conn = connection.connect()
    cursor = connection.select_database(conn, "football_player")

    sql = """insert into `players` (name, age, nationality,born_year, squad) values (%s, %s, %s, %s, %s)"""
    cursor.execute(sql, (name, age, nationality, born_year, squad))
    conn.commit()

    conn.close()
    print("Insert data successful.")
    main.main()


def insert_new_data():
    name = input("Player name: ")
    age = input("Player age: ")
    nationality = input("Player nationality: ")
    born_year = input("Player born_year: ")
    squad = input("Plyaer squad: ")

    insert_data(name, age, nationality, born_year, squad)


def show_data(val):
    global sql
    global field
    global operator
    global sortBy
    global sortOption

    conn = connection.connect()
    cursor = connection.select_database(conn, "football_player")

    if val == "1":
        print("1. Search by name")
        print("2. Search by age")
        print("3. Search by nationality")
        print("4. Search by born year")
        print("5. Search by squad")

        option = input("Select search by field : ")

        if option == "1":
            field = "name"
        elif option == "2":
            field = "age"
        elif option == "3":
            field = "nationality"
        elif option == "4":
            field = "born_year"
        elif option == "5":
            field = "squad"
        else:
            print("Option does not exist")

        operator_option = select_operator()

        value = input("Give the value : ")

        print("1. Sort by name")
        print("2. Sort by age")
        print("3. Sort by nationality")
        print("4. Sort by born year")
        print("5. Sort by squad")

        sort = input("Select sort by field : ")

        print("1. ASCENDING")
        print("2. DESCENDING")
        sort_option = input("Select sort method : ")

        if sort == "1":
            sortBy = "name"
        elif sort == "2":
            sortBy = "age"
        elif sort == "3":
            sortBy = "nationality"
        elif sort == "4":
            sortBy = "born_year"
        elif sort == "5":
            sortBy = "squad"
        else:
            print("Option does not exist")

        if sort_option == "1":
            sortOption = "ASC"
        elif sort_option == "2":
            sortOption = "DESC"

        if operator_option == "1":
            sql = "select * from players where {field} = '{value}' order by {sort} {sort_option}".format(field=field,
                                                                                                         value=value,
                                                                                                         sort=sortBy,
                                                                                                         sort_option=sortOption)
        elif operator_option == "2":
            sql = "select * from players where {field} != '{value}' order by {sort} {sort_option}".format(field=field,
                                                                                                          value=value,
                                                                                                          sort=sortBy,
                                                                                                          sort_option=sortOption)
        elif operator_option == "3":
            sql = "select * from players where {field} LIKE '%{value}%' order by {sort} {sort_option}".format(
                field=field, value=value, sort=sortBy, sort_option=sortOption)
        elif operator_option == "4":
            sql = "select * from players where {field} NOT LIKE '%{value}%' order by {sort} {sort_option}".format(
                field=field, value=value, sort=sortBy, sort_option=sortOption)
        elif operator_option == "5":
            sql = "select * from players where {field} > '{value}' order by {sort} {sort_option}".format(field=field,
                                                                                                         value=value,
                                                                                                         sort=sortBy,
                                                                                                         sort_option=sortOption)
        elif operator_option == "6":
            sql = "select * from players where {field} < '{value}' order by {sort} {sort_option}".format(field=field,
                                                                                                         value=value,
                                                                                                         sort=sortBy,
                                                                                                         sort_option=sortOption)
        elif operator_option == "7":
            sql = "select * from players where {field} >= '{value}' order by {sort} {sort_option}".format(field=field,
                                                                                                          value=value,
                                                                                                          sort=sortBy,
                                                                                                          sort_option=sortOption)
        elif operator_option == "8":
            sql = "select * from players where {field} <= '{value}' order by {sort} {sort_option}".format(field=field,
                                                                                                          value=value,
                                                                                                          sort=sortBy,
                                                                                                          sort_option=sortOption)
        else:
            print("Operator option does not exist")

    elif val == "2":
        sql = "select * from players"
    else:
        print("Option not available")
        main.main()

    print(sql)
    cursor.execute(sql)
    records = cursor.fetchall()

    data = []
    for row in records:
        data.append(row)

    df = pd.DataFrame(data, columns=['Id', 'Name', 'Age', 'Nationality', 'Born Year', 'Squad'])
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', 7)
    pd.set_option('display.expand_frame_repr', False)
    df.to_string()

    print(df)
    conn.close()
    main.main()


def show_option():
    print("1. Filter/Search data")
    print("2. Show all data")

    val = input("Select your option: ")

    show_data(val)


def update_data():
    conn = connection.connect()
    cursor = connection.select_database(conn, "football_player")

    global field
    global sql
    global set_field

    print("1. Update name")
    print("2. Update age")
    print("3. Update nationality")
    print("4. Update born year")
    print("5. Update squad")

    set_field_option = input("Select update field : ")

    if set_field_option == "1":
        set_field = "name"
    elif set_field_option == "2":
        set_field = "age"
    elif set_field_option == "3":
        set_field = "nationality"
    elif set_field_option == "4":
        set_field = "born_year"
    elif set_field_option == "5":
        set_field = "squad"

    value = input("Give update field value : ")

    print("1. Update by id")
    print("2. Update by name")
    print("3. Update by age")
    print("4. Update by nationality")
    print("5. Update by born year")
    print("6. Update by squad")

    option = input("Select update parameter : ")

    if option == "1":
        field = "id"
    elif option == "2":
        field = "name"
    elif option == "3":
        field = "age"
    elif option == "4":
        field = "nationality"
    elif option == "5":
        field = "born_year"
    elif option == "6":
        field = "squad"
    else:
        print("Option does not exist")

    operator_option = select_operator()

    cond_value = input("Give update parameter value : ")

    if operator_option == "1":
        sql = "update players set {set_field}='{value}' where {field} = '{cond_value}'".format(
            set_field=set_field, value=value, field=field, cond_value=cond_value)

    elif operator_option == "2":
        sql = "update players set {set_field}='{value}' where {field} != '{cond_value}'".format(
            set_field=set_field, value=value, field=field, cond_value=cond_value)

    elif operator_option == "3":
        sql = "update players set {set_field}='{value}' where {field} LIKE '%{cond_value}%'".format(
            set_field=set_field, value=value, field=field, cond_value=cond_value)

    elif operator_option == "4":
        sql = "update players set {set_field}='{value}' where {field} NOT LIKE '{cond_value}%'".format(
            set_field=set_field, value=value, field=field, cond_value=cond_value)

    elif operator_option == "5":
        sql = "update players set {set_field}='{value}' where {field} > '{cond_value}'".format(
            set_field=set_field, value=value, field=field, cond_value=cond_value)

    elif operator_option == "6":
        sql = "update players set {set_field}='{value}' where {field} < '{cond_value}'".format(
            set_field=set_field, value=value, field=field, cond_value=cond_value)

    elif operator_option == "7":
        sql = "update players set {set_field}='{value}' where {field} >= '{cond_value}'".format(
            set_field=set_field, value=value, field=field, cond_value=cond_value)

    elif operator_option == "8":
        sql = "update players set {set_field}='{value}' where {field} <= '{cond_value}'".format(
            set_field=set_field, value=value, field=field, cond_value=cond_value)

    else:
        print("Operator option does not exist")

    print(sql)
    cursor.execute(sql)
    conn.commit()

    conn.close()

    print("Update data successful")
    main.main()


def delete_data():
    conn = connection.connect()
    cursor = connection.select_database(conn, "football_player")

    global sql
    global set_field

    print("1. Delete by id")
    print("2. Delete by name")
    print("3. Delete by age")
    print("4. Delete by nationality")
    print("5. Delete by born year")
    print("6. Delete by squad")

    set_field_option = input("Select delete parameter : ")

    if set_field_option == "1":
        set_field = "id"
    elif set_field_option == "2":
        set_field = "name"
    elif set_field_option == "3":
        set_field = "age"
    elif set_field_option == "4":
        set_field = "nationality"
    elif set_field_option == "5":
        set_field = "born_year"
    elif set_field_option == "6":
        set_field = "squad"

    operator_option = select_operator()

    value = input("Give parameter value : ")

    if operator_option == "1":
        sql = "delete from players where {set_field} = '{value}'".format(set_field=set_field, value=value)

    elif operator_option == "2":
        sql = "delete from players where {set_field} != '{value}'".format(set_field=set_field, value=value)

    elif operator_option == "3":
        sql = "delete from players where {set_field} LIKE '%{value}%'".format(set_field=set_field, value=value)

    elif operator_option == "4":
        sql = "delete from players where {set_field} NOT LIKE '%{value}%'".format(set_field=set_field, value=value)

    elif operator_option == "5":
        sql = "delete from players where {set_field} > '{value}'".format(set_field=set_field, value=value)

    elif operator_option == "6":
        sql = "delete from players where {set_field} < '{value}'".format(set_field=set_field, value=value)

    elif operator_option == "7":
        sql = "delete from players where {set_field} >= '{value}'".format(set_field=set_field, value=value)

    elif operator_option == "8":
        sql = "delete from players where {set_field} <= '{value}'".format(set_field=set_field, value=value)

    else:
        print("Operator option does not exist")

    print(sql)
    cursor.execute(sql)
    conn.commit()

    conn.close()

    print("Delete data successful")
    main.main()
