import csv
import datetime as dt


def loadData(file_path):
    # Load the CSV data from the given file path 
    # and return it as a list of dictionaries.
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


def getInfectedVisits(data, patient_name, date):
    # Find and return a list of addresses visited by 
    # the infected patient on the given date.
    visits = []
    for entry in data:
        if (entry["User"].lower() == patient_name.lower() 
            and entry["Date"] == date):
            visits.append(entry["Address"])
    return visits


def findContacts(data, infected_visits, date):
    # Find all individuals who visited the same addresses as 
    # the infected person on the given date.
    # Places identified individuals in a dict with them as a key 
    # and the address they were contacted at as the value.
    contacts = {}
    for entry in data:
        if (entry["Date"] == date 
            and entry["Address"] in infected_visits):
            contacts[entry["User"]] = entry["Address"]
    return contacts


def main():
    patientName = input("The person who was tested positive: ").strip()
    inDate = input("When was the test? ").strip()
    data = loadData("contacts.csv")
    # Convert the inputted date into the format needed for the output
    conDate = dt.datetime.strptime(inDate, "%m/%d/%Y")
    # Converts the date to "mm/dd/yyyy" if not already
    midDate = dt.datetime.strftime(conDate, "%m/%d/%Y")
    outDate = dt.datetime.strftime(conDate, "%d, %b %Y")
    infectedVisits = getInfectedVisits(data, patientName, midDate)
    contacts = findContacts(data, infectedVisits, midDate)
    if patientName in contacts:
        del contacts[patientName]  # Remove patient as contact with self
    
    if contacts:
        for contact in contacts:
            print(
                f"{contact} should stay at home for next 10 days"
                f"due to the trip to {contacts[contact]} on {outDate}"
            )
    elif not contacts:
        print(f"No contacts found for {patientName} on {outDate}")


main()
