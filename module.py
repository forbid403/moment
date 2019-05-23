import datetime

def cutDate(date_string):
    temp00 = date_string.replace("(", "")
    temp0 = temp00.replace(")", "")
    temp1 = temp0.split('/')
    month = int(temp1[0])

    temp2 = temp1[1]
    temp3 = temp2.split(" ")
    day = int(temp3[0])

    temp4 = temp3[1]
    temp5 = temp4.split(":")
    hour = int(temp5[0])
    minute = int(temp5[1])

    return datetime.datetime(2019, month, day, hour, minute)

