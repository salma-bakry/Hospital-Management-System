class Person:
    """Represent a person in the hospital system."""

    def __init__(self, name: str, age: int) -> None:
        """
        Initialize a Person object.

        Args:
            name: The person's name.
            age: The person's age.
        """
        self.name: str = name
        self.age: int = age

    def view_info(self) -> str:
        """
        Return basic information about the person.

        Returns:
            A string containing the person's name and age.
        """
        return f"Name: {self.name}, Age: {self.age}"    