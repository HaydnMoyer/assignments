'''
Haydn Moyer
sandwiches

'''


def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich("tuna", "sweet pickle", "mustard")
make_sandwich("ham", "cheese")
make_sandwich("ham", "mustard", "maynonnaise", "pickles")