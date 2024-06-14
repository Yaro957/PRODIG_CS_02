import numpy as np
from PIL import Image


def encrypt(image_path, key):
    # open the image
    image = Image.open(image_path)

    # convert the image to numpy array
    image_array = np.array(image)

    key =np.resize(key,image_array.shape)

    # encrypting using xor
    encrypt_array =np.bitwise_xor(image_array, key)

    encrypted_image = Image.fromarray(encrypt_array)

    encrypted_image.save("encrypted_image.png")
    print("image encryted succesfully")

def decryption(image_path, key):
     # open the image
    image = Image.open(image_path)

    # convert the image to numpy array
    image_array = np.array(image)

    key =np.resize(key,image_array.shape)

    # decrypting using xor
    decrypt_array =np.bitwise_xor(image_array, key)

    decrypted_image = Image.fromarray(decrypt_array)
    
    
    decrypted_image.save("decrypted_image.png")
    print("image encryted succesfully")



     


image_path = input("enter the path of the image\n")
key = np.random.randint(0, 256 ,size=(3),dtype=np.uint8)

# encrypt the image
encrypt(image_path, key)

decryption("encrypted_image.png",key)
