#!/usr/bin/env python3
import os

def henon_map_keygen(length: int, x0: float, y0: float, a: float = 1.4, b: float = 0.3) -> bytes:
    """
    Generate a keystream of 'length' bytes using the Henon map.

    :param length: Number of bytes in the keystream
    :param x0: Initial x value (-1 < x0 < 1)
    :param y0: Initial y value (-1 < y0 < 1)
    :param a: Henon map parameter (default 1.4 for chaotic behavior)
    :param b: Henon map parameter (default 0.3 for chaotic behavior)
    :return: Keystream as bytes
    """
    x, y = x0, y0
    key = bytearray(length)

    for i in range(length):
        x, y = 1 - a * x ** 2 + y, b * x  # Henon map iteration
        key[i] = int((x % 1) * 256) & 0xFF  # Normalize x to [0, 255]

    return bytes(key)

def chaotic_encrypt_decrypt(input_path: str, output_path: str, x0: float, y0: float, a: float, b: float) -> bytes:
    """
    Encrypt or decrypt a file (any binary) using a Logistic map-based keystream.
    XOR is used for both encryption and decryption.

    :param input_path: path to the input file
    :param output_path: path to the output file
    :param x0: initial seed for the Logistic map
    :param r: parameter for the Logistic map
    """
    # Read entire file in binary mode
    with open(input_path, 'rb') as f_in:
        data = f_in.read()

    length = len(data)
    # Generate keystream of the same length
    key = henon_map_keygen(length, x0, y0, a, b)

    # XOR each byte
    result = bytes(d ^ k for d, k in zip(data, key))

    # Write result to output
    with open(output_path, 'wb') as f_out:
        f_out.write(result)

def main():
    print("=== Chaotic Map (Henon Map) Stream Cipher Demo ===")
    print("This script uses a simple XOR-based scheme with a Henon map keystream.")
    print("Disclaimer: Not secure for real-world cryptography.\n")

    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
    if mode not in ("encrypt", "decrypt"):
        print("Invalid mode. Use 'encrypt' or 'decrypt'.")
        return

    input_file = input("Enter path to input file: ").strip()
    output_file = input("Enter path to output file: ").strip()

    # Get seed x0 (-1 < x0 < 1), y (-1 < y0 < 1) and parameter a (commonly near 1.4), b (commonly near 0.3
    try:
        x0 = float(input("Enter henon map seed x0 (-1 < x0 < 1): ").strip())
        y0 = float(input("Enter henon map seed y0 (-1 < x0 < 1): ").strip())
        a = float(input("Enter henon map parameter r (e.g., 1.4): ").strip())
        b = float(input("Enter heno map parameter r (e.g., 0.3): ").strip())
    except ValueError:
        print("Invalid x0 or y0 or a or b. Must be float.")
        return

    if not (-1 < x0 < 1) and not (-1 < y0 < 1):
        print("x0,y0 must be between -1 and 1.")

        return

    # Perform the XOR-based operation
    # (Encryption and decryption are identical in this scheme.)
    chaotic_encrypt_decrypt(input_file, output_file, x0, y0, a, b)

    print(f"\nDone. {'Encrypted' if mode=='encrypt' else 'Decrypted'} file saved to '{output_file}'.")

if __name__ == "__main__":
    main()
