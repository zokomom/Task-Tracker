#!/usr/bin/env python3
"""
task-cli.py - simple task tracker CLI (single-file)
Usage:
  python3 task-cli.py add "Buy groceries"
  python3 task-cli.py update 1 "New description"
  python3 task-cli.py delete 1
  python3 task-cli.py mark-in-progress 1
  python3 task-cli.py mark-done 1
  python3 task-cli.py list
  python3 task-cli.py list done
"""

import sys,json,os
from datetime import datetime
FILE='tasks.json'
VALID_STATUS={"todo","in-progress","done","all"}

def new_iso():
    return datetime.utcnow().replace(microsecond=0).isoformat()+'Z'

def ensure_file():
    if not os.path.exists(FILE):
        with open(FILE,"w") as f:
            json.dump([],f)

def load_tasks():
    ensure_file()
    try:
        with open(FILE,"r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        backup = FILE + ".bak"
        os.replace(FILE,backup)
        print(f"Warning: {FILE} was corrupted. Backed up to {backup}. Starting fresh.")
        with open(FILE,"w") as f:
            json.dump([],f)
        return []
def save_tasks(tasks):
    tmp=FILE+".tmp"
    with open(tmp,"w") as f:
        json.dump(tasks,f,indent=2)
    os.replace(tmp,FILE)

def next_id(tasks):
    if not tasks:
        return 1 
    return max(t.get("id",0)for t in tasks)+1

def find_task(tasks,id_):
    for t in tasks:
        if t.get("id")==id_:
            return t
    return None
def add_cmd(description):
    if not description.strip():
        print("Error: Description cannot be empty.")
        return
    tasks=load_tasks()
    nid=next_id(tasks)
    t={
        "id": nid,
        "description": description,
        "status": "todo",
        "createdAt": new_iso(),
        "updatedAt": new_iso()
    }
    tasks.append(t)
    save_tasks(tasks)
    print(f"Task added successfully (ID {nid})")

def list_cmd(filter_status=None):
    tasks=load_tasks()
    if filter_status not in VALID_STATUS:
        print("Error: Invalid status. Use one of:",", ".join(VALID_STATUS))
        return
    if filter_status == "all":
        tasks = tasks
    else:
        tasks=[t for t in tasks if t.get("status")==filter_status]
        if not tasks:
            print("No tasks found.")
            return

    print(f"{'ID':<4} {'Status':<12} {'Description':<40} {'UpdatedAt'}")
    print("-"*90)
    for t in tasks:
        id_=t.get("id")
        status=t.get("status")
        desc=t.get("description")
        updated=t.get("updatedAt")
        if len(desc)>37:
            desc=desc[:34]+"..."
        print(f"{id_:<4} {status:<12} {desc:<40} {updated}")

def update_cmd(id_str,new_desc):
    try:
        id_ = int(id_str)
    except ValueError:
        print("Error: ID must be an number.")
        return
    if not new_desc.strip():
        print("Error: Description cannot be empty.")
        return
    tasks=load_tasks()
    t=find_task(tasks,id_)
    if not t:
        print(f"Error: No task with ID {id_}.")
        return
    t["description"]=new_desc
    t["updatedAt"]=new_iso()
    save_tasks(tasks)
    print(f"Task {id_} updated successfully.")

def delete_cmd(id_str):
    try:
        id_ = int(id_str)
    except ValueError:
        print("Error: ID must be an number.")
        return
    tasks=load_tasks()
    t=find_task(tasks,id_)
    if not t:
        print(f"Error: Task with ID {id_} not found.")
        return
    tasks=[task for task in tasks if task.get("id")!=id_]
    save_tasks(tasks)
    print(f"Task deleted successfully (ID {id_})")

def mark_cmd(id_str,status):
    try:
        id_ = int(id_str)
    except ValueError:
        print("Error: ID must be an number.")
        return
    if status not in VALID_STATUS:
        print("Error: Invalid status. Use one of:",", ".join(VALID_STATUS))
        return
    tasks=load_tasks()
    t=find_task(tasks,id_)
    if not t:
        print(f"Error: Task with ID {id_} not found.")
        return
    t["status"]=status
    t["updatedAt"]=new_iso()
    save_tasks(tasks)
    print(f"Task marked {status} (ID:{id_})")

def usage():
    print(__doc__)

def main(argv):
    if len(argv)<2:
        usage() 
        return
    cmd=argv[1]
    if cmd=="add":
        if len(argv)<3:
            print("Error: description required. Example: add \"Buy groceries\"")
            return
        add_cmd(argv[2])
    elif cmd=="list":
        if len(argv)==2:
            list_cmd()
        elif len(argv)==3:
            list_cmd(argv[2])
        else:
            print("Error: wrong usage of list.")
            return
    elif cmd=="update":
        if len(argv)<4:
            print("Error: usage: update <id> \"new description\"")
            return
        update_cmd(argv[2],argv[3])
    elif cmd=="delete":
        if len(argv)<3:
            print("Error: usage: delete <id>")
            return
        delete_cmd(argv[2])
    elif cmd=="mark-in-progress":
        if len(argv)<3:
            print("Error: usage: mark-in-progress <id>")
            return
        mark_cmd(argv[2],"in-progress")
    elif cmd=="mark-done":
        if len(argv)<3:
            print("Error: usage: mark-done <id>")
            return
        mark_cmd(argv[2],"done")
    else:
        print(f"Error: unknown command '{cmd}'")
        usage()
if __name__=="__main__":
    main(sys.argv)