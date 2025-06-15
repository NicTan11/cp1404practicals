"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display it."""
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer
        subjects.append(parts)  # Add the parts as a new list to subjects
    input_file.close()
    return subjects


def display_subject_details(subjects):
    """Display details of each subject."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
