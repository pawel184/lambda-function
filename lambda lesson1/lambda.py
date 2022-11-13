### Lamda 1
sum_arg = lambda a, b: a + b

sum = sum_arg(1, 2)

print('result_1 = ',sum)

### Lamda 2
x = input().split()
xs = (int(i) for i in x)



evens = list(filter(lambda x: x % 2 == 0,xs))
print(evens)
