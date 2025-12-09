current_position = 50
zero_count = 0

with open('list.txt', 'r') as file:
    for line in file:
        line = line.strip().upper()
        if not line:
            continue
        command = line[0]
        x = int(line[1:])
        #dial to the right
        if command == "R":
            current_position = (current_position + x) % 100
        #dial to the left
        elif command == "L":
            current_position = (current_position - x) % 100
        else:
            print("Invalid command")
            continue

        if current_position == 0:
            zero_count += 1
        print(f"current position is {current_position}")

print(f"Amount of times the dial pointed to zero: {zero_count}")