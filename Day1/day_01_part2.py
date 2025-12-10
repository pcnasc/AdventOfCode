current_position = 50
zero_count = 0

with open('list.txt', 'r') as file:
    for line in file:
        line = line.strip().upper()
        if not line:
            continue
            
        command = line[0]
        total_steps = int(line[1:]) 
        
        # Each 100 steps, dial goes to zero one time
        full_laps = total_steps // 100
        zero_count += full_laps
        
        # Remainder of the division
        remainder = total_steps % 100
        
        for _ in range(remainder):
            if command == "R":
                current_position = (current_position + 1) % 100
            elif command == "L":
                current_position = (current_position - 1) % 100
            
            # If in this "remainder" of movement it hits zero, count +1
            if current_position == 0:
                zero_count += 1

print(f"Total passcodes found (Part 2 - Hybrid Fix): {zero_count}")