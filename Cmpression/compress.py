import zlib, base64

# with open('Cmpression/demo.txt', 'r') as f:
#     data = f.read()
    
# data_bytes = bytes(data,'utf-8')
# compressed_data = zlib.compress(data_bytes, 9)
# compressed_data = base64.b64encode(compressed_data)
# decode_data = compressed_data.decode('utf-8')

# with open('Cmpression/compress.txt', 'w') as f:
#     f.write(decode_data)


with open('Cmpression/compress.txt', 'r') as f:
    data = f.read()
    
data_bytes = data.encode()
decompressed_data = base64.b64decode(data_bytes)
decompressed_data = zlib.decompress(decompressed_data)
decode_data = decompressed_data.decode()

print(decode_data)