## Day 1: Trebuchet?! ##

with open('input.txt', 'r') as f:
    number_sum = 0

    for line in f:
        line = line.strip()
        s_number = ""
        
        for c in line:
            if c.isdigit():
                s_number += c
                break
        
        for c in line[::-1]:
            if c.isdigit():
                s_number += c
                break
        
        number_sum += int(s_number)
    print(number_sum)