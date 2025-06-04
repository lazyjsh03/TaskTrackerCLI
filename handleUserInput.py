import cmd
import shlex
import json
import os

JSON_FILE = "tasks.json"

tasks = {}
id = 1

def load_data():
    global tasks, id
    try:
        if os.path.exists(JSON_FILE):
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                json_tasks = data.get("tasks", {})
                tasks = {int(key): value for key, value in json_tasks.items()}
                id = data.get("id", 1)
        else:
            tasks = {}
            id = 1
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Warning: cannot load '{JSON_FILE}' start with new file.")
        tasks = {}
        id = 1

def save_data():
    global tasks, id
    
    data_to_save = {
        "next-id": id,
        "tasks": tasks
    }
    try:
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)
    except IOError:
        print(f"Error: cannot save tasks in '{JSON_FILE}'.")


class TaskTracker(cmd.Cmd):
    prompt = "TaskCLI>> "  # prompt style
    intro = 'Welcome to TaskTrackerCLI. Type "help" for available commands'

    def do_help(self, arg):
        return super().do_help(arg)
    
    def do_create(self, arg):
       global id
       content = input("Type task content>> ")
       tasks[id] = {'content': content, 'check': False}
       print(f"Task id {id} created - {content} [ ]")
       id += 1
       save_data()

    def do_show(self, arg):
        if not tasks:
            print("No tasks to show.")
            return
        print("---------------< Tasks >---------------\n")
        for key, value in tasks.items():
            status = "[v]" if value['check'] else "[ ]"
            print(f"{status} {key}. {value['content']}")
        print("---------------------------------------\n")

    def do_update(self, arg):
        global id
        args = self._parse_args(arg)
        if (int(args[0]) <= id and int(args[0]) >= 1):
            if int(args[0]) in tasks:
                old_content = tasks[int(args[0])]
                content = input("Type new content>> ")
                tasks[int(args[0])] = content
                print(f"Update complete - task id {int(args[0])}: {old_content} => {content}")
                save_data()
            else:
                print(f"Invalid id: {int(args[0])}")
                return
        else:
            print("Invalid id - id does not exist")
            return
                
    def do_delete(self, arg):
        global id
        args = self._parse_args(arg)
        if (int(args[0]) <= id and int(args[0]) >= 1):
            if int(args[0]) in tasks:
                print(f"Delete complete - task id {int(args[0])}")
                del tasks[int(args[0])]
                save_data()
            else:
                print(f"Invalid id: {int(args[0])}")
                return
        else:
            print("Invalid id - id does not exist")
            return
        
    def do_check(self, arg):
        global id
        args = self._parse_args(arg)
        if (int(args[0]) <= id and int(args[0]) >= 1):
            if int(args[0]) in tasks:
                print(f"Checked - task id {int(args[0])}")
                if (tasks[int(args[0])]['check']):
                    tasks[int(args[0])]['check'] = False
                else:
                    tasks[int(args[0])]['check'] = True
                save_data()
            else:
                print(f"Invalid id: {int(args[0])}")
                return
        else:
            print("Invalid id - id does not exist")
            return
        
    def do_exit(self, arg):
        print("Bye!!")
        return True
    
    def _parse_args(self, arg):
        if not arg:
            return []
        try:
            return shlex.split(arg)
        except ValueError:
            print("Parsing Error: Check command")
            return []

    def emptyline(self):
        pass

    def default(self, line):
        print(f"Invalid command: '{line}'. Type 'help'")
    
if __name__ == "__main__":
    load_data()
    cli_app = TaskTracker()
    try:
        cli_app.cmdloop()
    except KeyboardInterrupt:
        print("\nExit Application. (Ctrl + C)")
        save_data()
