def time_3(credit):
    time = 9
    if credit < 13.5 and credit > 4.0:
        time =  str(int(time+((13.5- credit) * 30)//60)) +':' +  str(int((13.5- credit) * 30) % 60)
    else:
        time = 'not right time'
    return time


def time_2(credit):
    time = 9
    if credit < 8.5 and credit > 4.0:
        time =  str(int(time+((8.5- credit) * 30)//60)) +':' +  str(int((8.5- credit) * 30) % 60)
    else:
        time = 'not right time'
    return time  
