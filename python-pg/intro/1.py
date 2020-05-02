message1 = "Hello World"
message2 = "CloudAcademy Labs"

print(message1 + " - " + message2)

print("%s - %s" % (message1, message2))

print("%s - %s" % (message1.upper(), message2.upper()))

words = [message1, message2]
for w in words:
    print(w, len(w))