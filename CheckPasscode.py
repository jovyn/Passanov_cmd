import requests
import hashlib

def CheckMasterPass(masterpass):
    #jovin
    master_hash = '8061781D28D569067A648539683D51993FD7D2ED798DFB414BF911013FE01CD5DA1F46A92A394CE40245AA7BB5CB45620AF8D4C9E5E63C70AE883A11904C059A'
    target_hash = str(hashlib.sha3_512(masterpass.encode('utf-8')).hexdigest()).upper()
    if master_hash == target_hash:
        return True
    else:
        print("Masterpassword is INCORRECT !!!")
        return False

def CheckSecretAns(secret_ans):
    secret = '0804218596A9FED7BE782D0CEE5883C5179B8F549D5BD8ADF6A2EC8147704AF123D6B6C7F07A296037FA4611F7413BC238CBDA6D67C68B317F5F9E90835DF843'
    secret_hash = str(hashlib.sha3_512(secret_ans.encode('utf-8')).hexdigest()).upper()
    if secret == secret_hash:
        return True
    else:
        print("WRONG Answer !!!")
        return False

def CheckPass(password):
    print(password)
    hash_val = hashlib.sha1(password.encode('utf-8'))
    hash_val_digest = hash_val.hexdigest()
    hash_5chars = str(hash_val_digest[:5].upper())
    hash_tail = str(hash_val_digest[5:].upper())
    response = requests.get('https://api.pwnedpasswords.com/range/' + hash_5chars) # Using HIBP Api v2
    #print(hash_5chars)
    print(response.status_code)
    print("---------")
    # print(response.content)
    # print("---------")
    hibp_hashes = response.text.splitlines()

    for hash_found in hibp_hashes:
        hash_to_compare = str(hash_found[:35])

        if hash_to_compare == hash_tail:
            count =  str(hash_found[36:])

            print(f"Password \" {password} \" has been found {count} times in the Wild !!")

            return True













