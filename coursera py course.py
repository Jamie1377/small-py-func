a = {'name': 'RiRi', 'location': 'Van','age': 27 }

sen = '{} is a {} year old slut who wants to give me a bj at {}'


print(a['name'] + ' is a ' + str(a['age']) + ' year old slut who wants to give me a bj at ' + a['location'] + '.') 

# print(number for number in range(0,1000))



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

# importing the required module
import matplotlib.pyplot as plt
  
plt.show()
