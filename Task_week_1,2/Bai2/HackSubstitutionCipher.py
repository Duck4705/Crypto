from collections import Counter
import string

# Known English letter frequencies (from most frequent to least frequent)
english_frequencies = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

#
cipher_text = ("Rnw rqrxw twawth rv rnw hrvtb'h jsqm smrsfvmqhr, rnw Lstz Xvtl Hsktvm, unv qm sm wstxqwt sfw otwsrwl rnw Vmw Tqmf, sxxvuqmf nqj rv tkxw rnw vrnwt Tqmfh va Cvuwt fqywm rv jwm, lustywh, sml wxywh, qm nqh osjcsqfm rv ovmpkwt sxx va Jqllxw-wstrn. Atvj nvjwxb ewfqmmqmfh qm rnw Hnqtw, s nveeqr xsml twjqmqhowmr va rnw Wmfxqhn ovkmrtbhqlw, rnw hrvtb tsmfwh sotvhh Jqllxw-wstrn, avxxvuqmf rnw pkwhr rv lwhrtvb rnw Vmw Tqmf, hwwm jsqmxb rntvkfn rnw wbwh va rnw nveeqrh Atvlv, Hsj, Jwttb, sml Cqccqm. Sqlqmf rnw nveeqrh stw rnw uqdstl Fsmlsxa, rnw jwm Stsfvtm sml Evtvjqt, rnw wxa Xwfvxsh, sml rnw lusta Fqjxq, unv kmqrw sh rnw Ovjcsmb va rnw Tqmf qm vtlwt rv tsxxb rnw Atww Cwvcxwh va Jqllxw-wstrn sfsqmhr Hsktvm'h stjqwh sml fqyw Atvlv s onsmow rv lwhrtvb rnw Vmw Tqmf qm rnw aqtwh va Jvkmr Lvvj.")
# Count letter frequencies in the ciphertext (ignoring non-alphabet characters)
cipher_counts = Counter(''.join(filter(str.isalpha, cipher_text.upper())))

# Sort the ciphertext letters by frequency (most frequent first)
sorted_cipher = ''.join([item[0] for item in cipher_counts.most_common()])

# Create an initial mapping from ciphertext letters to the English frequency order
mapping = {}
for i, letter in enumerate(sorted_cipher):
    mapping[letter] = english_frequencies[i]

# For any letters not present in the ciphertext, add an identity mapping
for letter in string.ascii_uppercase:
    if letter not in mapping:
        mapping[letter] = letter

# Optional manual adjustments to improve decryption quality
mapping["H"] = "S"
mapping["R"] = "T"
mapping["S"] = "A"
mapping["T"] = "R"
mapping["V"] = "O"
mapping["B"] = "Y"
mapping["Q"] = "I"
mapping["M"] = "S"
mapping["U"] = "W"
mapping["J"] = "M"
mapping["A"] = "F"
mapping["M"] = "N"
mapping["F"] = "G"
mapping["O"] = "C"
mapping["K"] = "U"
mapping["P"] = "Q"
mapping["Z"] = "K"
mapping["D"] = "Z"
def print_key_mapping_table(mapping):
    """
    Displays the key mapping in the requested table format:
    
     A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
     --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--
     R  A  T  X  U  K  E  Y  H  O  I  D  V  F  G  M  P  L  Z  W  S  Q  J  C  B  N
    """
    plain_letters = list(string.ascii_uppercase)
    # Build the first row: plain letters with a fixed width (2 characters per letter)
    row1 = " ".join(f"{letter:2}" for letter in plain_letters)
    # Build the border row: "--+--+...+--"
    row2 = " " + "--" + "+--"*(len(plain_letters)-1) + " "
    # Build the third row: corresponding cipher letters from the mapping
    row3 = " ".join(f"{mapping[letter]:2}" for letter in plain_letters)
    
    print(row1)
    print(row2)
    print(row3)

# Display the final mapping using the desired table format
print_key_mapping_table(mapping)

# Decrypt the ciphertext using the mapping (preserving letter case)
decrypted_text = []
for char in cipher_text:
    if char.isalpha():
        if char.isupper():
            decrypted_text.append(mapping.get(char, char))
        else:
            decrypted_text.append(mapping.get(char.upper(), char.upper()).lower())
    else:
        decrypted_text.append(char)
decrypted_text = ''.join(decrypted_text)

print("\nDecrypted Text:")
print(decrypted_text)
