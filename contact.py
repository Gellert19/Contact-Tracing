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
                    "NHS number": row["NHS number"],
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
    date = input("Enter the date (YYYY-MM-DD) to search for contacts: ").strip()
    
    data = load_data("contacts.csv")
    
    
