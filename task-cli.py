#!/usr/bin/env python3
import sys,json,os
from datetime import datetime
FILE='tasks.json'
VALID_STATUS={"todo","in-progress","done"}

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
