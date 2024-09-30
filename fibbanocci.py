def fibbanocci(num):
    assert num >= 0 and int(num) == num , "Number must be a positive whole number"

    if num==0 or num==1 :
        return num
    else:
        return fibbanocci(num-1) + fibbanocci(num-2)
    

results = fibbanocci(3)     

print(results)