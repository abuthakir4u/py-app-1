command = ''
is_car_started = False
while True:
    command = input('> ')
    if command.lower() == 'start':
        if is_car_started:
            print('Car already started')
        else:
            print ('car started')
            is_car_started = True
    elif command.lower() == 'stop':
        if not is_car_started:
            print('Car already stopped')
        else:
            print ('car stopped')
            is_car_started = False
    elif command.lower() == 'help':
        print('''
start - to start the card
stop - to stop the car
quit - to exit
        ''')
    elif command == 'quit':
        break
    else:
        print ('i don\'t understand your command')