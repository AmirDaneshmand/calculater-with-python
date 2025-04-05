card_num = "5610591081018250"
number = list(card_num)
odd_sum = 0
double_even_num = []
even_sum = 0

for (ind, val) in enumerate(number):
    if(ind % 2 == 1):
        odd_sum += int(val)
    else:
        double_even_num.append(int(val) * 2)

double_string = ""
for x in double_even_num:
    double_string += str(x)
    
double_list = list(double_string)
for x in double_list:
    even_sum += int(x)

total_sum = even_sum + odd_sum

if(total_sum % 10 == 0):
    print("True")
else:
    print("False")