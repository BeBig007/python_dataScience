def all_thing_is_obj(object: any) -> int:
    print(object)
    match object:
        case ["Hello", "tata!"]:
            print("List : <class 'list'>")
        case ("Hello", "toto!"):
            print("Tuple : <class 'tuple'>")
        case {"Hello", "tutu!"} or {"tutu!", "Hello"}:
            print("Set : <class 'set'>")
        case {"Hello" : "titi!"}:
            print("Dict : <class 'dict'>")
        case str:
            print(f"{object} is in the kitchen : <class 'str'>")
        case _:
            print("Type not found")
    return 42
