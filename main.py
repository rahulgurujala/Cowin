"""
1. run it continiously 
2. data of coming 4 days including today
3. export data in json file
4. want data of bidar as well as mumbai
5. send email to me if slot available for feetype = free and age group = 18
"""
from datetime import date, datetime
from time import sleep
from Cowin.cowin import Cowin

cowin = Cowin()


def main(calender):

    calender = date(2021, 5, datetime.now().day + calender)

    print(calender)

    # bidar = cowin.avail_slots(272, calender)

    # for bid in bidar:
    #     if bid['Message'] == 'Slot/s Available':
    #         # here
    #         print('Bidar: ',bid)

    mumbai = cowin.avail_slots(392, calender)

    for mum in mumbai:
        if mum["Message"] == "Slot/s Available":
            # here
            print("Mumbai: ", mum)


# run = True

# while run:
#     for i in range(0, 4):
#         main(i)
#     sleep(600)
