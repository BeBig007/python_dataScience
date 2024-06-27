from S1E7 import Baratheon, Lannister

    # Ned = Stark("Ned")
    # print(Ned.__dict__)
    # print(Ned.is_alive)
    # Ned.die()
    # print(Ned.is_alive)
    # print(Ned.__doc__)
    # print(Ned.__init__.__doc__)
    # print(Ned.die.__doc__)
    # print("---")
    # Lyanna = Stark("Lyanna", False)
    # print(Lyanna.__dict__)
    # try:
    #     hodor = Character("hodor")
    # except TypeError as e:
    #     print(e)

def main():
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")

    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")

    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")


if __name__ == "__main__":
    main()

# $> python tester.py
# {'first_name': 'Robert', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hairs': 'dark'}
# <bound method Baratheon.__str__ of Vector: ('Baratheon', 'brown', 'dark')>
# <bound method Baratheon.__repr__ of Vector: ('Baratheon', 'brown', 'dark')>
# True
# False
# Representing the Baratheon family.
# ---
# {'first_name': 'Cersei', 'is_alive': True, 'family_name': 'Lannister', 'eyes': 'blue', 'hairs': 'light'}
# <bound method Lannister.__str__ of Vector: ('Lannister', 'blue', 'light')>
# True
# ---
# Name : ('Jaine', 'Lannister'), Alive : True
# $>