json = eval(input())

def json_sum(json):
    if type(json) == int:
        return json
    elif type(json) == str:
        return 0
    elif type(json) == list:
        return sum(map(json_sum, json))
    else: # dict
        return sum(map(json_sum, json.values()))

def json_sum2(json):
    if type(json) == int:
        return json
    elif type(json) == str:
        return 0
    elif type(json) == list:
        return sum(map(json_sum2, json))
    else: # dict
        if 'red' in json.values():
            return 0
        return sum(map(json_sum2, json.values()))

print("Part 1:", json_sum(json))
print("Part 2:", json_sum2(json))