# Text Compression Using Character Runs
# Python Activity-Based Learning

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
