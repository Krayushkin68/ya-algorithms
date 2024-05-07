import random
from string import ascii_lowercase

from D import hash_str

alphabet = list(ascii_lowercase)


def get_random_string(length) -> str:
    return ''.join(random.choices(alphabet, k=length))


def run():
    hashes = {}
    strings = set()

    while True:
        try:
            string = get_random_string(random.randint(10, 1000))
            if string in strings:
                continue

            hash_value = hash_str(string, 1000, 123987123)
            if hash_value in hashes:
                print('Found!')
                print(string)
                print(hashes[hash_value])
                print(hash_value)
                break

            hashes[hash_value] = string
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    run()

"""
Found!
piwnqtpzakiliehbsklolsjguwkvygfdocesrgmvujwqhtagdikdzaxgnlmbjodfsqycatlezpbmncjehfohrmcpbzdagslrbblnxioxjgkifwjuswyfbbbzwfakafhriszitrkuzpmtkouxhvbhlofxvixwhdtyfqxutdfkgmbtybvbdnirlmwvugpfbatzramvxbdwftcptdttgkxsqcebrfrbehfrwzknjpdyxgcdqfsqjftmkvnljfyphrmnbawpnwxybvzuxdguawgrdxcuqjezigypnkznpidikgowbhyiotngkhmcgxaglttdlwnrgabpuknbaugvjhvzfknizgojslvhlxisvzvmyxeqjhcillgqjrgykicwyzaxbclmiegoegyalcsxetvcexitkrtpsicsfyvyrawrraiekagroxhguzpcypajwqosfprmmmourlewvzrrjmwsegtjuuyqqbwwwivnotxtrpkgwijsogflciyfos
axjbtmirxdxqklsseymvnhglpgnpspfqmfgoouqwedjiebtwwupoqtfpwouyhvkrctqqylmklqwckbasfzpoinryyaqrxerjxqejcbwitvjylsgrngvwxhpkkxfvsatgdekpfaupokzsxdnytuuohiavidspssjhcohmqtpkskdhwrdkoswrmuhugkmjsgbsxmkvqqewosbfvsotgaojafjnofpteifujvkpazargvkfpmhdgqvvueyglqxjrkolivqabczccpditkewavqadalxkgxwnuryxcodurzzayhjgabcmdghfehfdoihmvuvbawmmtqayoxxqympqnonpuwykkwpianjzdvrnwubucfrgewzolzlhegjptejsrvfeynoovxojmucgbhtwakimtbdzfrjsergewzazpchrswzlhwksgbvlxqtxpvpkfkrmeqknwzkwquyefhadceppgvzlduubrdrvqludkljwkoforwcgfmfyhydcykxaulphyfdgbjmtcracwxdomafmglodobkidpxqglrykfmzkcqasvteppffmhwihsytzqvymqtgaxywimajacvctbfafmsjnqeppcgusieefoihsgnzgyfeykavpyhrdxiaxeflbggcgoclrvrddwqmpbbwi
34384378
"""
