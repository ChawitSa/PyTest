from BMI import *
m = float(input("Mass[kg]: "))
h = float(input("Height[cm]: "))
bmi = cal(m,h)
if m>=5 and m<=110 and h<=195 and h>=75:
    print("BMI: "+"{:.2f}".format(bmi)+"\t level[1-5]: "+over(m,h))
else:
    print("Alert! "+over(m,h))