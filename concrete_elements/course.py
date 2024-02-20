from elements.element import Element

class Course(Element):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def accept(self, visitor):
        visitor.visit_course(self)
