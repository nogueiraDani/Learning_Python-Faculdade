x = 10
y = 1
result = not x > y

print(result)

z = 5.5
new_result = (x > y) and (z == y)
print(new_result)

new_result = (x > y) or not (z == y) and y != y + z / x
print(new_result)
