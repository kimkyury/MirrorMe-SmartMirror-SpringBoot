import string
import random
import qrcode

def mirror_id():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(20))

def make_qr(MIRRORID : str):
    img = qrcode.make(MIRRORID)
    img.save(f'./{MIRRORID}.png')

if __name__ == "__main__":
    make_qr(mirror_id())