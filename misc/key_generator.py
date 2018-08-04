import string
import random
import json


def generate_config_from_list(object_name, display_name, file_name, key_list, max_list, duration_list):
    keys = [
        {
            'key': k,
            'count': 0,
            'max': m,
            'duration': d
        }
        for k, m, d in zip(key_list, max_list, duration_list)
    ]

    config_dict = {
        'object_name': object_name,
        'display_name': display_name,
        'file_name': file_name,
        'keys': keys
    }

    return config_dict


def generate_random_strings(length, number, restriction=string.ascii_uppercase+string.digits, seed=0):
    random.seed(seed)
    r_str_list = [''.join([random.choice(restriction) for j in range(length)]) for i in range(number)]
    return r_str_list


def generate_json(filename, list_of_dict):
    with open(filename, 'w') as f:
        json.dump(list_of_dict, f, indent=2)


if __name__ == '__main__':
    KEY_LENGTH = 8
    NUMBER_OF_KEYS = 3
    RANDOM_SEED = 201808041330

    rsl1 = generate_random_strings(KEY_LENGTH, NUMBER_OF_KEYS, seed=RANDOM_SEED)
    rsl2 = generate_random_strings(KEY_LENGTH, NUMBER_OF_KEYS, seed=RANDOM_SEED+1)
    ml = [-1 for i in range(NUMBER_OF_KEYS)]
    dl = [209912312359 for i in range(NUMBER_OF_KEYS)]

    config1 = generate_config_from_list('sample01', 'SAMPLE-01', 'sample01.txt', rsl1, ml, dl)
    config2 = generate_config_from_list('sample02', 'SAMPLE-02', 'sample02.txt', rsl2, ml, dl)
    config_list = [config1, config2]

    generate_json('test.json', config_list)
