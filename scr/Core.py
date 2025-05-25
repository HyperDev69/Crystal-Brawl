import socket
import argparse
import os
import json
import traceback

from threading import Thread

from Packets.Factory import Packets
from Logic.Device import Device

class Networking(Thread):
    def __init__(self, args):
        Thread.__init__(self)
        self.client = socket.socket()
        self.args = args
        self.config = json.load(open('Config.json'))

    def run(self):
        self.client.bind((self.config["address"], self.config["port"]))
        print(f'[*] Server started on {self.config["address"]}:{self.config["port"]}')

        while True:
            self.client.listen(5)
            client, address = self.client.accept()
            print('[*] New connection from {}'.format(address[0]))
            ClientThread(client, self.args, self.config).start()


class ClientThread(Thread):
    def __init__(self, client, debug, config):
        Thread.__init__(self)
        self.client = client
        self.device = Device(self.client)
        self.debug = debug
        self.config = config

    def recvall(self, size):
        data = []
        while size > 0:
            self.client.settimeout(5.0)
            s = self.client.recv(size)
            self.client.settimeout(None)
            if not s:
                print('[*] Error while sending data.')
                raise EOFError
            data.append(s)
            size -= len(s)
        return b''.join(data)

    def run(self):
        try:
            while True:
                header = self.client.recv(7)
                if len(header) < 7:
                    print('[*] Disconnection from client.')
                    self.client.close()
                    break

                packetid = int.from_bytes(header[:2], 'big')
                length = int.from_bytes(header[2:5], 'big')
                version = int.from_bytes(header[5:], 'big')
                data = self.recvall(length)

                if length == len(data):
                    print(f'[*] {packetid} with length {length} received.')

                    try:
                        decrypted = self.device.decrypt(data)
                        if packetid in Packets:
                            Message = Packets[packetid](decrypted, self.device)
                            Message.decode()
                            Message.process()
                        else:
                            if self.debug:
                                print(f'[*] {packetid} not handled.')
                    except:
                            print(f'[*] Error while decrypting / handling {packetid}.')
                            traceback.print_exc()
        except:
            self.client.close()


if __name__ == '__main__':
    width = os.get_terminal_size().columns
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    print('[*] Starting Crystal Brawl v2.57')
    Networking(args).start()