"""CP1404 Practical 7- Project Management
Tahlia Clennar
Time started: 8.14am
Estimated time: 1 hour
Actual time: 3 hours 30 minutes
"""
from operator import attrgetter

from prac_07.project import Project
import datetime

MENU = """Menu:
(L)oad projects
(S)ave projects
(D)isplay projects
(F)ilter projects by date
(A)dd a new project
(U)pdate project
(Q)uit"""


def main():
    """Allow user to load projects, save projects, display projects,
    filter projects by date, add new projects and update projects for a project text file."""
    projects = []
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Enter filename: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_projects(projects)
        elif choice == "U":
            update_projects(projects)
        elif choice == "Q":
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid menu choice")
            print(MENU)
        choice = input(">>> ").upper()


def save_projects(filename, projects):
    """Prompt the user for a filename to save projects to and save them"""
    output_file = open(filename, 'w')
    print(f"Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=output_file)
    for project in projects:
        print(f"{project.name}\t{project.start_date}\t{project.priority}\t"
              f"{project.cost_estimate}\t{project.completion_percentage}", file=output_file)


def load_projects(filename):
    """Prompt user for a filename to load projects from and load them"""
    projects = []
    input_file = open(filename, 'r')
    input_file.readline()
    for line in input_file:
        parts = line.strip().split("\t")
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    input_file.close()
    return projects


def display_projects(projects):
    """Display two groups: incomplete projects; completed projects, both sorted by priority"""
    print("Incomplete projects:")
    for project in projects:
        if not project.complete_project():
            print(f"\t{project}")
    print("Complete projects: ")
    for project in projects:
        if project.complete_project():
            print(f"\t{project}")


def filter_projects(projects):
    """Get date from user and display only projects that start after that date, sorted by date"""
    date_string = input("Show projects that start after date (d/m/yyyy): ")  # e.g., "30/9/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    projects.sort(key=attrgetter('start_date'))
    for project in projects:
        if date(project.start_date) >= date:
            print(project)


def add_projects(projects):
    """Get user inputs and add new project to memory"""
    print("Lets add a project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost Estimate: "))
    percent_complete = int(input("Percent complete: "))
    added_project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(added_project)


def update_projects(projects):
    """Allows a project to be chosen and modified"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choose_project = int(input("Project choice: "))
    update_project = projects[choose_project]
    print(update_project)
    try:
        percent_complete = int(input("New percentage: "))
        update_project.completion_percentage = percent_complete
    except ValueError:
        pass
    try:
        priority = int(input("New priority: "))
        update_project.priority = priority
    except ValueError:
        pass


if __name__ == '__main__':
    main()
