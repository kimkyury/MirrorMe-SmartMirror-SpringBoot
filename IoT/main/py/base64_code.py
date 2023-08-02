import base64

# bytes-like object만 가능
# temp = imread()
# base64_str = base64.b64encode(temp)
# print(base64_str)
# result = base64.b64decode(base64_str)
# print(result)

sitename = 'webisfree'
print(sitename)
sitename_bytes = sitename.encode('ascii')
print(sitename_bytes)
sitename_base64 = base64.b64encode(sitename_bytes)
print(sitename_base64)
sitename_base64_de = base64.b64decode(sitename_base64)
print(sitename_base64_de)
sitename_base64_str = sitename_base64_de.decode('ascii')
print(sitename_base64_str)