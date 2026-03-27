import csv
from pathlib import Path

# Default grades file path located beside this module
GRADES_PATH = Path(__file__).parent / 'grades.csv'

# Standard CSV header used by writers and readers
HEADER = ['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3']

def write_grades_interactive(filename=GRADES_PATH):
	"""
	Prompt the instructor to enter student records and write them to a CSV file.

	Parameters:
		filename (str): The output CSV filename to write student records into.

	Variables:
		count (int): Number of students the instructor wants to enter.
		header (list[str]): CSV header row written to the file.
		rows (list[list]): Accumulated student rows to write.
		first (str): Entered first name for the current student.
		last (str): Entered last name for the current student.
		exams (list[int]): Collected integer exam grades for the current student.

	Return:
		None: Writes data to disk and prints a confirmation message.
	"""
	while True:
		try:
			count = int(input('How many students do you want to enter? '))
			if count < 0:
				raise ValueError
			break
		except ValueError:
			print('Please enter a non-negative integer for the number of students.')

	header = HEADER
	# Ensure filename is a Path (accepts str or Path)
	filename = Path(filename)
	rows = []
	for i in range(count):
		print(f"Entering student {i+1} of {count}")
		first = input('First name: ').strip()
		last = input('Last name: ').strip()
		exams = []
		for e in range(1, 4):
			while True:
				try:
					val = int(input(f'Exam {e} grade (integer): '))
					exams.append(val)
					break
				except ValueError:
					print('Please enter an integer grade.')

		rows.append([first, last, exams[0], exams[1], exams[2]])

	# Write collected rows to CSV using the with context manager
	with filename.open('w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(header)
		writer.writerows(rows)

	# Confirm the write including the absolute path for clarity
	print(f'Wrote {len(rows)} student(s) to {filename.resolve()}')

def write_grades_from_list(students, filename=GRADES_PATH):
	"""
	Write student records provided as an iterable of tuples/lists into a CSV file.

	Parameters:
		filename (str): The output CSV filename.
		students (iterable[tuple|list]): Each item should be
			(first, last, exam1, exam2, exam3) where exam* are integers.

	Variables:
		header (list[str]): CSV header row written to the file.

	Return:
		None: Writes the provided student data to `filename`.
	"""
	# Ensure filename is a Path and write rows
	filename = Path(filename)
	with filename.open('w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(HEADER)
		writer.writerows(list(students))

def read_grades(filename=GRADES_PATH):
	"""
	Read the grades CSV file and display its contents in a tabular format.

	Parameters:
		filename (str): Path to the CSV file to read.

	Variables:
		rows (list[list]): All rows read from the CSV (including header).
		header (list[str]): The first row interpreted as column names.
		data (list[list]): Remaining rows containing student records.
		cols (list[tuple]): Columns transposed for width calculation.
		widths (list[int]): Calculated max width per column for formatting.
		sep (str): Column separator used when printing the table.
		line (str): Formatted header line printed to stdout.

	Return:
		None: Prints a formatted table to stdout or an error message.
	"""
	# Ensure filename is a Path and exists
	filename = Path(filename)
	if not filename.exists():
		print(f'File not found: {filename}')
		return

	# Read all rows using the csv module and a context manager
	with filename.open('r', newline='') as csvfile:
		reader = csv.reader(csvfile)
		rows = list(reader)

	if not rows:
		print('CSV is empty')
		return

	header = rows[0]
	data = rows[1:]

	# Compute column widths robustly by transposing rows into columns
	cols = list(zip(*([header] + data))) if data else [[h] for h in header]
	widths = [max(len(str(item)) for item in col) for col in cols]

	# Build and print the header and a separator line
	sep = ' | '
	line = sep.join(h.ljust(w) for h, w in zip(header, widths))
	print(line)
	print('-' * len(line))

	# Print each data row aligned to the calculated column widths
	for row in data:
		print(sep.join(str(cell).ljust(widths[i]) for i, cell in enumerate(row)))

if __name__ == '__main__':
	# Use the grades.csv file located in this exercise's folder
	try:
		write_grades_interactive()
		print('\nContents of the created file:')
		read_grades()
	except KeyboardInterrupt:
		print('\nInput cancelled by user.')
