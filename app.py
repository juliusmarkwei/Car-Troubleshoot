import time

print('Hi there, welcome to the new online troubleshoot assistance.'); time.sleep(4)
print('Please you need to keep your answers short. #Format: Yes/No'); time.sleep(4)
print('Now let\'s begin...'); time.sleep(1)
print()
issue = input('Is the car silent when you turn the key?\n:> ').capitalize()
while True:
    if issue == 'Yes':
        batteryI = input('Are the battery terminals corroded?\n:> ').capitalize()
        if batteryI == 'Yes':
            print('Clean terminals and try starting again.'); break
        elif batteryI == 'No':
            print('Your battery cables may be damaged. '
                  'Replace cables and try again.'); break
    elif issue == 'No':
        secondI = input('Does the car make a clicking noise?\n:> ').capitalize()
        if secondI == 'Yes':
            print('Replace the battery.'); break
        elif secondI == 'No':
            secondII = input('Does the car crank up but fail to start?\n:> ').capitalize()
            if secondII == 'Yes':
                print('Check spark plug connections.'); break
            elif secondII == 'No':
                secondIII = input('Does the engine start and then die?\n:>').capitalize()
                if secondIII == 'Yes':
                    finalI = input('Does your car have fuel injection?\n:> ').capitalize()
                    if finalI == 'Yes':
                        print('Get it in for service.'); break
                    elif finalI == 'No':
                        print('Check to ensure the choke is opening and closing.'); break
                else:
                    print('Get it in for service.'); break
