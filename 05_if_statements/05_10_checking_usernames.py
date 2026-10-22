'''
Haydn Moyer
Checking Usernames

'''



usernames = ["admin", "Dreadedheadplays", "HaydnMoney", "The_DOg", "Jane_Doe", "Burger Nugget"]

new_users = ["Mario", "Loui-G", "Bowser", "Bowser Jr", "Dark Vader"]

current_users_lower = [user.lower() for user in usernames]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} will need to enter a new username.")
    else:
        print(f"{new_user} is available.")