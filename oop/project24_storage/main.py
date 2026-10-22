from storage import MemoryStorage, LocalStorage, UserService




def main() -> None:
    storage = MemoryStorage()
    user_service = UserService(storage)

    user_service.save_user("user_1", {"name": "Alice", "age": 25})

    user = user_service.get_user("user_1")
    print(user)
    

if __name__ == "__main__":
    main()
