# km-to-miles
- These two little python programs can convert `kilometers to miles` and `miles to kilometers`

## Needed
- Python3
- or a online python compiler with the output

## How to?
- First download the `.py` files from releases and run them with python3 and enter the kilometers or miles.
- Or copy the codes and paste on a online compiler and run it.

### miles to kilometers
```python
# Taking kilometers input from the user
kilometers = float(input("Enter value in miles: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers / conv_fac
print('%0.2f miles is equal to %0.2f kilometers' %(kilometers,miles))
```
### Kilometers to miles
```python
# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
```
> #### Don't forget to give a star :star2: to my repo..
