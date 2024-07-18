# Clocks

## Description

The aim of this challenge is to arrange a series of clock face images showing different times into chornological order.

The clock faces are variations on a simple 12 hour analogue clock. A clock face showing 3:50 should be ordered before a clock face showing 10:45. For the purposes of this challenge a clock face showing anything in the range 12:00 to 12:59 should be ordered before a clock face showing 1:00 or later.

The clock face images will be given in a random order and you have to return a comma separated string that indicates the proper chronological position for each clock face image.
Example:

If we were to give you 3 images showing:

10:45

3:20

7:50

then image 1 (3:20) would be the earliest, image 2 (7:50) is next and image 0 (10:45) should be last. (Note the zero based indexing)

A correct response string for this example would be:

1,2,0

We won't be giving you 3 images we will be giving you 12 and they will be Base64 encoded.

Image examples can be found in the sample.zip file.

Start the clock...

Connection info: nc 54.79.244.247 9875

## Files

* [samples.zip](files/samples.zip)

