'''
Haydn Moyer
Polling
'''
 
 # polling.py


 favorite_languages = { "jen":["python ", "rust"],
    "sarah" : ["c"],
    "edward": ["rust"],
    "phil": ["python"] }


 people_to_poll = ["jen", "rust", "mike", "alex", "phil", "jaden"]

 for person in people_to_poll:
    if person in favorite_languages:
        print(f "Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f "{person.title()}, please take our favorite languages poll.")