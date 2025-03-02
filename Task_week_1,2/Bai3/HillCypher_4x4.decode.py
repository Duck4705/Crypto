#Tính định thức
def calculate_det(matrix):
    # Tách ma trận thành các phần tử riêng biệt
    a, b, c, d = matrix[0]
    e, f, g, h = matrix[1]
    i, j, k, l = matrix[2]
    m, n, o, p = matrix[3]

    # Tính định thức theo công thức khai triển
    det = (
            a * (f * (k * p - l * o) - g * (j * p - l * n) + h * (j * o - k * n))
            - b * (e * (k * p - l * o) - g * (i * p - l * m) + h * (i * o - k * m))
            + c * (e * (j * p - l * n) - f * (i * p - l * m) + h * (i * n - j * m))
            - d * (e * (j * o - k * n) - f * (i * o - k * m) + g * (i * n - j * m))
    )
    return det

# Hàm tạo ma trận khóa 4x4 từ key
def getKeyMatrix(key):
    keyMatrix = [[0] * 4 for _ in range(4)]
    k = 0
    for i in range(4):
        for j in range(4):
            keyMatrix[i][j] = (ord(key[k]) - 65) % 26  # A=0, B=1, ..., Z=25
            k += 1
    return keyMatrix

# Hàm tính nghịch đảo modulo 26 của định thức
def mod_inverse(det, mod=26):
    for i in range(1, mod):
        if (det * i) % mod == 1:
            return i
    raise ValueError("Không tìm thấy nghịch đảo modulo 26.")

# Hàm tính ma trận nghịch đảo (tự code)
def modInverseMatrix(matrix):
    det = calculate_det(matrix) % 26

    det_inv = mod_inverse(det)

    # Tính ma trận phụ hợp (adjugate)
    adj = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            minor = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
            minor_det = calculate_det(minor)
            adj[j][i] = ((-1) ** (i + j)) * minor_det  # Transpose và đổi dấu
            adj[j][i] = adj[j][i] % 26

    # Nhân với det_inv và mod 26
    inverse = [[(adj[i][j] * det_inv) % 26 for j in range(4)] for i in range(4)]
    return inverse

# Hàm mã hóa
def hillCipherEncrypt(plaintext, keyMatrix):
    message = [(ord(c) - 65) % 26 for c in plaintext]
    cipher = [0] * 4
    for i in range(4):
        cipher[i] = sum(keyMatrix[i][j] * message[j] for j in range(4)) % 26
    return ''.join([chr(c + 65) for c in cipher])

# Hàm giải mã
def hillCipherDecrypt(ciphertext, keyMatrix):
    inverseKey = modInverseMatrix(keyMatrix)
    message = [(ord(c) - 65) % 26 for c in ciphertext]
    plain = [0] * 4
    for i in range(4):
        plain[i] = sum(inverseKey[i][j] * message[j] for j in range(4)) % 26
    return ''.join([chr(p + 65) for p in plain])

# Hàm chính
def main():
    plaintext = input("Nhập plaintext (4 ký tự): ").upper()
    key = input("Nhập key (16 ký tự): ").upper()

    keyMatrix = getKeyMatrix(key)
    print("Ma trận khóa:")
    for row in keyMatrix:
        print(row)

    try:
        ciphertext = hillCipherEncrypt(plaintext, keyMatrix)
        print("Ciphertext:", ciphertext)
        decrypted = hillCipherDecrypt(ciphertext, keyMatrix)
        print("Giải mã:", decrypted)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()