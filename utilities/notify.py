import time, datetime, os, sys, json
from win10toast import ToastNotifier
# pip install win10toast

users_dir = os.path.join(os.path.dirname(sys.path[0]),'todolists')
icon_dir = os.path.join(os.path.dirname(sys.path[0]),'ui\\images\\notification.ico')
os.makedirs(users_dir, exist_ok=True)

n = ToastNotifier()

def start_service(username):
    while True:
        with open(f"{users_dir}\\{username}\\{username}.json") as fileobj:
            try:
                tasks = json.load(fileobj)
            except Exception as e:
                tasks = []
        
        if len(tasks) == 0:
            time.sleep(10)
        else:
            taskObj = tasks[0]
            current_time = int(datetime.datetime.now().strftime("%Y%m%d%p%I%M").replace('PM','1').replace('AM','0'))
            diff = int(taskObj['reminder']) - current_time
            if diff <= 0:
                print('notified')
                n.show_toast(taskObj['task'], 'Due on: '+ taskObj['due_date'], duration=7, icon_path = icon_dir)
                tasks.pop(0)
                with open(f"{users_dir}\\{username}\\{username}.json",'w') as fileObj:
                    fileObj.write(json.dumps(tasks))
            else:
                # sleep
                time.sleep(10)

start_service('Mihir')

# {"task": "watch movie", "due_date": "No Due Date", "dueSortKey": "99991231", "reminder": 2022042310521}