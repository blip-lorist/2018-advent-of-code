class TaskManager():
    # Generates tasks to give to workers
    # Pushes completed tasks to a finished list
    def __init__(self, task_queue):
        self.queue = task_queue
        self.finished_tasks = []

    def get_next_task(self):
        if len(self.queue) == 0:
            raise Exception("No more tasks!")

        new_task_name = self.queue.pop(0)
        return Task(new_task_name)


class Worker:
    # After initializing, a worker will
    # - retrieve a task from the task manager
    # - Check if the task can be started
    # - track time remaining for the task

    def __init__(self):
        self.current_task = None
        self.time_remaining_on_task = None
        self.can_start = False

    def receive_task(self, task):
        self.current_task = task.name

class Task:
    def __init__(self, name):
        self.name = name




def main():
    # Instantiate task manager and workers
    task_queue = list("CABFDE")
    task_manager = TaskManager(task_queue)
    worker_one = Worker()
    worker_two = Worker()
    pool = [worker_one, worker_two]

    # Workers are assigned work
    for worker in pool:
        next_task = task_manager.get_next_task()
        worker.receive_task(next_task)

    import pdb; pdb.set_trace()


main()
