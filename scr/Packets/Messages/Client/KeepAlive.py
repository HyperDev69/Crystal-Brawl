from Packets.Messages.Server.KeepAliveOk import KeepAliveOk
from Utils.ByteStream import ByteStream


class KeepAlive(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        print('[*] KeepAliveMessage succesfully received!')

    def process(self):
        KeepAliveOk(self.device).Send()