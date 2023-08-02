import base64


def Encryption(Sentence : str, n : int, e : int) -> str:
    return "".join([chr(pow(i,e,n)) for i in base64.b64encode(Sentence.encode('utf-8'))])


def Decryption(Sentence: str, n: int, d: int) -> str:
    return base64.b64decode("".join([chr(pow(j,d,n)) for j in [ord(i) for i in Sentence]])).decode('utf-8')


n = "오늘 날씨가 정말 좋고 더워 뒤지겠어요...."
n = Encryption(n,1517,1421)
print(n)
n = Decryption(n,1517,1061)
print(n)
