# Stegosaurus

## Description

An organisation recently detected a cyber incident on their network. Their forensic investigation has found two strange images in outgoing network traffic, and they are worried that data may have been exfiltrated from their system. They would like you to help investigate these images to find what, if anything, may have been taken.

Use your analysis and reverse engineering skills to find any hidden data.

Here is some guidance:
1) Start with dinos.png - look at the end of the file.
2) Figure out what the encoded data is. Try redirecting it to a file at each stage and check the file types. Look for "spines".
3) Try making the code more readable. Separate out functions and rename variables.
4) What common steganography technique might work with single bits? How might a bitmask be applied when implementing this technique?
How might you reverse the steganography encoding?
5) Is the data placed at the beginning of the image? 

## Files

* [dinos.png](files/dinos.png)

* [stegosaurus.png](files/stegosaurus.png)

