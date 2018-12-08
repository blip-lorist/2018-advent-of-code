class TaskManager():
    # Generates tasks to give to workers
    # Pushes completed tasks to a finished list
    def __init__(self, task_queue, prereqs):
        self.queue = task_queue
        self.prereqs = prereqs
        self.finished_tasks = []

    def get_next_task(self):
        if len(self.queue) == 0:
            raise Exception("No more tasks!")

        new_task_name = self.queue.pop(0)
        return Task(new_task_name)

    def grant_permission(self, task):
        task_prereqs = self.prereqs.get(task, None)

        if task_prereqs is None:
            return True

        for prereq in task_prereqs:
            if prereq not in self.finished_tasks:
                return False

            return True

class Worker:
    # After initializing, a worker will
    # - retrieve a task from the task manager
    # - Check if the task can be started
    # - track time remaining for the task

    def __init__(self):
        self.assigned_task = None
        self.status = "idle"

    def receive_task(self, task):
        self.assigned_task = task.name

class Task:
    def __init__(self, name):
        self.name = name




def get_permissions_lookup():
    input_file = "mini_input.txt"
    #input_file = "input.txt"
    with open(input_file, "r") as f:
        steps = f.readlines()

    steps = [x.strip() for x in steps]

    prereq_lookup = {}

    # Build prereq dictionary for each step
    for step in steps:
        step = step.split(" ")
        prereq_step = step[1]
        next_step = step[7]

        if next_step in prereq_lookup.keys():
            prereq_lookup[next_step].add(prereq_step)
        else:
            prereq_lookup[next_step] = set(prereq_step)

    return prereq_lookup


def main():
    # Instantiate task manager and workers
    task_queue = list("CABFDE")
    permissions = get_permissions_lookup()
    task_manager = TaskManager(task_queue, permissions)
    worker_one = Worker()
    worker_two = Worker()
    pool = [worker_one, worker_two]

    # Workers are assigned work
    for worker in pool:
        next_task = task_manager.get_next_task()
        worker.receive_task(next_task)

    elapsed_seconds = 0
    while len(task_manager.finished_tasks) < len(task_queue):
    # Second starts
        # Workers check if they can start work
        for worker in pool:
            if task_manager.grant_permission(worker.assigned_task):
                worker.status = "working"
            else:
                worker.status = "idle"

        import pdb; pdb.set_trace()
             # Workers check if they can mark work finished
             # Print
                # second
                # worker's current task
                # finished tasks
        # second ends



main()
