import datetime
import re

MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october", "november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]

def get_date(text):
    text = text.lower()
    today = datetime.datetime.today()

    y = re.search('\d{4}',text)
    if y:
        text = re.sub(y.group(0), '', text)
        y = y.group(0)
    else:
        y = ''

    if text.count("today") > 0:
        return today

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

    # THE NEW PART STARTS HERE
    if month < today.month and month != -1:  # if the month mentioned is before the current month set the year to the next
        year = year+1

    # This is slighlty different from the video but the correct version
    if month == -1 and day != -1:  # if we didn't find a month, but we have a day
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month

    # if we only found a dta of the week
    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if text.count("next") >= 1:
                dif += 7
        res = today + datetime.timedelta(dif)
        return res.strftime('%d'), res.strftime('%m'), res.strftime('%B'), res.strftime('%Y')

    try:
        month_in_words = MONTHS[month-1]
    except:
        month_in_words = month

    if day != -1:  # FIXED FROM VIDEO
        return str(day).zfill(2), str(month).zfill(2), month_in_words, str(y) or str(year)

def get_time(text):
    # returns hours, minutes, 'AM' or 'PM'
    try:
        text = text.lower()
        text = text.replace(':',' ').replace('p.m.','PM').replace('a.m.','AM').replace('am','AM').replace('pm','PM')

        res = list(map(int ,re.findall("\d+", text)))
        if len(res) >= 2:
            hours = (res[0] + int(res[1]/60))%12
            minutes = res[1]%60
        else:
            hours = res[0]%12
            minutes = 0
            
        f = re.search('PM|AM', text)
        if f:
            f = f.group(0)
        else:
            f='AM'
        
        return str(hours).zfill(2), str(minutes).zfill(2), f, '0' if f=='AM' else '1'
    except Exception as e:
        return '11', '59', 'AM', '0'

# print(get_date('monday'))
# print(get_date('next monday'))
# print(get_date('15 june 2022'))
# print(get_date('31 february 2021'))

# print(get_time('4:45 p.m.'))
# print(get_time('4 p.m.'))
# print(get_time('4 02 p.m.'))
# print(get_time('4 02 '))