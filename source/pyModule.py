"""Short description of the module within a single line.

Here comes the long description of the module.
It can be many lines.
Same max character lengths as comments (72 characters).
More info on docstrings:
https://realpython.com/documenting-python-code/
"""

# The blank line above is because of docstrings. Code goes below this line.
def greet(name: str = "World"):
    """Greet the caller with its name or the default."""

    print("Hello " + name)

class SimpleClass:
    """Class docstrings go here."""

    greeting_str = "Hello {name}"

    def __init__(self, name):
        """Constructor"""
 
        self.name = name

    def say_hello(self, name: str):
        """Class method docstrings go here."""

        print(self.greeting_str.format(name=name))
        print(f"My name is {self.name}.")