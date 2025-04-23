import os
import json

DIARY_FILE = 'diary_entries.json'

def load_entries():
    """Load diary entries from the file."""
    if os.path.exists(DIARY_FILE):
        with open(DIARY_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_entries(entries):
    """Save diary entries to the file."""
    with open(DIARY_FILE, 'w') as file:
        json.dump(entries, file)

def add_entry(entries):
    """Add a new diary entry."""
    date = input("Enter the date (YYYY-MM-DD): ")
    content = input("Write your diary entry: ")
    entries[date] = content
    save_entries(entries)
    print("Diary entry added.")

def view_entries(entries):
    """View all diary entries."""
    if not entries:
        print("No diary entries found.")
    else:
        for date, content in entries.items():
            print(f"{date}: {content}")

def delete_entry(entries):
    """Delete a diary entry by date."""
    date = input("Enter the date of the entry to delete (YYYY-MM-DD): ")
    if date in entries:
        del entries[date]
        save_entries(entries)
        print("Diary entry deleted.")
    else:
        print("No entry found for that date.")

def main():
    entries = load_entries()

    while True:
        print("\nOptions:")
        print("1. Add Diary Entry")
        print("2. View Diary Entries")
        print("3. Delete Diary Entry")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_entry(entries)

        elif choice == '2':
            view_entries(entries)

        elif choice == '3':
            delete_entry(entries)

        elif choice == '4':
            print("Exiting the application.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()