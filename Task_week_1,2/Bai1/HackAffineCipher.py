import string


#Hàm check xem coi a có phải là ước chung của 26 không, với m mặc định là 26 chữ cái
def mod_inverse(a, m):
    """
    Computes the modular inverse of a modulo m using a simple brute-force approach.
    Returns the inverse if it exists, else None.
    """
    a = a % m
    for x in range(1, m):

        if (a * x) % m == 1:
            return x
    return None
#Hàm ánh xạ chữ cái theo công thức y = (ax + b) % 26
def affine_mapping(a, b):
    """
    Generates a dictionary mapping for the Affine cipher (for uppercase letters).
    For each letter with index x (A=0, B=1, …, Z=25), compute:
      mapped_index = (a * x + b) mod 26
    """
    mapping = {}
    alphabets = string.ascii_uppercase
    for i, letter in enumerate(alphabets):
        mapped_index = (a * i + b) % 26
        mapping[letter] = alphabets[mapped_index]
    return mapping

#Hàm in ra bảng chữ cái 1 : 1 sau khi đã được ánh xạ gồm có ba dòng: dòng một từ A-Z, dòng hai viền, dòng 3 : các chữ cái đã được ánh xạ theo thứ tự từ A - Z
def print_affine_mapping_table(a, b):
    """
    Displays the Affine cipher mapping in a two-line table:
    - First row: Plain letters (A-Z)
    - Second row: A border
    - Third row: Cipher letters (resulting from the affine mapping)
    """
    mapping = affine_mapping(a, b)
    plain_letters = list(string.ascii_uppercase)

    # Row with plain letters, each formatted to a width of 2
    row1 = " ".join(f"{letter:2}" for letter in plain_letters)
    # Border row
    row2 = " " + "--" + "+--" * (len(plain_letters) - 1) + " "
    # Row with cipher letters from the mapping
    row3 = " ".join(f"{mapping[letter]:2}" for letter in plain_letters)

    print(row1)
    print(row2)
    print(row3)

#Hàm này mã hóa bắt đầu mã hóa từng chữ cái một với khóa a và b và có phân biệt chữ hoa chữ thường
def affine_encrypt(text, a, b):
    """
    Encrypts the input text using the Affine cipher with keys a and b.
    Uppercase and lowercase letters are handled; non-alphabetic characters are left unchanged.
    """
    mapping = affine_mapping(a, b)
    result = []
    for char in text:
        if char.isupper():
            result.append(mapping.get(char, char))
        elif char.islower():
            # Convert to uppercase, map, then convert back to lowercase.
            result.append(mapping.get(char.upper(), char.upper()).lower())
        else:
            result.append(char)
    return ''.join(result)
#Hàm mã hóa
def affine_decrypt(text, a, b):
    """
    Decrypts the input text using the Affine cipher with keys a and b.
    Computes the modular inverse of a and applies the decryption formula:
      D(y) = a_inv * (y - b) mod 26.
    """
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError(f"No modular inverse for a = {a}. Please choose a value of 'a' that is coprime with 26.")

    alphabets = string.ascii_uppercase
    result = []
    for char in text:
        if char.isupper():
            y = ord(char) - ord('A')
            x = (a_inv * (y - b)) % 26
            result.append(alphabets[x])
        elif char.islower():
            y = ord(char.upper()) - ord('A')
            x = (a_inv * (y - b)) % 26
            result.append(alphabets[x].lower())
        else:
            result.append(char)
    return ''.join(result)

def main():
    try:
        a = int(input("Enter the key 'a' in (a * x + b) mod 26 for the Affine cipher (must be coprime with 26): "))
        b = int(input("Enter the key 'b' in (a * x + b) mod 26 for the Affine cipher (an integer): "))
    except ValueError:
        print("Invalid input. Please enter integers for keys a and b.")
        return

    # Ensure that 'a' is coprime with 26.
    if mod_inverse(a, 26) is None:
        print(f"Key 'a' = {a} is not coprime with 26. Please choose a different value for 'a'.")
        return

    print("\nAffine Cipher Key Mapping:")
    print_affine_mapping_table(a, b)

    plaintext = input("\nEnter the text to encrypt: ")
    encrypted_text = affine_encrypt(plaintext, a, b)
    print("\nEncrypted text:")
    print(encrypted_text)


    #Đoạn code này dùng để brute force mà khi không biết trước key với điều kiện biết vùng giới hạn của a và b
    #Giới hạn của a là số không phải ước chung với 26 nằm trong đoạn từ [1,26]
    #Giới hạn của b là số nằm trong đoạn [1,25]
    #Tổng số vòng loop tối đa là 300 lần nếu sử dụng brute force
    n = 0 # Dùng để đém số lần thứ n brute force
    for a_term in range(1, 26):
        for b_term in range(1, 25):
            #Dòng này kiểm tra xem a có phải là ước chung của 26 không nếu có bỏ qua không thực hiện gì cả
            if mod_inverse(a_term, 26) == None:
                continue
            n+=1
            #Dòng dưới đây là giải mã với a, b được chọn ra trong đoạn nhắc ở trên
            input(f"\nPress Enter to continue to brute force with a = {a_term}, b = {b_term} n = {n}...")
            output = affine_decrypt(encrypted_text, a_term, b_term)
            print("\nDecrypted text:")
            print(output)


if __name__ == "__main__":
    main()