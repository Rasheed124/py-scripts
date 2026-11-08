from users.user import User


class Admin(User):
    @property
    def admin_id(self):
        return self.user_id

    def __str__(self):
        return f"Admin: {self.name}"
