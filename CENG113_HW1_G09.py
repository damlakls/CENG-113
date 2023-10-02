#Group ID:09
#Nurcan Yıldız-280201082
#Damla Keleş-280201057

Month = input("Please write the month: ")
if Month == "January" or Month == "February" or Month == "December" :
    print(Month, "is in Winter." )
elif Month == "March" or Month == "April" or Month == "May" :
    print(Month, "is in Spring.")
elif Month == "June" or Month == "July" or Month == "August" :
    print(Month, "is in summer.")
elif Month == "September" or Month=="October" or Month == "November" :
    print(Month, "is in Autumn.")
else:                                                                      #if the user enters something other than months, thanks to 'else' 
    print("Please enter a valid year or use capital letters.")