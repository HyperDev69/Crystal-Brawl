from Packets.Messages.Server.OwnHomeData import OwnHomeData
from Utils.ByteStream import ByteStream

class GoHome(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.data = data

    def decode(self):
        print('[*] GoHomeFromOfflineMessage succesfully received!')

    def process(self):
        OwnHomeData(self.device).Send()