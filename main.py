import filtering
import transaction


def main():
    trx = transaction.Transaction()
    filters = filtering.Filtering()

    df = filters.result('2022_2023_Football_Player_Stats.csv')
    trx.import_data(df)

    print("========================================")
    print("Choose action you want (type the number)")
    print("1. Insert New data")
    print("2. Show data")
    print("3. Update data")
    print("4. Delete data\n")

    val = input("Give your action: ")

    if val == "1":
        trx.insert_new_data()
    elif val == "2":
        trx.show_option()
    elif val == "3":
        trx.update_data()
    elif val == "4":
        trx.delete_data()
    else:
        print("Option not available")


if __name__ == '__main__':
    main()
