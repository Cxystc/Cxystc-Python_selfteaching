import random
#tag 方法循环：
tag = True
score = 0
variate = random.randint(0,10)
print('Game start ,now there is a new number range from 1 to 10,you are supposed to guess the number and try to find it due to the tips!\n')
while tag:
    print(variate)
    guess_number = int(input ('now input you number: '))
    #判断
    if guess_number > variate:
        print('\nTry to guess a small one!\n')
        continue

    elif guess_number < variate:
        print('\n5Try to guess a bigger one!\n')
        continue
    else:
        print('Well done!\n')
        variate = random.randint(0,10)
        score += 1
        print('Congratulations!  You have got %d points!\n'%score)
        if score > 1 :
            chioce = input('You have successfully guess for several time ,input "q" to quit or input "c" to continue:\n')
            if chioce == 'q':
                print('Thanks for playing!\n')
                tag = False
            elif chioce == 'c' :
                continue
            else : 
                print ('?????We don\'t understand ,we will start a new game for you!\n')
                continue





