import queue

def task(name, work_queue):
    while not work_queue.empty():
        count = work_queue.get()
        total = 0
        print(f"Task {name} running")
        for _ in range(count):
            total += 1
            yield
        print(f"Task {name} total: {total}")

def main():
    work_queue = queue.Queue()
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    tasks = [task("One", work_queue), task("Two", work_queue)]

    while tasks:
        for current_task in tasks.copy():
            try:
                next(current_task)
            except StopIteration:
                tasks.remove(current_task)

if __name__ == "__main__":
    main()



























# import queue

# def task(name, work_queue):
#     if work_queue.empty():
#         print(f"Task {name} nothing to do")
#         return

#     while not work_queue.empty():
#         count = work_queue.get()
#         total = 0
#         print(f"Task {name} running")
#         for _ in range(count):
#             total += 1
#         print(f"Task {name} total: {total}")

# def main():
#     work_queue = queue.Queue()
#     for work in [15, 10, 5, 2]:
#         work_queue.put(work)

#     tasks = [(task, "One", work_queue), (task, "Two", work_queue)]

#     for task_func, task_name, tasks_queue in tasks:
#         task_func(task_name, tasks_queue)

# if __name__ == "__main__":
#     main()










# from dataclasses import dataclass


# @dataclass
# class User:
#     name: str
#     email: str
#     age: int


# user = User(
#     name="John",
#     email="john@example.com",
#     age=25
# )

# print(user)



# # 2. Understanding the @dataclass decorator


# @dataclass(
#     init=True,
#     repr=True,
#     eq=True,
#     order=False,
#     frozen=False
# )
# class Product:
#     name: str
#     price: float




# # Use default_factory whenever you need a new mutable default value for each instance.









