def get_prefix_hashes(string: str, base: int, mod: int) -> list[int]:
    hashes = [0] * (len(string) + 1)
    for i, char in enumerate(string):
        hashes[i + 1] = (hashes[i] * base + ord(char)) % mod

    return hashes


def get_substring_hash(ix_l: int, ix_r: int, hashes: list[int], base_powers: list[int], mod: int) -> int:
    hash_r = hashes[ix_r]
    hash_l = hashes[ix_l - 1]
    power = base_powers[ix_r - ix_l + 1]
    return (hash_r - hash_l * power) % mod


def get_base_powers(length: int, base: int, mod: int) -> list[int]:
    base_powers = [1] * length
    for i in range(1, length):
        base_powers[i] = (base_powers[i - 1] * base) % mod

    return base_powers


def main():
    base = int(input())
    mod = int(input())
    string = input()

    prefix_hashes = get_prefix_hashes(string, base, mod)
    base_powers = get_base_powers(len(string) + 1, base, mod)

    n = int(input())
    results: list[str] = []
    for _ in range(n):
        ix_l, ix_r = map(int, input().split())
        res = get_substring_hash(ix_l, ix_r, prefix_hashes, base_powers, mod)
        results.append(str(res))

    print('\n'.join(results))


if __name__ == '__main__':
    main()
