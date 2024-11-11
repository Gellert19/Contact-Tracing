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

    contacts = {}

    for entry in data:
        if entry["Date"] == date and entry["Address"] in infected_visits:
            contacts[entry["User"]] = entry["Address"]

    return contacts


def main():
    patient_name = input("Enter the name of the infected patient: ").strip()

    indate = input("Enter the date (MM/DD/YYYY) to search for contacts: ").strip()

    data = load_data("contacts.csv")

    infected_visits = get_infected_visits(data, patient_name, indate)

    contacts = find_contacts(data, infected_visits, indate)
    del contacts[patient_name] # Remove patient as contact with self

    # Convert the inputed date into the format needed for the output
    condate = dt.datetime.strptime(indate, "%m/%d/%Y")
    outdate = dt.datetime.strftime(condate, "%d, %b %Y")

    if contacts:
        for contact in contacts:
            print(
                f"{contact} should stay at home for the next 10 days due to the trip to {contacts[contact]} on {outdate}"
            )
    elif not contacts:
        print(f"No contacts found for {patient_name} on {outdate}")


main()
