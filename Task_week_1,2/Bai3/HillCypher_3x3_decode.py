import numpy as np

# Tạo một ma trận key 3x3
keyMatrix = np.zeros((3,3), dtype=int)
# Tạo ma trận 1x3 để chứa 3 ký tự cần giải mã
messageVector = np.zeros((3,1), dtype=int)
# Ma trận kết quả sau giải mã
plainMatrix = np.zeros((3,1), dtype=int)

# Biến key vừa nhập thành một ma trận 3x3 được đánh số theo thứ tự trong bảng chữ cái
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

# Tìm nghịch đảo modulo 26 của ma trận sử dụng numpy
def modInverseMatrix(matrix):
    det = int(round(np.linalg.det(matrix))) % 26
    if np.gcd(det, 26) != 1:
        raise ValueError("Determinant không có nghịch đảo modulo 26")
    det_inv = pow(det, -1, 26)

    adjugate_matrix = np.round(np.linalg.inv(matrix) * det).astype(int) % 26

    inverse_matrix = (det_inv * adjugate_matrix) % 26
    return inverse_matrix

# Giải mã bằng cách nhân nghịch đảo ma trận keyMatrix với messageVector để có plainMatrix
def decrypt(messageVector, inverseKeyMatrix):
    plainMatrix[:] = np.dot(inverseKeyMatrix, messageVector) % 26

# Thuật toán giải mã Hill Cipher 3x3
def HillCipherDecrypt(ciphertext, key):
    # Tạo khóa
    getKeyMatrix(key)

    # Tìm nghịch đảo của ma trận khóa
    inverseKeyMatrix = modInverseMatrix(keyMatrix)

    # Biến các chữ cái được đánh số giống trong bảng chữ cái
    for i in range(3):
        messageVector[i][0] = ord(ciphertext[i]) % 65

    # Giải mã
    decrypt(messageVector, inverseKeyMatrix)

    # Biến đoạn code sau thành lại chuỗi
    PlainText = ''.join(chr(int(plainMatrix[i][0] + 65)) for i in range(3))
    return PlainText

# Hàm khởi tạo
def main():
    # Nhập một chuỗi đã được mã hóa có 3 ký tự
    while True:
        ciphertext = input("Enter a cipher text (3 characters): ")
        if len(ciphertext) == 3:
            break
    # Nhập key có 9 ký tự
    while True:
        key = input("Enter a key (9 characters): ")
        if len(key) == 9:
            break
    # Chuỗi sau giải mã
    try:
        plaintext = HillCipherDecrypt(ciphertext.upper(), key.upper())
        print(plaintext)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
