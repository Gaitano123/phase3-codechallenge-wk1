def constant_value(string):
    vowels = "aeiou"
    constant_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
                        'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
                        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
                        'w': 23, 'x': 24, 'y': 25, 'z': 26}
    
    current_value = 0
    max_value = 0
    
    for char in string:
        if char in vowels:
            current_value = 0
        
        else:
            current_value += constant_values[char]
            max_value = max(max_value, current_value)
            
    return max_value
