#A four-digit integer is given. Find the sum of odd digits in it.
number=2573
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=number
a=var_int%10
b=var_int//10%10
c=var_int//100%10
d=var_int//1000%10

#Create a variable "sum_even" and assign it 0.
sum_even=0
#Find the sum of the odd digits in the variable "var_int".
sum_odd=((a+0)%2*a)+((b+0)%2*b)+((c+0)%2*c)+((d+0)%2*d)

print(sum_odd)