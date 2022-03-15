from app.exc.invalids_requests import InvalidKeys, InvalidValues


key_names = ["name", "last_name", "email", "password" ]

def check_keys(data: dict):
    data_keys = data.keys()
    missing_keys = [key for key in key_names if key not in data_keys]

    if missing_keys:
        raise InvalidKeys(missing_keys, key_names)

def check_values_types(data: dict):
    for key in key_names:
        if type(data[key]) != str:
            raise InvalidValues(data={f'{key}: {data[key]}'}, type=type(data[key]))