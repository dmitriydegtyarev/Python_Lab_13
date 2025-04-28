# First student Дігтярьов Дмитро Вікторович
import csv
import json

"""
CSV file has structure:

    ID, Subject, Score
    1, Algorithms, 95

JSON file has structure:

    [
        {
            "ID": "1",
            "Subject": "Algorithms",
            "Score": "95"
        }
    ]
"""

# First student files Дігтярьов Дмитро Вікторович
csv_file = "data.csv"
json_file = "data.json"

# Second student file Дігтярьов Дмитро Вікторович
csv_output_file = "data_updated.csv"

# Data for files first student Дігтярьов Дмитро Вікторович
data_setup = [
    ["ID", "Subject", "Score"],
    ["1", "Algorithms", "95"],
    ["2", "Data Structures", "88"],
    ["3", "Operating Systems", "92"],
    ["4", "Computer Networks", "85"],
    ["5", "Databases", "93"]
]

# Data for files second student Дігтярьов Дмитро Вікторович
data_update = [
    {"ID": "6", "Subject": "Computer Science", "Score": "98"},
    {"ID": "7", "Subject": "System Modeling", "Score": "92"}
]

# First student Дігтярьов Дмитро Вікторович
# Create CSV
def create_csv_file():
    try:
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(data_setup)
        print(f"CSV file '{csv_file}' successfully created.")
    except Exception as e:
        print("Error creating CSV file:", e)

# Convert CSV to JSON
def convert_csv_to_json():
    try:
        with open(csv_file, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)

        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"Date from CSV file '{csv_file}' successfully converted to JSON file '{json_file}'.")
    except Exception as e:
        print("Convert failed CSV to JSON:", e)

# Second student Дігтярьов Дмитро Вікторович
# Convert JSON to CSV and add data
def convert_and_add_data_json_to_csv():
    try:
        # Read JSON
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Define the title
        if data:
            headers = data[0].keys()  # ["ID", "Subject", "Score"]
        # Default title
        else:
            headers = ["ID", "Subject", "Score"]

        # Written data to CSV
        with open(csv_output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
            writer.writerows(data_update)
        print(f"Data from JSON '{json_file}' convert to CSV '{csv_output_file}', add new row.")
    except Exception as e:
        print("Convert failure JSON to CSV:", e)

# First student Дігтярьов Дмитро Вікторович
while True:
    print("\nMenu:"
          "\n1 -> Create CSV and convert to JSON"
          "\n2 -> Convert JSON to CSV and add data"          
          "\n3 -> Exit\n")

    choice = input("Your choice: \n")

    if choice == "1":
        create_csv_file()
        convert_csv_to_json()
    elif choice == "2":
        convert_and_add_data_json_to_csv()
    elif choice == "3":
        print("Exit program.")
        break
    else:
        print("Error: invalid variant entered.")