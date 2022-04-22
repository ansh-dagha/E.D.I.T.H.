import datetime
import re

MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october", "november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]

def get_date(text):
    text = text.lower()

    y = re.search('\d{4}',text)
    if y:
        y = y.group(0)
    else:
        y = ''
    text = re.sub(y, '', text)

    today = datetime.date.today()

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

        return today + datetime.timedelta(dif)

    try:
        month_in_words = MONTHS[month-1]
    except:
        month_in_words = month

    if day != -1:  # FIXED FROM VIDEO
        return day, month, month_in_words, int(y) or year


def get_time(text):
    # returns hours, minutes, 'AM' or 'PM'
    try:
        text = text.lower()
        text = text.replace(':',' ').replace('p.m.','PM').replace('a.m.','AM').replace('am','AM').replace('pm','PM')

        text = text.split()
        return int(text[0]), int(text[1]), text[2]
    except:
        return 12, 0, 'PM'