number = int(input("Enter Number: "))



word_num = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 100:"Hundred", 1000:"Thousand"}

count = 0
num = number
while num != 0:
    num //= 10
    count += 1


if count==2 and number>20:
    tw_num = (number//10)*10
    re_num = number%10
    if re_num >0 :
        print(word_num[tw_num]+" "+word_num[re_num])
    else:
        print(word_num[tw_num])
elif number<20:
    print(word_num[number])


if count==3:
    th_num = (number//100)
    rh_num = number%(th_num*100)
    if rh_num>20:
        tw_num = (rh_num//10)*10
        re_num = rh_num%10
        if re_num>0:
            print(word_num[th_num]+" "+word_num[100]+" "+word_num[tw_num]+" "+word_num[re_num])
        else:
            print(word_num[th_num]+" "+word_num[100]+" "+word_num[tw_num])

    elif rh_num<20:
        print(word_num[th_num]+" "+word_num[100]+" "+word_num[rh_num])

if count>3:
    tr_num = (number//1000)
    rr_num = number%(th_num*1000)
    
    


