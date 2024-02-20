from concrete_elements.department import Department
from concrete_elements.course import Course
from concrete_visitors.print_visitor import PrintVisitor

if __name__ == "__main__":

    # Creating elements
    se_department = Department("Software Engineering")
    cs_department = Department("Computer Science")
    

    programming_course = Course("Collaborative Software Development", "SWEN732")
    circuits_course = Course("Algorithm Fundamentals", "CSCI402")

    # Adding elements to a list
    elements = [cs_department, se_department, programming_course, circuits_course]

    # Creating a visitor
    visitor = PrintVisitor()

    # Accepting the visitor for each element
    for element in elements:
        element.accept(visitor)
