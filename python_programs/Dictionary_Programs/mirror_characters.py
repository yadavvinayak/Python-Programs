def mirror_characters(text, start="a", end="z"):
    alphabet = {chr(code): chr(ord(start) + ord(end) - code)
                for code in range(ord(start), ord(end) + 1)}
    return "".join(alphabet.get(char, char) for char in text)

if __name__ == "__main__":
    print(mirror_characters("abcxyz"))
