# UTF-8 Validation
For this interview practice algorithm, UTF-8 is used.  A character in UTF-8 can be 1 to 4 bytes long, and a data set can contain multiple characters.

[UTF-8 Validation](/0x04-utf8_validation/)
* Write a Python method `def validUTF8(data)` that determines if a given data set represents a valid UTF-8 encoding:
  * A character in UTF-8 can be 1 to 4 bytes long.
  * The data set can contain multiple characters.
  * The data will be represented by a list of integers.
  * Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer.
  * Returns `True` if data is valid UTF-8 encoding, `False` otherwise