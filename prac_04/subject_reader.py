"""
Tahlia Clennar
CP1404 Practical 4- Converting Data Strings to Lists
Program for converting Data Strings to Lists and displaying Subject details
"""
FILENAME = "subject_data.txt"


def main():
    """Get data as list of lists and display subject details"""
    data = get_data()
    print(data)
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data_lists = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        data_lists.append(parts)
    input_file.close()
    return data_lists


def display_subject_details(data):
    """Display subject details"""
    for part in data:
        print(f"{part[0]} is taught by {part[1]} and has {part[2]} students")


main()
