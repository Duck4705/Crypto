# Tạo một ma trận key 2*2
keyMatrix = [[0] * 2 for i in range(2)]
# Tạo ma trận 2*1 để chứa 2 ký tự cần giải mã
messageVector = [[0] for i in range(2)]
# Ma trận kết quả sau giải mã
plainMatrix = [[0] for i in range(2)]

# Biến key vừa nhập thành một ma trận 2*2 được đánh số theo thứ tự trong bảng chữ cái
def getKeyMatrix(key):
    k = 0
    for i in range(2):
        for j in range(2):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

# Tìm nghịch đảo modulo 26 của ma trận
def modInverseMatrix(matrix):
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26
    det_inv = pow(det, -1, 26)
    inv_matrix = [
        [matrix[1][1] * det_inv % 26, -matrix[0][1] * det_inv % 26],
        [-matrix[1][0] * det_inv % 26, matrix[0][0] * det_inv % 26],
    ]
    for i in range(2):
        for j in range(2):
            inv_matrix[i][j] = inv_matrix[i][j] % 26
    return inv_matrix

# Giải mã bằng cách nhân nghịch đảo ma trận keyMatrix với messageVector để có plainMatrix
def decrypt(messageVector, inverseKeyMatrix):
    for i in range(2):
        plainMatrix[i][0] = 0
        for x in range(2):
            plainMatrix[i][0] += (inverseKeyMatrix[i][x] * messageVector[x][0])
        plainMatrix[i][0] = plainMatrix[i][0] % 26

# Thuật toán giải mã Hill Cipher 2*2
def HillCipherDecrypt(ciphertext, key):
    # Tạo khóa
    getKeyMatrix(key)

    # Tìm nghịch đảo của ma trận khóa
    inverseKeyMatrix = modInverseMatrix(keyMatrix)

    # Biến các chữ cái được đánh số giống trong bảng chữ cái
    for i in range(2):
        messageVector[i][0] = ord(ciphertext[i]) % 65

    # Giải mã
    decrypt(messageVector, inverseKeyMatrix)

    # Biến đoạn code sau thành lại chuỗi
    PlainText = []
    for i in range(2):
        PlainText.append(chr(plainMatrix[i][0] + 65))
    return "".join(PlainText)

# Hàm khởi tạo
def main():
    # Nhập một chuỗi đã được mã hóa có 2 ký tự
    while True:
        ciphertext = input("Enter a cipher text (2 characters): ")
        if len(ciphertext) == 2:
            break
    # Nhập key có 4 ký tự
    while True:
        key = input("Enter a key (4 characters): ")
        if len(key) == 4:
            break
    # Chuỗi sau giải mã
    plaintext = HillCipherDecrypt(ciphertext.upper(), key.upper())
    print(plaintext)

if __name__ == "__main__":
    main()
