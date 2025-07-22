def create_multiples(num , length):
    nums = []
    i = 1
    while len(nums)< length:
        nums.append(num*i)
        i+=1
    
    return nums