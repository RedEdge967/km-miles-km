# Taking kilometers input from the user
kilometers = float(input("Enter value in miles: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers / conv_fac
print('%0.2f miles is equal to %0.2f kilometers' %(kilometers,miles))
