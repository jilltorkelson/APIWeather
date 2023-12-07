from datetime import datetime


def format_date(today):
    weekday = today.strftime("%A")
    month_name = today.strftime("%B")
    day_num = today.strftime("%d")
    year = today.strftime("%Y")
    hour = today.strftime("%H")
    minute = today.strftime("%M")
    daytime = today.strftime("%p")

    formatted_date = (weekday + ", " + month_name + " " + day_num + ", " + year + " " + hour  + ":" + minute + daytime)
    return formatted_date
