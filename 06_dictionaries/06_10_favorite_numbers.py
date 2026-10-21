'''
Haydn Moyer
Favorite Numbers

'''

favorite_numbers = {
    "Rondo Parker": [37, 21, 56],
    "Haydn Moyer": [12, 95, 43],
    "Lonnie Walker": [25, 72, 65],
    "Clint Barton": [42, 89, 29],
    "Tony Stark": [58, 45, 59] 
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(number)