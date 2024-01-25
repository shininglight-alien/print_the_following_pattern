# Print the following pattern

for i in range(1, 6):
    print(str(i) * i)
    
print("\n".join(str(i) * i for i in range(1, 6)))
