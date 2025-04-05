import zlib, base64

def compress(inputFile, outputFile):
    with open(inputFile, 'r') as f:
        data = f.read()
        
    data_bytes = data.encode()
    compress_data = zlib.compress(data_bytes, 9)
    compress_data = base64.b64encode(compress_data)
    decode_data = compress_data.decode()
    
    with open(outputFile, 'w') as f:
        f.write(decode_data)
         

def decompress(inputFile, outputFile):
    with open(inputFile, 'r') as f:
        data = f.read()
        
    data_bytes = data.encode()
    decompress_data = base64.b64decode(data_bytes)
    decompress_data = zlib.decompress(decompress_data)
    decode_data = decompress_data.decode()
    
    with open(outputFile, 'w') as f:
        f.write(decode_data)
        