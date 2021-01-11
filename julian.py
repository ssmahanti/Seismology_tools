#This program calculates julian day for a date

month=[31,28,31,30,31,30,31,31,30,31,30,31] #month-day list

a=int(input("enter the year:"))
b=int(input("enter the month:"))
c=int(input("enter the day:"))

j=c	#julian day
i=0

#check whether a leap year or not
if a%400==0:
	month[1]=29
elif a%100==0:
	pass
elif a%4==0:
	month[1]=29
else:
	pass
#calculates julian day
while i<b-1:
	j=j+month[i]
	i=i+1
print j
