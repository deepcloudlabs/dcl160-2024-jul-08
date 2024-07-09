message1 = b"\xf0\x9d\x84\x9e"  # 𝄞
print(message1)
message2 = message1.decode("utf-8")
print(message2)
message3 = "𝄞"
print(message3)
message4 = message3.encode("utf-8")
print(message4)
message5 = "₺"
print(message5)
message6 = message5.encode("utf-8")
print(message6)
