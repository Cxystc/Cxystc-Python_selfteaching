
Birthdays_list = {
	'陈文波':'74_0107',
	'吴楚凤':'74_1017',
	'欧阳宇':'04_0626',
	'张忠豪':'04_0215',
	'李想':'04_0227',
	'陈逸朗':'04_0109',
	'潘枳安':'04_0906',
	'刘智昕':'04_0307',
	'刘敏婧':'04_0517',
	'何朗轩':'04_0830',
	'陈毓馨':'02_0225',
	'左嘉耀':'04_0320',
	'梁己正':'04_0512',
	'曾浩烨':'04_0826',
	'陈心怡':'04_0115',
	'陈俊熙':'05_1024',
	'黄恺晴':'03_1221',
	'冯雅禧':'04_0813',
	'陈博睿':'04_0324',
	'陈梓凯':'04_0217',
	'黎泽霖':'04_0331',
	'冯梓淇':'08_1225'
}
def Birthday_Search():
	Activation = True
	while Activation:
		person = input ('请输入目标的全名 \n(print "quit" or "q" to quit) :')
		if person == 'quit' :
			Activation = False
		elif person == 'q' :
			Activation = False
		elif person in Birthdays_list.keys() :
			print ("Ta的出生日期是：",Birthdays_list[person])
		else:
			print ('此人不在列表里QAQ')

# Birthday_Search()
class BirthdaySearch_method:
    
    def __init__ (self,class_ofper):
        self.class_ofper = class_ofper
        r = input ('if you want you append you list?yes or no \n:')
        if r == 'yes':
            self.Add()
        else :
            pass
    def Search (self):
        activation = True
        while activation :
            person = input ('请输入目标的全名 \n(print "quit" or "q" to quit) :')              
            
            if person == 'quit':
                activation = False
            elif person == 'q':
                activation = False           
            elif person in Birthdays_list.keys():
                print ("The birthday of",person,"is",str(Birthdays_list[person]))
            else:
                print ("Sorry ,the person isn't in your list.Plase check your spell or list content and try again")
                print ("input quit or q to stop the application\n")    	
    def Add (self):
        print ('Modify the list in the following format：陈梓凯/04_0217')

        added_person = input ("Please input the person's name you want to append in Chinese:\n")

        Birthday = input ("Please input his or her Birthday in the format of :xx_xxxx")
        Birthdays_list[added_person] = Birthday

list_1 = BirthdaySearch_method("classmate")
list_1.Search()
print (Birthdays_list)
