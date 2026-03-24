def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


def get_name_with_age(name: str, age: int):
    name_with_age = name.title() + f" is {age} years old"
    return name_with_age


if __name__ == "__main__":
    print(get_full_name("aaron", "sun"))
    print(get_name_with_age(get_full_name("lian", "chang"), 18))
