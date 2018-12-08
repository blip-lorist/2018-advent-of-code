import string

class TaskManager():
    # Generates tasks to give to workers
    # Pushes completed tasks to a finished list
    def __init__(self, task_queue, prereqs):
        self.queue = task_queue
        self.prereqs = prereqs
        self.finished_tasks = []
        self.total_task_count = len(self.queue)

    def get_next_task(self):
        if len(self.queue) == 0:
            return None

        available_tasks = []
        for task_name in self.queue:
            if self.grant_permission(task_name):
                available_tasks.append(task_name)

        available_tasks = sorted(available_tasks)
        if len(available_tasks) == 0:
            return None

        new_task_name = available_tasks.pop(0)
        self.queue.remove(new_task_name)
        return Task(new_task_name)

    def grant_permission(self, task_name):
        task_prereqs = self.prereqs.get(task_name, None)

        if task_prereqs is None:
            return True

        for prereq in task_prereqs:
            if prereq not in self.finished_tasks:
                return False


        return True

    def mark_done(self, task):
        self.finished_tasks.append(task.name)

    def all_tasks_complete(self):
        if len(self.finished_tasks) == self.total_task_count:
            return True

        return False

class Worker:

    def __init__(self):
        self.assigned_task = None
        self.status = "idle"

    def receive_task(self, task):
        self.assigned_task = task

    def do_work(self):
        if self.status == "working":
            task = self.assigned_task
            task.remaining_time -= 1

    def is_finished(self):
        task = self.assigned_task
        if task is None:
            return False

        if task.remaining_time == 0:
            return True

        return False

class Task:
    def __init__(self, name):
        self.name = name
        self.remaining_time = (string.ascii_uppercase.index(self.name) + 1) + 60

def get_permissions_lookup():
    #input_file = "mini_input.txt"
    input_file = "input.txt"
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
    #task_queue = list("CABFDE")
    task_queue = list("AHJDBEMNFQUPVXGCTYLWZKSROI")
    permissions = get_permissions_lookup()
    task_manager = TaskManager(task_queue, permissions)
    pool = []
    for num in range(1,6):
        pool.append(Worker())


    ## Workers are assigned work
    #for worker in pool:
    #    next_task = task_manager.get_next_task()
    #    worker.receive_task(next_task)

    elapsed_seconds = 0
    while not task_manager.all_tasks_complete():
    # Second starts
        print("Second {}".format(elapsed_seconds))

        # debugging
        #workers_with_tasks = [worker for worker in pool if worker.assigned_task is not None]
        #if elapsed_seconds > 0 and len(task_manager.queue) > 5 and len(workers_with_tasks) != 5:
        #    raise Exception("Not all workers have tasks")

        # Workers check if they can start work
        for idx, worker in enumerate(pool):

            # Check if workers are finished, mark tasks complete
            if worker.is_finished():
                task_manager.mark_done(worker.assigned_task)
                worker.assigned_task = None
                worker.status = "idle"

            # Assign work if worker is available
            if worker.status == "idle" and worker.assigned_task is None:
                next_task = task_manager.get_next_task()
                worker.receive_task(next_task)

            # Check if workers have permission to start
            print("Worker {}".format(idx + 1))
            task = worker.assigned_task

            if task is not None and task_manager.grant_permission(task.name):
                worker.status = "working"
                print(worker.assigned_task.name)
            else:
                worker.status = "idle"
                print(".")


            worker.do_work()


        # second ends
        print("Finished tasks")
        print(task_manager.finished_tasks)
        print("")

        if not task_manager.all_tasks_complete():
            elapsed_seconds += 1


    print("Total elapsed seconds {}".format(elapsed_seconds))


main()
