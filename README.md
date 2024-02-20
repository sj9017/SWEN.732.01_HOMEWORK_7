# RIT Visitor Pattern Project

This project demonstrates the Visitor design pattern in the context of Rochester Institute of Technology (RIT). The Visitor pattern allows you to define operations (visitors) on elements without changing their structure.

## Project Structure

- **`visitors/`**: Contains the visitor interface.
  - `visitor.py`: Defines the `Visitor` interface.

- **`elements/`**: Contains the element interface.
  - `element.py`: Defines the `Element` interface.

- **`concrete_elements/`**: Contains the concrete elements.
  - `department.py`: Implements the `Department` class.
  - `course.py`: Implements the `Course` class.

- **`concrete_visitors/`**: Contains the concrete visitors.
  - `print_visitor.py`: Implements the `PrintVisitor` class.

- **`main.py`**: The main entry point for the project where elements, visitors, and the Visitor pattern are demonstrated.