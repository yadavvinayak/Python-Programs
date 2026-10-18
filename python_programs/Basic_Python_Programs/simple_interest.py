def simple_interest(principal, rate, years):
    return principal * rate * years / 100

if __name__ == "__main__":
    p = float(input("Principal: "))
    r = float(input("Annual rate (%): "))
    t = float(input("Years: "))
    print("Simple interest:", simple_interest(p, r, t))
