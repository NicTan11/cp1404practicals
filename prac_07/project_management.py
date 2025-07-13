"""
CP1404/CP5632 Practical
Project Management Program
Estimated time: 3 hours
Actual time: 2.5 hours
"""

import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """Main function to run the project management program."""
    print("Welcome to Pythonic Project Management")
    
    # Load projects from default file at startup
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
    
    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").upper()
        
        if choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Filename: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            project = add_project()
            projects.append(project)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
            save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? ").lower()
            if save_choice.startswith('y'):
                save_projects(DEFAULT_FILENAME, projects)
                print(f"Saved {len(projects)} projects to {DEFAULT_FILENAME}")
        else:
            print("Invalid choice")
    
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    try:
        with open(filename, 'r') as file:
            file.readline()  # Skip header
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split('\t')
                    if len(parts) >= 5:
                        name = parts[0]
                        start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
                        priority = int(parts[2])
                        cost_estimate = float(parts[3])
                        completion_percentage = int(parts[4])
                        project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                        projects.append(project)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except (ValueError, IndexError) as e:
        print(f"Error loading projects: {e}")
    
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    try:
        with open(filename, 'w') as file:
            file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
            for project in projects:
                file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
    except IOError as e:
        print(f"Error saving projects: {e}")


def display_projects(projects):
    """Display projects grouped by incomplete and completed, sorted by priority."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]
    
    incomplete_projects.sort()
    completed_projects.sort()
    
    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"  {project}")
    
    print("Completed projects: ")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter and display projects that start after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    try:
        # Handle both dd/mm/yy and dd/mm/yyyy formats
        try:
            filter_date = datetime.datetime.strptime(date_string, "%d/%m/%y").date()
        except ValueError:
            filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        
        filtered_projects = [project for project in projects if project.is_started_after(filter_date)]
        filtered_projects.sort(key=lambda x: x.start_date)
        
        for project in filtered_projects:
            print(project)
    except ValueError:
        print("Invalid date format")


def add_project():
    """Add a new project by getting user input."""
    print("Let's add a new project")
    name = input("Name: ")
    
    while True:
        try:
            date_string = input("Start date (dd/mm/yy): ")
            try:
                start_date = datetime.datetime.strptime(date_string, "%d/%m/%y").date()
            except ValueError:
                start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Invalid date format")
    
    while True:
        try:
            priority = int(input("Priority: "))
            break
        except ValueError:
            print("Invalid input; enter a valid number")
    
    while True:
        try:
            cost_string = input("Cost estimate: $")
            if cost_string.startswith('$'):
                cost_string = cost_string[1:]
            cost_estimate = float(cost_string)
            break
        except ValueError:
            print("Invalid input; enter a valid number")
    
    while True:
        try:
            completion_percentage = int(input("Percent complete: "))
            break
        except ValueError:
            print("Invalid input; enter a valid number")
    
    return Project(name, start_date, priority, cost_estimate, completion_percentage)


def update_project(projects):
    """Update a project's completion percentage and/or priority."""
    if not projects:
        print("No projects to update")
        return
    
    # Display all projects with indices
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    
    while True:
        try:
            choice = int(input("Project choice: "))
            if 0 <= choice < len(projects):
                break
            else:
                print("Invalid project number")
        except ValueError:
            print("Invalid input; enter a valid number")
    
    project = projects[choice]
    print(project)
    
    # Update completion percentage
    new_percentage_input = input("New Percentage: ")
    if new_percentage_input.strip():
        try:
            new_percentage = int(new_percentage_input)
            project.update_completion(new_percentage)
        except ValueError:
            print("Invalid percentage")
    
    # Update priority
    new_priority_input = input("New Priority: ")
    if new_priority_input.strip():
        try:
            new_priority = int(new_priority_input)
            project.update_priority(new_priority)
        except ValueError:
            print("Invalid priority")


if __name__ == "__main__":
    main() 