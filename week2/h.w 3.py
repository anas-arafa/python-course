# x=input("the number of chickens")
# z=input("the number of cows")
# y=input("the number of pigs")
# total=(int(x)*2)+(int(z)*4)+(int(y)*4)
# print(total)


x=int(input("Enter the chickens count"))
y=int(input("Enter the cows count"))
z=int(input("Enter the pigs count"))
legs={"ch":x*2,"c":y*4,"p":z*4}
print(legs["ch"] + legs["c"] + legs["p"])

