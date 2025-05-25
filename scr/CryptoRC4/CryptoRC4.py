from Crypto.Cipher import ARC4

class CryptoRc4:
    def __init__(self):
        self.key = b'fhsd6f86f67rt8fw78fw789we78r9789wer6re'
        self.nonce = b'nonce'
        self.full_key = self.key + self.nonce

        self.RC4_Stream = ARC4.new(self.full_key)
        self.RC4_Stream.encrypt(self.full_key)

        self.RC4_Stream2 = ARC4.new(self.full_key)
        self.RC4_Stream2.encrypt(self.full_key)

    def decrypt(self, data: bytes) -> bytes:
        return self.RC4_Stream.encrypt(data)

    def encrypt(self, data: bytes) -> bytes:
        return self.RC4_Stream2.encrypt(data)