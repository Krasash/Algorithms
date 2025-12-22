
#Euclidean Algorithm
def euclidean_alg(a, b):
    while b != 0:
        a, b = b, a % b
    return a

first_value = input('Type in the first value: ')
second_value = input('Type in the second value: ')
print(euclidean_alg(int(first_value), int(second_value)))


