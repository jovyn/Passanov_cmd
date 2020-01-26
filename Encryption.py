from Crypto.Cipher import Blowfish
from struct import pack

def EncryptData(account_name, username, passcode, comments, master_code, secret_code):
    key = str(master_code + "!@#$%^&*" + secret_code).encode('utf-8')
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)
    bs = Blowfish.block_size
    data_string = str(account_name + ":" + username + ":" + passcode + ":" + comments).encode('utf-8')
    plen = bs - len(data_string) % bs
    padding = [plen] * plen
    padding = pack('b'*plen, *padding)
    encrypted_data = cipher.iv + cipher.encrypt(data_string + padding)

    return encrypted_data

def DecryptData(encrypted_data, mpass, secKey):
    decrypt_key = str(mpass + "!@#$%^&*" + secKey).encode('utf-8')
    cipher = Blowfish.new(decrypt_key, Blowfish.MODE_CBC)
    decryption = cipher.decrypt(encrypted_data)

    return decryption
