import csv


def process_csv():

    input_file = "employees.csv"
    output_file = "employees_valid.csv"
    valid_records = []
    total_salary = 0
    valid_count = 0
    invalid_count = 0

    try:

        print("Reading employees.csv...\n")

        with open(input_file, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row_number, row in enumerate(reader, start=2):

                try:

                    if row["name"].strip() == "":
                        print(f"Row {row_number}: Missing Name - Skipping")
                        invalid_count += 1
                        continue

                    if row["email"].strip() == "":
                        print(f"Row {row_number}: Missing Email - Skipping")
                        invalid_count += 1
                        continue

                    if "@" not in row["email"]:
                        print(f"Row {row_number}: Invalid Email - Skipping")
                        invalid_count += 1
                        continue


                    age = int(row["age"])

                    salary = float(row["salary"])
                    total_salary += salary
                    valid_count += 1
                    valid_records.append(row)

                except ValueError:

                    print(f"Row {row_number}: Invalid Age or Salary - Skipping")
                    invalid_count += 1

        print("\n===== Summary =====")
        print(f"Valid Records   : {valid_count}")
        print(f"Invalid Records : {invalid_count}")

        if valid_count > 0:
            average_salary = total_salary / valid_count
            print(f"Average Salary  : Rs {average_salary:,.2f}")
            print(f"Total Employees : {valid_count}")


        print("\nWriting Valid Records...")
        with open(output_file, "w", newline="") as file:
            fieldnames = ["name", "age", "email", "salary"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(valid_records)

        print("File written successfully.")

    except FileNotFoundError:
        print("Error: CSV file not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except csv.Error:
        print("Error: Malformed CSV file.")

    except IOError:
        print("Error: File I/O Error.")


process_csv()

