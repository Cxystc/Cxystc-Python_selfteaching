factor = (7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)
key = ("1","0","X","9","8","7","6","5","4","3","2")
list = input("please input your ID number :\n")
def check(list):
    num = 0 
    if (len(list) != 18 ) :
        print("Invalid,please try again")
        return 
    for i in range(0,17):
        num += factor[i] * int(list[i])
    left = (num % 11) 
    if int(list[17]) != int(key[left]):
        print("Invalid,please try again")
        return
    if int(list[17]) % 2 == 0:
        print('0') 
    else :
        print('1')

check(list)