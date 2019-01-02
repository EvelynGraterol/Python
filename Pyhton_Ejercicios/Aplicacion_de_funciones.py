def caught_speeding(speed,is_birthday):
    if is_birthday == True:
        if speed<=65:
            print ('No ticket')
        if speed >66 and speed<=86:
            print('Small Ticket')
        if speed>86:
            print('Big Ticket')

    else:
        if speed <=60:
            print('No Ticket')
        if speed >61 and speed<=81:
            print('Small Ticket')
        if speed>81:
            print('Big Ticket')
        pass

caught_speeding(50,True)
