# program to convert emoji in sentences
message_input = input("> ")
words = message_input.split(" ")
emojis = {
    ":)" : "😊",
    ":(" : "😒"
}
output_txt = ""
for word in words:
    output_txt += emojis.get(word, word) + " "

print(output_txt)