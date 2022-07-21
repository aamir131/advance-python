f = open('writeline.txt',"a")
lst = ['Mumabi\n','Delhi\n','Manali\n','Lucknow\n','Indore\n','Kolkata\n','Chennai\n','Shimla\n',]
f.writelines(lst) # this method is used to create a group of list
f.close()
print("successfully") 