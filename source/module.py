"""Short description of the module within a single line.

Here comes the long description of the module.
It can be many lines.
Same max character lengths as comments (72 characters).
More info on docstrings:
https://realpython.com/documenting-python-code/
"""


def greet(name: str = "World"):
    """Greet the caller with its name or the default.

    :param name: Name of the caller, defaults to "World"
    :param name: str, optional
    """

    print("Hello " + name)


class SimpleClass:
    """Class docstrings go here."""

    greeting_str = "Hello {name}"

    def __init__(self, name: str):
        """Define name of class itself within constructor.

        :param name: Name of the class itself.
        :type name: str
        """

        self.name = name

    def say_hello(self, name: str):
        """Docstring for method of class goes here.

        :param name: Name of person to be greeted
        :type name: str
        """

        print(self.greeting_str.format(name=name))
        print(f"My name is {self.name}.")
