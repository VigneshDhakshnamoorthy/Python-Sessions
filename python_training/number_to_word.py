word_num = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 100:"Hundred", 1000:"Thousand"}



def count_num(number):
    count = 0
    num = number
    while num != 0:
        num //= 10
        count += 1
    return count

def count_2(number):
    if number>20:
        tw_num = (number//10)*10
        re_num = number%10
        if re_num >0 :
            return(word_num[tw_num]+" "+word_num[re_num])
        else:
            return(word_num[tw_num])
    elif number<20:
        return(word_num[number])

def count_3(number):
    th_num = (number//100)
    rh_num = number%(th_num*100)
    return(word_num[th_num]+" "+word_num[100]+" "+count_2(rh_num))

def count_4(number):
    tr_num = (number//1000)
    rr_num = number%(tr_num*1000)
    return(word_num[tr_num]+" "+word_num[1000]+" "+count_3(rr_num))

  
def find_word_num():
    number = int(input("Enter Number: "))
    count = count_num(number)
    if count <3:
        print(count_2(number))
    elif count==3:
        print(count_3(number))
    else:
        print(count_4(number))


    
find_word_num()
    


