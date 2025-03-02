import numpy as np

# Tạo ma trận key 3x3
keyMatrix = [[0] * 3 for i in range(3)]
# Ma trận 1x3 để chứa 3 ký tự mã hóa
cipherVector = [[0] for i in range(3)]
# Ma trận chứa kết quả giải mã
plainMatrix = [[0] for i in range(3)]

# Biến key thành ma trận 3x3
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

# Tìm nghịch đảo modulo 26 của một số
def modInverse(a, m=26):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Tính ma trận nghịch đảo modulo 26
def getInverseKeyMatrix():
    matrix = np.array(keyMatrix)

    # Tính định thức và nghịch đảo định thức modulo 26
    det = int(round(np.linalg.det(matrix))) % 26
    det_inv = modInverse(det, 26)

    if det_inv is None:
        raise ValueError("Ma trận không khả nghịch modulo 26!")

    # Tính ma trận adjugate (phụ hợp)
    adjugate = np.round(np.linalg.inv(matrix) * np.linalg.det(matrix)).astype(int) % 26

    # Nhân với nghịch đảo của định thức mod 26
    inverseMatrix = (adjugate * det_inv) % 26
    return inverseMatrix.astype(int)

# Nhân ma trận nghịch đảo với ciphertext để giải mã
def decrypt(cipherVector, inverseKeyMatrix):
    for i in range(3):
        plainMatrix[i][0] = 0
        for x in range(3):
            plainMatrix[i][0] += (inverseKeyMatrix[i][x] * cipherVector[x][0])
        plainMatrix[i][0] = plainMatrix[i][0] % 26

# Thuật toán giải mã Hill Cipher 3×3
def HillCipherDecrypt(ciphertext, key):
    # Tạo khóa
    getKeyMatrix(key)

    # Tính ma trận nghịch đảo của key
    inverseKeyMatrix = getInverseKeyMatrix()

    # Chuyển ciphertext thành số
    for i in range(3):
        cipherVector[i][0] = ord(ciphertext[i]) % 65

    # Giải mã
    decrypt(cipherVector, inverseKeyMatrix)

    # Chuyển về dạng chữ cái
    plaintext = "".join([chr(plainMatrix[i][0] + 65) for i in range(3)])
    return plaintext

# Hàm khởi chạy chương trình
def main():
    # Nhập ciphertext (3 ký tự)
    while True:
        ciphertext = input("Enter a ciphertext(3 characters): ").upper()
        if len(ciphertext) == 3:
            break
    # Nhập key (9 ký tự)
    while True:
        key = input("Enter a key(9 characters): ").upper()
        if len(key) == 9:
            break
    try:
        plaintext = HillCipherDecrypt(ciphertext, key)
        print("Decrypted text:", plaintext)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
