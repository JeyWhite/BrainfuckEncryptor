def Encrypt(text: str) -> str:
    decals: str = ""
    outs: str = ""
    for char in text:
        num = ord(char)
        dec = round(num, -1)
        decals += ">" + ("+" * int(dec/10))
        outs += ">" + ("+" if num > dec else "-")*abs(num-dec) + "."
    return "+" * 10 + "[" + decals + (len(text) * "<") + "-]" + outs


if __name__ == '__main__':
    print(Encrypt(input()))
