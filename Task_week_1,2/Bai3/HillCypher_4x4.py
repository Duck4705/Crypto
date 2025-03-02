#Tạo một ma trận key 4*4
keyMatrix = [[0] * 4 for i in range(4)]
#Tạo ma trận 1*2 để chứa 2 ký tự cần mã hóa
messageVector = [[0] for i in range(4)]
#Ma trân kết quả sau mã hóa
cipherMatrix = [[0] for i in range(4)]

#Biến key vừa nhập thành một trận 4*4 được đánh số theo thứ tự trong bảng chữ cái
def getKeyMatrix(key):
    k = 0
    for i in range(4):
        for j in range(4):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

#Mã hóa bằng cách nhân ma trận keyMatrix * messageVector = cipherMatrix
#Sau khi có cipherMatrix cần mod 26 để nó nằm trong phạm vi của bảng chữ cái
def encrypt(messageVector):
    for i in range(4):
        cipherMatrix[i][0] = 0
        for x in range(4):
            cipherMatrix[i][0] += (keyMatrix[i][x] * messageVector[x][0])
        cipherMatrix[i][0] = cipherMatrix[i][0] % 26

#Thuật toán mã hóa HillCipher 4*4
def HillCipher(message, key):
    #Tạo khóa
    getKeyMatrix(key)

    #Biến các chữ cái được đánh số giống trong bảng chữ cái
    for i in range(4):
        messageVector[i][0] = ord(message[i]) % 65
    #Mã hóa
    encrypt(messageVector)

    #Biến đoạn code sau thành lại chuỗi
    CipherText = []
    for i in range(4):
        CipherText.append(chr(cipherMatrix[i][0] + 65))
    return "".join(CipherText)

#Hàm khởi tạo
def main():
    #Nhập một chuỗi có 4 ký tự nếu sai nhập lại
    while True:
        plaintext = input("Enter a string(4 characters): ")
        if len(plaintext) == 4:
            break
    #Nhập key có 16 ký tự nếu sai nhập lại
    while True:
        key = input("Enter a key(16 characters): ")
        if len(key) == 16:
            break
    #Chuỗi sau mã hóa. In hoa trước khi đi vào mã hóa
    ciphertext = HillCipher(plaintext.upper(), key.upper())
    print(ciphertext)

if __name__ == "__main__":
    main()