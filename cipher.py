# -*- coding: utf-8 -*-
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64

rsa_key = '''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDWwRHPVDCD81vulmut/+ME1+Z
UMf9sf2S1jYmtTsOPP+cmYXFL7DCwWh59WOhVcHBsgcm6IYIJB8yCWP9T6mbeitK
RLq8UiCctp+aCLNW6Q1/DdD0mzw0JDtZsAWZ8cfze7K/gV7OmnB9fA4iA4Wix6K4
I68pwvafm3AyS12TSwIDAQAB
-----END PUBLIC KEY-----
'''
msg = '159753'


class rsa_encrypt():
    @staticmethod
    def rsa_enc(data, rsa_key):
        a = bytes(data, encoding='utf-8')
        rsakey = RSA.importKey(rsa_key)
        cipher = PKCS1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(a))
        b = str(cipher_text,encoding='utf-8')
        return b


if __name__ == '__main__':
    rsa_encrypt().rsa_enc(data=msg, rsa_key=rsa_key)
