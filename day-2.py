## Day 2: Cube Conundrum ##

with open("input.txt", "r") as f:
    game_counter = 0

    for id, line in enumerate(f, start=1):
        line = line[line.index(':')+1::]
        r_MAX = 1
        g_MAX = 1
        b_MAX = 1

        # Split the game by rounds
        rounds = line.strip().split(';')
        for round in rounds:
            # Split the round by hands
            for hand in round.split(','):
                count, color = hand.split()
                if color == "red" and r_MAX < int(count):
                    r_MAX = int(count)
                elif color == "green" and g_MAX < int(count):
                    g_MAX = int(count)
                elif color == "blue" and b_MAX < int(count):
                    b_MAX = int(count)
    
        game_counter += r_MAX * g_MAX * b_MAX
    print(game_counter)
        
                    
        
        
    
        
