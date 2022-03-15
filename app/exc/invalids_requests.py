class InvalidKeys(Exception):
    def __init__(self, missing_keys: list, keys_list: list) -> None:
        self.message = {
            "required_keys": keys_list,
            "missing_keys": missing_keys
        }

class InvalidValues(Exception):
    def __init__(self, data: dict, type: str) -> None:
        self.message = {
            "error": f'type of {data} is {type}',
            "msg": "the values must be passing in string"
        }