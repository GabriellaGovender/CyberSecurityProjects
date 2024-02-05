#picoCTF challenge: basic-mod-1
import string
input = [165, 248, 94, 346, 299, 73, 198, 221, 313, 137, 205, 87, 336, 110, 186, 69, 223, 213, 216, 216, 177, 138]
symbols = string.ascii_uppercase + string.digits + "_"
flag = "".join(symbols[s%37] for s in input)
print("picoctf{{{}}}".format(flag))
