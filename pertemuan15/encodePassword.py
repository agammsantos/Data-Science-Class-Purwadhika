# menggunakan enkripsi base64
import base64

# untuk mengetahui bentuk encode dari password gunakan
repr = base64.b64encode(b'password')
pws = repr.decode('utf-8')
print(pws)

#untuk menggunakan hasil encode tersebut di coding (python3) gunakan
base64.b64decode(b"<hasil encode password>").decode('utf-8')