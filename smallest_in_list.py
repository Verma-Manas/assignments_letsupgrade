ele=int(input("Enter number of elements you want in the list: "))
list1=[]
for a in range(0,ele):
    ele=int(input("Enter element: "))
    list1.append(ele)
print("List is: ",list1)
smallest=min(list1)
print("The smallest element in the list is: ", smallest)
