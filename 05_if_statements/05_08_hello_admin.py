'''
Haydn Moyer
Hello Admin

'''

usernames = ["admin", "Dreadedheadplays", "HaydnMoney", "The_DOg", "Jane_Doe", "Burger Nugget"]

for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")