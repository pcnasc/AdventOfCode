import os

def is_valid_id(number):
    s = str(number)
    length = len(s)
    
    # NÃO descartamos ímpares logo de cara, pois 123123123 (tam 9) é inválido.
    
    # Vamos testar tamanhos de padrão de 1 até a metade da string
    # (Ex: numa string de 10, testamos padrões de tamanho 1, 2, 3, 4, 5)
    limit = length // 2
    
    for size in range(1, limit + 1):
        
        # 1. O tamanho do padrão tem que ser divisor do tamanho total
        if length % size == 0:
            
            # 2. Pega o "tijolinho" (padrão)
            pattern = s[:size]
            
            # 3. Calcula quantas vezes ele precisaria repetir
            repeats = length // size
            
            # 4. Reconstrói e compara (A mágica do Python)
            if pattern * repeats == s:
                return True # ACHAMOS! É formado por repetição, logo é "Inválido" (Soma)

    return False # Se testou todos os tamanhos e nada casou, é um ID normal (Não soma)
    
def solve():
    total_sum = 0
    
    # Certifique-se que o input.txt está na mesma pasta
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

if __name__ == "__main__":
    result = solve()
    print(f"The invalid IDs sum is: {result}")