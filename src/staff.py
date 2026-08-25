"""Staff model for the hospital management system."""

from src.person import Person


class Staff(Person):
    """Represent a hospital staff member assigned to a department."""

    def __init__(self, name: str, age: int, position: str, department: str) -> None:
        """Initialize a staff member with their role and department."""
        super().__init__(name, age)
        self.position: str = position
        self.department: str = department

    def view_info(self) -> str:
        """Return the staff member's personal and work information."""
        return (
            f"{super().view_info()}, Position: {self.position}, "
            f"Department: {self.department}"
        )
