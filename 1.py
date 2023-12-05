y = int(input("Please enter the number of years: "))
c = y*12
i=1
while(i<=c):
    Temperature=int(input("please enter the monthly temperature"))
    i=i+1
average_monthly_high_temperature = Temperature/c
average_yearly_high_temperature = Temperature/y
print("The average monthly high temperature is: ", average_monthly_high_temperature)
print("The average yearly high temperature is:", average_yearly_high_temperature)

    


    