# leo-homework-week1-7
Problem:
The railfence cipher is a way of scrambling a message so as to make it unreadable. It works by breaking up the text into several pieces called rails. Suppose we wish to have $n$ rails. We form rail $i$ (where $0 \le i < n$) by starting with the character in position $i$ (assuming the first character is in position 0) and taking every $n^\text{th}$ character following. We then concatenate the rails in reverse order to form the scrambled string.

For example:
text = "This is a test."
2-rail example:
  rail 0: "Ti sats."
  rail 1: "hsi  et"
  cipher: "hsi  etTi sats."
3-rail example:
  rail 0: "Tss s"
  rail 1: "h  tt"
  rail 2: "iiae."
  cipher: "iiae.h  ttTss s"


Part (a): Write a function $\verb#encipher_fence#.$ It takes two parameters: the first is a string to scramble, and the second is the number of rails. It should return the scrambled text.

Part (b): Write a function $\verb#decipher_fence#.$ It takes two parameters: the first is a string to unscramble, and the second is the number of rails. It should return the original text.

Part (c): Write a function $\verb#decode_text#.$ It should take two parameters, a text to decode and a filename for a file containing a list of English words. It should return a deciphered text, reversing the railfence cipher. This would be easy if you knew the number of rails involved. Without that knowledge, you can still break the code: try different rail numbers (2, 3, 4, etc.) until you get a text that consists of English words. (You can assume that the number of rails will not be more than 10.) Not every word in the coded text may appear in the wordlist (for example, proper names). You should return the text with the most words in it, according to your list of valid words. Also make sure you ignore punctuation when you look up words in the word list. You can use the file $\verb#wordlist.txt#$ to check the validity of words.
