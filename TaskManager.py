import json
from datetime import datetime

class TaskManager:
  def __init__(self):
    self.file_path = "data/user_tasks.json"
    self.load_data()
  
  def load_data(self):
    with open(self.file_path, 'r') as file:
      self.data = json.load(file)
      
  def save_data(self):
    with open(self.file_path, 'w') as file:
      json.dump(self.data, file, indent=2)
    
  def new_task(self, user, task, points, notes):
    new_task = {
        "task": task,
        "points": points,
        "notes": notes,
        "done": False
    }
    self.data["users"][user]["tasks"].append(new_task)
    self.save_data()
    print("New Task added perfectly")
  
  def task_done(self, user, task):
    for t in self.data["users"][user]["tasks"]:
      if t["task"] == task and not t["done"]:
        t["done"] = True
        t["completed_at"] = str(datetime.now())
        self.data["users"][user]["completed_tasks"].append(t)
        self.data["users"][user]["tasks"].remove(t)
        self.data["users"][user]["total_points"] += int(t["points"])
        self.save_data()
        return True
    return False
  
  
  
if __name__ == "__main__":
  # manager = TaskManager()
  # manager.new_task("ftleo", "Test", "10", None)
  # manager.task_done("ftleo", "Test")
  pass