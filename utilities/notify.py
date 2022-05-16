import time, datetime, os, sys, json
from win10toast import ToastNotifier
import settings
# pip install win10toast

# todolist_dir = os.path.join(os.path.dirname(sys.path[0]),'todolists')
todolist_dir = os.path.join(os.path.dirname(sys.path[0]),'AI-Assistant\\todolists')
# icon_dir = os.path.join(os.path.dirname(sys.path[0]),'ui\\images\\notification.ico')
icon_dir = os.path.join(os.path.dirname(sys.path[0]),'AI-Assistant\\ui\\images\\notification.ico')
os.makedirs(todolist_dir, exist_ok=True)

n = ToastNotifier()

def start_service(username):

    os.makedirs(f"{todolist_dir}", exist_ok=True)
    open(f"{todolist_dir}\\{username}.json", "a").close()

    while settings.stopNotifications == False:

        with open(f"{todolist_dir}\\{username}.json") as fileobj:
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
                n.show_toast(taskObj['task'], 'Due on: '+ taskObj['due_date'], duration=7, icon_path = icon_dir)
                print('notified')
                tasks.pop(0)
                with open(f"{todolist_dir}\\{username}.json",'w') as fileObj:
                    fileObj.write(json.dumps(tasks))
            else:
                # sleep
                time.sleep(1)

    print("Stoping notification service")

# start_service('Mihir')

# {"task": "watch movie", "due_date": "No Due Date", "dueSortKey": "99991231", "reminder": 2022042310521}