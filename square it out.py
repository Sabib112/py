def filter_square_values(start: int, end: int):
    squares = {num: num ** 2 for num in range(start, end + 1)}
    
    even_squares = {num: sq for num, sq in squares.items() if sq % 2 == 0}
    odd_squares = {num: sq for num, sq in squares.items() if sq % 2 != 0}
    
    print("Even Square Values:")
    for num, sq in even_squares.items():
        print(f"{num}^2 = {sq}")
    
    print("\nOdd Square Values:")
    for num, sq in odd_squares.items():
        print(f"{num}^2 = {sq}")

filter_square_values(1, 10)