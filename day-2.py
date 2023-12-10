## Day 2: Cube Conundrum ##

with open("input.txt", "r") as f:
    possible_counter = 0

    for id, line in enumerate(f, start=1):
        line = line[line.index(':')+1::]
        r_MAX = 12
        g_MAX = 13
        b_MAX = 14

        possible = True
        
        # Split the game by rounds
        rounds = line.strip().split(';')
        for round in rounds:
            # Split the round by hands
            for hand in round.split(','):
                count, color = hand.split()
                if color == "red" and r_MAX < int(count):
                    possible = False
                    break
                elif color == "green" and g_MAX < int(count):
                    possible = False
                    break
                elif color == "blue" and b_MAX < int(count):
                    possible = False
                    break
            if not possible:
                break
            
        if possible:
            possible_counter += id
    print(possible_counter)

        
        
    
        
