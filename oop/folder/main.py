from storage import LocalStorage, MemoryStorage, UserService


def main() -> None:
    print("=== MEMORY STORAGE ===")
    memory_service = UserService(MemoryStorage())
    memory_service.save_user("user_1", {"name": "Alice", "age": 25})
    print("Saved user:", memory_service.get_user("user_1"))

    try:
        memory_service.get_user("missing_user")
    except KeyError as error:
        print("Missing record handled:", error)

    print("\n=== LOCAL STORAGE ===")
    local_service = UserService(LocalStorage("data"))
    local_service.save_user("user_2", {"name": "David", "age": 31})
    print("Saved user:", local_service.get_user("user_2"))

    # print("\n=== DELETE TEST ===")
    # local_service.delete_user("user_2")
    # try:
    #     local_service.get_user("user_2")
    # except KeyError as error:
    #     print("Record after deletion:", error)

    # print("\n=== ABSTRACT CLASS TEST ===")
    # from storage.base import Storage
    # try:
    #     Storage()
    # except TypeError as error:
    #     print("Cannot instantiate Storage:", error)


if __name__ == "__main__":
    main()
