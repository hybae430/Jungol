inputs = []
for i in range(3):
    inputs.append(input())
    if i == 2:
        print(inputs[i])
    else:
        print("%.2f" %float(inputs[i]))