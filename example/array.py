N_MAX = 15
arr = list()
n = int(input("Enter number of elements (max 15): "))
if n > N_MAX:
    n = N_MAX
    print("n is limited to 15")

print("Enter elements:")
i = 0
while (i < n):
    tmp = int(input(""))
    arr.append(tmp)
    i += 1

print("Array:")
i = 0
while (i < n):
    print(arr[i], end = " ")
    i += 1
print("")