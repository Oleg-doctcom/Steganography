# from stegano import lsb
#
# secret= lsb.hide("img/1.png", "Secret text")
# secret.save("img/1_secret.png")
#
# result= lsb.reveal("img/1_secret.png")
# print(result)


# from stegano import exifHeader
# secrets=exifHeader.hide("img/2.jpg", "img/2_secret.jpg", "Закодирован")
#
# result= exifHeader.reveal("img/2_secret.jpg")
# result= result.decode()
# print(result)

from steganocryptopy.steganography import  Steganography

Steganography.generate_key("")
secret= Steganography.encrypt("key.key","img/3.png", "awa.txt")
secret.save("img/3_secret.png")

result =Steganography.decrypt("key.key","img/3_secret.png")
print(result)