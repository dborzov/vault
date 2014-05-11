hashlib.sha1(fh.read()).hexdigest() #sha1 things!


string_to_encode = hmac.new(str(secret), str("superstring!"), hashlib.sha1).digest()
secret =  base64.b64encode(string_to_encode)
