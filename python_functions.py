1.

def sum_to(n):
    return sum(range(1, n +1))


print(sum_to(3))



2.

def largest(nums):
    return max(nums)

print(largest((1, 2, 3, 4, 12, 65, 4)))

3. 
def occurences(str1, str2):
    return str1.count(str2)





4. 
def product(*args):
    products = 1
    for arg in args:
        products *= arg
    return products

print(product(3, 4, 5))


# function product(m, m, m) {
#     return
# }