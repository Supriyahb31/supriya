import cv2
import os
import string

image = cv2.imread("suppi.jpg")

message = input("Enter message to hide:")

password = input("Enter your password:")

d={}
c={}

for i in range(255):
    d[chr(i)]=i
    c[i] = chr(i)

m=0
n=0
z=0

for i in range(len(message)):
    image[n,m,z] = d[message[i]]
    n=n+1
    m=m+1
    z=(z+1)%3

cv2.imwrite("Encryptedmsg.jpg",image)

os.system("start Encryptedmsg.jpg")


msg=""

n=0
m=0
z=0

pas = input("Enter passcode for Decryption")

if password == pas:
    for i in range(len(message)):
        msg = msg+ c[image[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1) % 3
    print("Decryption message",msg)
else:
    print("Not valid key")