def factorial(num):
    assert num >= 0 and int(num) == num , "The number must be a positive whole number"

    if num == 1 or num == 0 :
        return 1
    else:
        return num * factorial(num-1)
    

results = factorial(5)
print(results)