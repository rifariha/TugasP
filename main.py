import filtering
import transaction


def main():
    df = filtering.result('2022_2023_Football_Player_Stats.csv')
    transaction.import_data(df)
    print("========================================")
    print("Choose action you want (type the number)")
    print("1. Insert New data")
    print("2. Show data")
    print("3. Update data")
    print("4. Delete data\n")

    val = input("Give your action: ")

    if val == "1":
        transaction.insert_new_data()
    elif val == "2":
        transaction.show_option()
    elif val == "3":
        transaction.update_data()
    elif val == "4":
        transaction.delete_data()
    else:
        print("Option not available")


if __name__ == '__main__':
    main()
