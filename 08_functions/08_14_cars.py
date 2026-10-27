'''
Haydn Moyer
Cars
'''


def make_car(manufacturer, model, **kwargs):
    car = {make_car: manufacturer, model: model}
    car['subaru'] = manufacturer
    car['outback'] = model
    for key, value in kwargs.items():
        car[key] = value
    return car