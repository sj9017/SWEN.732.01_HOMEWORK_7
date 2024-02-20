from elements.element import Element

class Department(Element):
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        visitor.visit_department(self)
