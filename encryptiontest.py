import rsa
import os
import secrets
import string
import hashlib
from ecdsa import SigningKey, NIST192p


def generate_keys():
    return rsa.newkeys(1024)


def generate_signing_keys():
    sk = SigningKey.generate(curve=NIST192p)
    vk = sk.verifying_key
    #print(f"Sk {sk}")
    #print(f"VK {vk}")
    return (sk, vk)


def sign_msg(encrypted_message, sk):
    signature = sk.sign(encrypted_message)
    return signature


def verify_msg(signature, encrypted_message, vk):
    return vk.verify(signature, encrypted_message)


def encrypt_msg(message, publickey):
    encoded_msg = message.encode(encoding='UTF-8')
    encrypted_message = rsa.encrypt(encoded_msg, publickey)
    return encrypted_message


def decrypt_msg(encrypted_msg, privatekey):
    decrypted_message = rsa.decrypt(encrypted_msg, privatekey)
    decoded_msg = decrypted_message.decode()
    return decoded_msg


msg = input("Enter your message ")
publickey, privatekey = generate_keys()

#print(f"The private key is {privatekey}")
encrypted = encrypt_msg(msg, publickey)
#print(f"The encrypted message is {encrypted}")
decrypted = decrypt_msg(encrypted, privatekey)
#print(f"The decrypted message is {decrypted}")
sk, vk = generate_signing_keys()
#print(sk.to_string())
sign = sign_msg(encrypted, sk)
res={"signature":sign}
print(res)
#print(f"The signature is {sign}")
if(verify_msg(sign, encrypted, vk)):
    print("Verified")
else:
    print("Not verified")
