# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    my_file = open(file_name, "r")
    chars = []
    s=''
    message = ""
    for line in my_file:
       for c in line:
           chars.append(c)
    message = s.join(chars[::2])
    print(message)

decrypt("duplicated_chars.txt")
