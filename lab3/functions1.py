#Exercise 1. A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams
n = int(input())
def ingredient(n):
    a = 28.3495231 * n
    return a
print(ingredient(n))

#Exercise 2. Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)

n = int(input())
def Fahrenheit(n):
    C = ((5/9) * (n - 32))
    return C;
print(Fahrenheit(n))
