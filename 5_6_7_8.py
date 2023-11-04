num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count = 0

for idx, i in enumerate(num_list):
    count+=1
    if i == 36:
        print("Number found at position:", idx)
        break
        
print(count)

"""
Output:
Number found at position: 8
9
"""
