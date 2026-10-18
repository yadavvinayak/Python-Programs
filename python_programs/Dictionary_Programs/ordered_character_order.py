from collections import OrderedDict

def characters_in_order(text, order):
    positions = {char: index for index, char in enumerate(order)}
    return "".join(sorted(text, key=lambda char: positions.get(char, len(positions))))

if __name__ == "__main__":
    print(characters_in_order("geeksforgeeks", "egr"))
