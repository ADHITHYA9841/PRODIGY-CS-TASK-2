print("##########image encrypter##########")
print("by adhithya mangalampeta ")
from PIL import Image

def encrypt_image(image_path, output_path, key):
    # Open the image
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure image is in RGB mode
    
    # Get the width and height of the image
    width, height = img.size
    
    # Create a new image for the encrypted data
    encrypted_img = Image.new("RGB", (width, height))
    
    # Encrypt each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            encrypted_img.putpixel((x, y), (r, g, b))
    
    # Save the encrypted image
    encrypted_img.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    img = img.convert("RGB")
    
    # Get the width and height of the image
    width, height = img.size
    
    # Create a new image for the decrypted data
    decrypted_img = Image.new("RGB", (width, height))
    
    # Decrypt each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            decrypted_img.putpixel((x, y), (r, g, b))
    
    # Save the decrypted image
    decrypted_img.save(output_path)
    print(f"Decrypted image saved to {output_path}")

if __name__ == "__main__":
    import os
    
    # User input for image paths and key
    image_path = input("Enter the path to the image: ")
    encrypted_output_path = "encrypted_image.png"
    decrypted_output_path = "decrypted_image.png"
    key = int(input("Enter an encryption key (integer): "))
    
    if not os.path.exists(image_path):
        print("The specified image path does not exist.")
    else:
        # Encrypt the image
        encrypt_image(image_path, encrypted_output_path, key)
        
        # Decrypt the image
        decrypt_image(encrypted_output_path, decrypted_output_path, key)
        
        print("Encryption and decryption complete.")
