def snake_to_pascal(text):
    return "".join(part.capitalize() for part in text.split("_"))

if __name__ == "__main__":
    print(snake_to_pascal("hello_python_world"))
