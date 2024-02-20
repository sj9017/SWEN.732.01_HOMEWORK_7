from visitors.visitor import Visitor

class PrintVisitor(Visitor):
    def visit_department(self, department):
        print(f"Visited Department: {department.name}")

    def visit_course(self, course):
        print(f"Visited Course: {course.name} ({course.code})")
