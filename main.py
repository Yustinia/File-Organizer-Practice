from fileorganize import FileOrganizer
import time

organizer = FileOrganizer()


# Identify the items/files
def ident_items():
    while True:
        do_ident_items = input("Identify the items? Y/N: ").strip().lower()

        if do_ident_items == "y":
            organizer.identify_file()
            break
        elif do_ident_items == "n":
            for sec in range(3, 0, -1):
                print(f"Exiting in {sec}...")
                time.sleep(0.2)
            break
        else:
            print("Invalid")

    return do_ident_items


# Asks whether to sort the files
def organize():
    while True:
        do_organize_items = input("\nDo you want to organize the files? Y/N: ").strip().lower()

        if do_organize_items == "y":
            organizer.move_item()
            break
        elif do_organize_items == "n":
            for sec in range(3, 0, -1):
                print(f"Exiting in {sec}...")
                time.sleep(0.2)
            break
        else:
            print("Invalid")

    return do_organize_items


def main():
    do_ident_items = ident_items()

    if do_ident_items == "y":
        do_organize_items = organize()

        if do_organize_items == "y":
            organizer.move_summary()

    elif do_ident_items == "n":
        pass


main()
