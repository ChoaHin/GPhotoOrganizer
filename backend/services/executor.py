def execute(tasks, functions, context):
    executed = set()

    def run(task):
        if task in executed:
            return
        
        for dep in tasks.get(task, []):
            run(dep)

        print(f"Executing task: {task}")
        functions[task](context)
        executed.add(task)

    for task in tasks:
        run(task)