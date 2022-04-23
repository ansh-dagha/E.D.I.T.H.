import os, sys, json, re
from datetime import datetime as dt
from utilities.get_date_time import *
from utilities.speech_functions import * 


users_dir = os.path.join(os.path.dirname(sys.path[0]),'todolists')
os.makedirs(users_dir, exist_ok=True)


def preprocess(task, due_date, reminder_date, time):
    try:
        if (task == "" or task == None):
            task = "Do Nothing"
        
        try:
            day, month, month_in_words, year = get_date(due_date)
            due_date = f"{int(day)} {month_in_words}"
            dueSortKey = year+month+day
        except Exception as e:
            print(e)
            due_date = "No Due Date"
            dueSortKey = "99991231"

        try:
            day, month, month_in_words, year = get_date(reminder_date)
        except Exception as e:
            print(e)
            today = dt.today()
            day, month, month_in_words, year = (str(today.day).zfill(2), str(today.month).zfill(2), today.strftime("%B"), str(today.year))

        hours, minutes, f_in_words, f = get_time(time)
        reminder = int(year+month+day+f+hours+minutes)
        return task, due_date, dueSortKey, reminder
    
    except Exception as e:
        print(e)
        pass
    

def add_to_list(username, task, due_date, reminder_date, time):
    try:
        task, due_date, dueSortKey, reminder = preprocess(task, due_date, reminder_date, time)

        tasks = []
        open(f"{users_dir}\\{username}\\{username}.json", 'a').close()

        with open(f"{users_dir}\\{username}\\{username}.json") as fileobj:
            try:
                tasks = json.load(fileobj)
            except Exception as e:
                tasks = []
                pass

            task_obj = {
                'task':task,
                'due_date': due_date,
                'dueSortKey': dueSortKey,
                'reminder': reminder,
            }
            tasks.append(task_obj)

            tasks.sort(key = lambda d: d['reminder'])

        with open(f"{users_dir}\\{username}\\{username}.json",'w') as fileobj:
            fileobj.write(json.dumps(tasks))

        speak('Task added to your list')

    except Exception as e:
        print(e)



def remove_from_list(username, task_no):
    try:
        tasks = []

        with open(f"{users_dir}\\{username}\\{username}.json") as fileobj:
            try:
                tasks = json.load(fileobj)
            except Exception as e:
                print(e)
                speak('No pending tasks')
                return
        
        if task_no > len(tasks) or task_no < 1:
            speak("Invalid Task Number")
            return
        
        tasks.pop(task_no-1)
        
        with open(f"{users_dir}\\{username}\\{username}.json",'w') as fileobj:
            fileobj.write(json.dumps(tasks))
        
        speak('Task removed from your list')

    except Exception as e:
        print(e)


def to_do_list_open(username):
    output = "No pending tasks"

    try:
        with open(f"{users_dir}\\{username}\\{username}.json") as fileobj:
            tasks = json.load(fileobj)
            if len(tasks) == 0:
                print(output)
                return output
            output = ""
            tasks.sort(key = lambda task: task['dueSortKey'])
            for taskObj in tasks:
                if taskObj['due_date'] != 'No Due Date':
                    output += f"Task : "+ taskObj['task'] + " due on " + taskObj['due_date'] + "\n"
                else:
                    output += f"Task : "+ taskObj['task'] + " is not due" + "\n"
    
        with open(f"{users_dir}\\tasks.txt",'w') as fileobj:
            fileobj.write(output)

        os.startfile(f"{users_dir}\\tasks.txt")
        speak(output)

    except Exception as e:
        speak('Unable to access to do list')
        print(e)


def to_do_list_add_task(username):
    try:
        speak('What task do you want me to add')
        task = listen()
        speak('When is the task due?')
        due_date = listen()
        speak('On which date should i remind you')
        reminder_date = listen()
        speak('On What time should i remind you')
        reminder_time = listen()

        add_to_list(username, task, due_date, reminder_date, reminder_time)
    except Exception as e:
        speak('Sorry unable to add task')
    

def to_do_list_remove_task(username):
    try:
        speak('Which task do you want me to remove')
        text = listen()
        num = re.search('\d+', text)
        if num:
            remove_from_list(username, int(num.group(0)))
            
    except Exception as e:
        print(e)
        speak('Sorry unable to remove task')

# add_to_list('Mihir', 'drink water', '27th april 2022', 'monday', '8 a.m.')
# add_to_list('Mihir', 'complete mini project', '2nd may 2022', '23rd april', ' 11 1 p.m.')
add_to_list('Mihir', 'watch movie', 'No due date', 'dont remind', 'dont remind')

# to_do_list_remove_task('Mihir')

# to_do_list_open('Mihir')