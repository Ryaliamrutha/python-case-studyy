# Case Study 35: Text Compression Using Character Runs

## Problem Statement
Encode a string by grouping consecutive repeated characters and displaying each character followed by its repetition count. Compare the original and encoded lengths.

## Objectives
1. Traverse a string character by character.
2. Count consecutive repeated characters.
3. Create an encoded string and compare lengths.

## Assumptions
- The input is a non-empty string.
- The encoded form uses character followed by count, including count 1.
- This simple method is for learning and may not shorten every input.

## Algorithm
1. Start.
2. Read the input string.
3. If it is empty, display a message.
4. Set current character and count.
5. Traverse the remaining characters.
6. If the next character matches, increase count; otherwise append the previous character and count to the encoded string.
7. Append the final character group.
8. Display encoded string and length comparison.

## Flowchart
```text
START
  |
INPUT AND VALIDATE DATA
  |
PROCESS USING LOOPS / CONDITIONS
  |
DISPLAY RESULTS
  |
STOP
```

## Pseudocode
```text
START
INPUT text
IF text is empty: DISPLAY Empty input
ELSE
  SET encoded = empty string
  SET current = first character, count = 1
  FOR each next character
    IF character = current: count += 1
    ELSE
      APPEND current and count to encoded
      SET current = character, count = 1
    END IF
  END FOR
  APPEND final current and count
  DISPLAY encoded and lengths
END IF
STOP
```

## Python Source Code
```python
text = input("Enter text to encode: ")

if len(text) == 0:
    print("Empty input")
else:
    encoded = ""
    current = text[0]
    count = 1

    for i in range(1, len(text)):
        if text[i] == current:
            count = count + 1
        else:
            encoded = encoded + current + str(count)
            current = text[i]
            count = 1

    encoded = encoded + current + str(count)

    print("Original text:", text)
    print("Encoded text:", encoded)
    print("Original length:", len(text))
    print("Encoded length:", len(encoded))

    if len(encoded) < len(text):
        print("Encoding reduces the length")
    else:
        print("Encoding does not reduce the length")
```

## Test Cases
- Test 1: aaabbc → a3b2c1; encoded length 6
- Test 2: abcd → a1b1c1d1; encoding does not reduce length
- Test 3: aaaa → a4

## Sample Output
```text
Enter text to encode: aaabbc
Original text: aaabbc
Encoded text: a3b2c1
Original length: 6
Encoded length: 6
Encoding does not reduce the length
```

## Conclusion
The program uses string traversal and repetition counting to demonstrate a basic run-length encoding technique and compare string lengths.
