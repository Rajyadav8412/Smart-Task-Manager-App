import json
import heapq

def build_priority_queue(tasks):
    heap = []

    for task in tasks:
        # (priority, task)
        heapq.heappush(heap, (task.priority, task))

    return heap


def get_next_task(heap):
    if not heap:
        return None

    return heapq.heappop(heap)[1]

def save_tasks(tasks):
    data = [task.to_dict() for task in tasks]

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


def load_tasks():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

            return data
    except:
        return []
    
def search_tasks(tasks, keyword):
    result = []

    for task in tasks:   # Linear Search
        if keyword.lower() in task.title.lower():
            result.append(task)

    return result

def sort_tasks(tasks):
    return sorted(tasks, key=lambda x: (x.priority, x.due_date))

def get_highest_priority_task(tasks):
    if not tasks:
        return None

    highest = tasks[0]

    for task in tasks:
        if task.priority < highest.priority:
            highest = task

    return highest