import os

def is_valid_id(number):
    s = str(number)
    length = len(s)
    
    if length % 2 != 0:
        return False
    
    mid = length // 2
    first_half = s[:mid]
    second_half = s[mid:]

    return first_half == second_half
    
def solve():
    total_sum = 0
    
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
        content = f.read().strip()

    ranges = content.split(",")

    for interval in ranges:
        start_str, end_str = interval.split("-")
        start = int(start_str)
        end = int(end_str)

        for num in range(start, end + 1):
            if is_valid_id(num):
                total_sum += num
                    
    
    return total_sum

result = solve()
print(f"The valid IDs sum is: {result}")