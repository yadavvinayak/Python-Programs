import ipaddress

def is_valid_ip(value):
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    print(is_valid_ip(input("IP address: ")))
