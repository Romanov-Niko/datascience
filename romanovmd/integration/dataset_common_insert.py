from romanovmd.validator.lib import *
from burdenkods.validator.lib import *
from romanovmd.integration.dataset_structure_common import dataset


def get_keys(prompt):
    key = input(prompt)
    while not keys_validator(key):
        key = input(prompt)
    return str(key)

def get_asins(prompt):
    asins = input(prompt)
    while not asins_validator(asins):
        asins = input(prompt)
    return str(asins)

def update_dataset():
    id = id_validator("Введіть id - ")
    keys = get_keys("Введіть keys - ")
    asins = get_asins("Введіть asins - ")
    name = name_validator("Введіть name - ")
    price_amountMin = price_amountMin_validator("Введіть price_amountMin - ")
    sizes = sizes_validator("Введіть sizes - ")
    dataset.update({id:{'keys':keys, 'asins': asins, 'name': name, 'price.amount_Min': price_amountMin, 'sizes': sizes}})
    print(dataset)

print(update_dataset())