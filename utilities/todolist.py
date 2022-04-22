import os, sys, json, re
from datetime import datetime
from utilities.get_date_time import *
from utilities.speech_functions import * 


users_dir = os.path.join(os.path.dirname(sys.path[0]),'users')
os.makedirs(users_dir, exist_ok=True)


def preprocess(task, reminder_date, time):
    try:
        if (task == "" or task == None):
            task = "Do Nothing"
        try:
            day, month, month_in_words, year = get_date(reminder_date)
        except Exception as e:
            print(e)
            reminder_date = (datetime.now().day,
                        datetime.now().month,
                        datetime.now().year)
        hours, minutes, f = get_time(time)

        reminder_date = f"{day} {month_in_words} {year}"
        time = f"{hours} {minutes} {f}"
        dtKey = str(year)+str(month).zfill(2)+str(day).zfill(2)+f+str(hours).zfill(2)+str(minutes).zfill(2)

        return task, reminder_date, time, dtKey
    
    except Exception as e:
        print(e)
        pass
    


def add_to_list(username, task, reminder_date, time):
    try:
        task, reminder_date, time, dtKey = preprocess(task, reminder_date, time)

        tasks = []
        open(f"{users_dir}\\{username}.json", 'a').close()

        with open(f"{users_dir}\\{username}.json") as fileobj:
            try:
                tasks = json.load(fileobj)
            except Exception as e:
                tasks = []
                pass

            task_obj = {
                'task':task,
                'reminder_date': reminder_date,
                'time':time,
                'dtKey': dtKey,
            }
            tasks.append(task_obj)

            tasks.sort(key = lambda d: d['dtKey'])

        with open(f"{users_dir}\\{username}.json",'w') as fileobj:
            fileobj.write(json.dumps(tasks))

        speak('Task added to your list')

    except Exception as e:
        print(e)



def remove_from_list(username, task_no):
    try:
        tasks = []

        open(f"{users_dir}\\{username}.json", 'a').close()

        with open(f"{users_dir}\\{username}.json") as fileobj:
            try:
                tasks = json.load(fileobj)
            except Exception as e:
                print(e)
                tasks = []
                pass
        
        if task_no > len(tasks) or task_no < 1:
            speak("Invalid Task Number")
            return

        with open(f"{users_dir}\\{username}.json",'w') as fileobj:
            fileobj.write(json.dumps(tasks))
        
        speak('Task removed from your list')
    except Exception as e:
        print(e)


def open_list(username):

    pass



def to_do_list_add_task(username):
    try:
        speak('What task do you want me to add')
        task = listen()
        speak('On which date should i remind you')
        reminder_date = listen()
        speak('On What time should i remind you')
        reminder_time = listen()

        add_to_list(username, task, reminder_date, reminder_time)
    except Exception as e:
        speak('Sorry unable to add task')
    

def to_do_list_remove_task(username):
    try:
        speak('Which task do you want me to remove')
        text = listen()
        num = re.search('\d+', text)
        if num:
            remove_from_list(username, num.group(0))

    except Exception as e:
        print(e)
        speak('Sorry unable to remove task')

to_do_list_add('Mihir')