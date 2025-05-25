import traceback
from CryptoRC4.CryptoRC4 import CryptoRc4
from Packets.Factory import Packets


class Device:
    def __init__(self, socket=None):
        self.socket = socket
        self.crypto = CryptoRc4()

    def SendData(self, packet_id, data, version=None):
        encrypted_data = self.crypto.encrypt(data)
        packet_id_bytes = packet_id.to_bytes(2, 'big')
        version_bytes = (version or 0).to_bytes(2, 'big')
        length_bytes = len(encrypted_data).to_bytes(3, 'big')

        packet = packet_id_bytes + length_bytes + version_bytes + encrypted_data

        if self.socket:
            self.socket.send(packet)
        else:
            self.transport.write(packet)

    def decrypt(self, data):
        return self.crypto.decrypt(data)

    def process_packet(self, packet_id, payload):
        print(f'[*] Packet {packet_id} received')

        try:
            decrypted = self.decrypt(payload)

            if packet_id in availablePackets:
                message = availablePackets[packet_id](decrypted, self)
                message.decode()
                message.process()

        except Exception as e:
            print(f'[*] Error while decrypting / handling packet {packet_id}: {e}')
            traceback.print_exc()