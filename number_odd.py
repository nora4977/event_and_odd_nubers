#A four-digit integer is given. Find the number of odd digits in it.
number=3457
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=number
a=var_int%10
b=var_int//10%10
c=var_int//100%10
d=var_int//1000%10
#Print the number of odd digits in the variable "var_int".
number=((a+0)%2)+((b+0)%2)+((c+0)%2)+((d+0)%2)

print(number)