import csv


# Put the full path to your CSV/Excel file here
MY_FILE = "../data/sample_sfpd_incident_all.csv"


def parse(raw_file,delimiter):
	"""Parses a raw CSV file into a JSON like object."""

	# Open CSV file, and safely close it when we are done.
	opened_file = open(raw_file)

	#Read the data from the CSV file.
	csv_data = csv.reader(opened_file, delimiter=delimiter)

	# Setup an empty list
	parsed_data = []

	# Skip over first line for headers of the CSV file.
	fields = csv_data.next()

	# Iterate over each row of the csv file. Relate together field with value.
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))

	# Close the file
	opened_file.close()

	return parsed_data

def main():
	# Call the parse function and give it the needed parameters
	new_data = parse(MY_FILE, ",")

	# Let's see what we got.
	print new_data

if __name__ == "__main__":
	main()