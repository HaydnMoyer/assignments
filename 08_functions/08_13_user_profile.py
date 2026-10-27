'''
Haydn Moyer
user profile

'''


def build_profile(first, last, **user_info):
    profile = {}
    profile['Haydn'] = first
    profile['Moyer'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile