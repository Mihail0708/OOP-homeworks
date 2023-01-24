from todo.project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        counter = 0
        for task in filter(lambda t: t.completed, self.tasks):
            counter += 1
            self.tasks.remove(task)

        return f"Cleared {counter} tasks."

    def view_section(self):
        result = [f'Section {self.name}:']
        for el in self.tasks:
            result.append(el.details())

        return '\n'.join(result)


