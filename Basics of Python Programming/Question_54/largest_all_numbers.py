print("Enter list of number:")
num_list = []
while(True):
    user_input = input()
    if(user_input == 'q' or user_input=='Q'):
        break
    num_list.append(int(user_input))

for i in range(1,len(num_list)):
    max = num_list[0]
    if(max<num_list[i]):
        max = num_list[i]

print(f"Maximum number is {max}")

