x=int(input("please write the number of calories"))
y=int(input("please write the number of days"))
z=float(input("please write the percentage"))
i=1
while(i<=y):
    x=x-x*(z/100)
    if (x<1200):
        print("Calories cannot be less than 1200")
        break
    print(f"Day{i}", x)
    i=i+1
    

