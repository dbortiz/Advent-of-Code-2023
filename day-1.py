## Day 1: Trebuchet?! ##

dict_number = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

# Loop through dict to find possible number
def search_dict(search):
    for number in dict_number.keys():
        if number in search:
            return dict_number[number]
    return 0

with open('input.txt', 'r') as f:
    number_sum = 0

    for line in f:
        line = line.strip()
        s_number = ""

        # Find first digit in number
        number = []
        for c in line:
            if c.isdigit():
                s_number += c
                break
            
            if len(number) == 5:
                number.pop(0)
                number.append(c)
            elif len(number) < 5:
                number.append(c)
            
            number_to_search = "".join(number)
            res = search_dict(number_to_search)
            if res:
                s_number += res
                break
        
        # Find second digit in number
        number = []
        for c in line[::-1]:
            if c.isdigit():
                s_number += c
                break

            if len(number) == 5:
                number.pop()
                number.insert(0, c)
            else:
                number.insert(0, c)

            number_to_search = "".join(number)
            res = search_dict(number_to_search)
            if res:
                s_number += res
                break
         
        # Sum numbers
        number_sum += int(s_number)
    print(number_sum)