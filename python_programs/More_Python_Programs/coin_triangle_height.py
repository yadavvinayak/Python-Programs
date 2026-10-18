from math import isqrt

def max_coin_triangle_height(coins):
    if coins < 0:
        raise ValueError("coins must be non-negative")
    return (isqrt(8 * coins + 1) - 1) // 2

if __name__ == "__main__":
    print(max_coin_triangle_height(int(input("Coins: "))))
