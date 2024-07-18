# Hot Wheels

## Description

Access the system here: https://54.79.244.247:8500/

Usage:
Click on a wheel, and then type a letter to rotate that wheel to that letter. If the wheels are linked, this will also rotate all other wheels by the same amount.

Setting the key:
Click on two numbers at the top to swap the positions of the corresponding wheels. Repeat until you have the secret wheel order.

Encryption:
With the wheels unlinked, enter your 24-letter message along the centre row. Then click the "Link" button. Click the arrows a random number of times to rotate the wheels. The resulting centre row is your ciphertext.

Decryption:
With the wheels unlinked, enter your 24-letter ciphertext along the centre row. Then click the "Link" button. Click the arrows to rotate the wheel until you can read one that makes sense. This is *probably* the plaintext.

For example, under the default key 1,2,..,24:
"OHNOITSNONDETERMINISTICF" could encrypt to
"DUXGLRUBHQITIQDDBXPLVUIM" or "LVKLZDXQQMNDWPZCPZOZRGTB", and many other possibilities.

For longer texts, perform the encryption/decryption line-by-line.

The flag is hidden in the ciphertext.

## Files

* [ciphertext.txt](files/ciphertext.txt)

* [wheels.txt](files/wheels.txt)

