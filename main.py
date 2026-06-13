from collections import Counter
import math
import os


def calculate_entropy(password: str) -> dict:

    current_length = len(password)
    if current_length == 0:
        return {"length": 0, "unique_chars": 0.0, "per_char_entropy": 0.0, "total_entropy": 0.0}
    
    
    char_map = dict(Counter(password))
    unique_chars = len(char_map)

    prob_map = {char: count / current_length for char, count in char_map.items()}
    log_map = {char: math.log(prob, 2) for char, prob in prob_map.items()}

    product_map = {char: prob_map[char] * log_map[char] for char in prob_map.keys()}

    per_char_entropy = -sum(product_map.values())
    total_entropy = per_char_entropy * current_length
    
    return {"length": current_length, "unique_chars": unique_chars, 
        "per_char_entropy": per_char_entropy,
        "total_entropy": total_entropy}

def run_cli():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        user_input = input("Enter your password (Type 'E' to exit): ")
        if user_input.lower() == "e":
            break 
        
        result = calculate_entropy(user_input)



