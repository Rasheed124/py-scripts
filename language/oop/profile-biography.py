
class Profile:
    def __init__(
        self,
        name: str,
        biography: str | None = None
    ):
        self.__name = name.strip()
        self.__biography = biography

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self.__name = value.strip()

    @property
    def biography(self) -> str | None:
        return getattr(self, "_Profile__biography", None)

    @biography.setter
    def biography(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Biography must be a string")

        if not value.strip():
            raise ValueError("Biography can't be empty")

        if len(value.strip()) <= 10:
            raise ValueError("Biography must be greater than 10 characters")

        self.__biography = value.strip()

    @biography.deleter
    def biography(self):
        self.__biography = None
        print("Biography deleted successfully")

    def __str__(self):
        biography = self.biography
        if biography is None:
            biography = "No biography available"

        return f"{self.__name} has a biography of {biography}"


user1 = Profile("Adeola")

user1.biography = (
    "Am a fenfenfe enfkjefnwufbw wfnwnfwbfbwkjf "
    "wnfiwnfujnefbwefwf wfwnfnwiufeuwf"
)

del user1.biography

print(user1)
