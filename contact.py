import csv
import datetime as dt


def load_data(file_path):
    # Load the CSV data from the given file path and return it as a list of dictionaries.
    # Each dictionary contains 'User', 'NHS number', 'Date', and 'Address'.

    data = []
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(
                {
                    "User": row["User"],
                    "NHS Number": row["NHS Number"],
                    "Date": row["Date"],
                    "Address": row["Address"],
                }
            )

    return data


def get_infected_visits(data, patient_name, date):
    # Find and return a list of addresses visited by the infected patient on the given date.

    visits = []

    for entry in data:
        if entry["User"].lower() == patient_name.lower() and entry["Date"] == date:
            visits.append(entry["Address"])

    return visits


def find_contacts(data, infected_visits, date):
    # Find all individuals who visited the same addresses as the infected person on the given date.

    contacts = set()  # Uses a set to avoid duplicates

    for entry in data:
        if entry["Date"] == date and entry["Address"] in infected_visits:
            contacts.add(entry["User"])

    return contacts


def main():
    patient_name = input("Enter the name of the infected patient: ").strip()

    date = input("Enter the date (DD/MM/YYYY) to search for contacts: ").strip()

    dates = []
    dates = date.split("/")  # split all the numbers apart

    date = ""  # empty date

    for i in reversed(dates):
        date += i
        date += "-"

    date = date.removesuffix("-")  # removes extra "-" at the end of the date

    data = load_data("contacts.csv")

    infected_visits = get_infected_visits(data, patient_name, date)

    # If lonly declare
    if not infected_visits:
        print(f"No visits found for {patient_name} on {date}")

    contacts = find_contacts(data, infected_visits, date)

    contacts.discard(patient_name)  # remove patient if appear as contact with self

    if contacts:
        print("The people who need to be contacted are: ")
        for contact in contacts:
            print(contact)
        else:
            print(f"No contacts found for {patient_name} on {date}")


main()
