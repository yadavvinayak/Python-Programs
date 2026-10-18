def execute_python(source, namespace=None):
                                                                         
    namespace = {} if namespace is None else namespace
    exec(source, namespace)
    return namespace

if __name__ == "__main__":
    execute_python("result = 2 + 3")
    print("Example result:", execute_python("result = 2 + 3")["result"])
