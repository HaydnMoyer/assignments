'''
Haydn Moyer
Favorite numbers

'''
favorite_numbers = { 'Rondo': 7,
                    'Haydn': 3,
                    'Lonnie': 9,}

print(f'{favorite_numbers["Lonnie"]} is the favorite.')

for key, value in favorite_numbers.items():
    print (f'The key is {key} and the value is {value}.')
    