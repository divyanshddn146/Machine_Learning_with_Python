num_list = []
sum = 0
even_sum = 0
odd_sum = 0
count_even = 0
count_odd = 0

print("Enter list of number:")
while(True):
    user_input = int(input())
    num_list.append(user_input)
    if(user_input == -1):
        for i in range(0,len(num_list)-1):
            sum = sum + num_list[i]
            if(num_list[i]%2 == 0):
                count_even = count_even+ 1
                even_sum = even_sum + num_list[i]
            else:
                count_odd = count_odd + 1
                odd_sum = odd_sum + num_list[i]
        print(f"Count = {len(num_list)-1}")
        print(f"Sum = {sum}")
        print(f"Even Average = {even_sum/count_even}")
        print(f"Odd Average = {odd_sum / count_odd}")

