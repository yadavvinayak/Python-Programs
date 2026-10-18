def compound_amount(principal, rate, years, compounds_per_year=1):
    if compounds_per_year <= 0:
        raise ValueError("compounds_per_year must be positive")
    return principal * (1 + rate / (100 * compounds_per_year)) ** (compounds_per_year * years)

if __name__ == "__main__":
    p = float(input("Principal: "))
    r = float(input("Annual rate (%): "))
    t = float(input("Years: "))
    n = int(input("Compounds per year: "))
    print("Compound interest:", compound_amount(p, r, t, n) - p)
