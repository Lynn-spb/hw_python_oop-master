n = float(input())

first_dig = n // 1000
second_dig = ((n % 1000) // 100)
third_dig = n % 100
fourth_dig = n % 10

print(first_dig + second_dig + third_dig + fourth_dig)
print(len(n))
print(first_dig * second_dig * third_dig + fourth_dig)
print((first_dig + second_dig + third_dig + fourth_dig) // 4)
print(first_dig)
print(first_dig + fourth_dig)