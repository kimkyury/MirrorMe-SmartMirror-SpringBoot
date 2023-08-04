import base64

def Encryption(Sentence : str, n : int, e : int) -> str: return "".join([chr(pow(i,e,n)) for i in base64.b64encode(Sentence.encode('utf-8'))])
def Decryption(Sentence: str, n: int, d: int) -> str: return base64.b64decode("".join([chr(pow(j,d,n)) for j in [ord(i) for i in Sentence]])).decode('utf-8')

n = "안녕하세요. 오늘 날씨가 너무 좋아서 죽을 것 같아요. 양산을 쓰면 훨씬 좋다네요. 양산 하나 사러 갈까요?"

N = 1517
PNA = 1421
PNB = 1061

n = Encryption(n,N,PNA)
print(n)
n = Decryption(n,N,PNB)
print(n)