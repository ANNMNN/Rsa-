import random


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_large_prime():
    while True:
        p = random.randint(2 ** 15, 2 ** 16)
        if is_prime(p):
            return p


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e, phi):
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    while phi != 0:
        q = e // phi
        e, phi = phi, e % phi
        x1, x2 = x2 - q * x1, x1
        y1, y2 = y2 - q * y1, y1
    return x2

#Генерирую открытый и закрытый ключи
def generate_keypair():
    p = generate_large_prime()
    q = generate_large_prime()
    n = p * q
    phi = (p - 1) * (q - 1)  # Функция эйлера

    e = random.randrange(1, phi) # число Е
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi) # число закрытой экспоненты, с помощью открытой

    return ((e, n), (d, n))

# Шифрует - преобразуя каждый символ сообщения в его числовое представление, затем применяет операцию возведения в степень по модулю n.
def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

# возведения в степень по модулю n, затем преобразует полученные числа обратно в символы.
def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)


public_key, private_key = generate_keypair()
message = "RSA"
encrypted_message = encrypt(public_key, message)
decrypted_message = decrypt(private_key, encrypted_message)

print('Открытый ключ:', public_key)
print('Закрытый ключ:', private_key)
print('Сообщение:', message)
print('Зашифрованное:', encrypted_message)
print('Расшифрованное:', decrypted_message)