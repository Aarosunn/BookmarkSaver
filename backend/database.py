curr_id = 0


def next_id() -> int:
    global curr_id
    curr_id = curr_id + 1
    return curr_id


db = {}
