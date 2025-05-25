from Utils.ByteStream import ByteStream

from Packets.Messages.Server.Login.LoginOk import LoginOk
from Packets.Messages.Server.OwnHomeData import OwnHomeData
from Packets.Messages.Server.Club.ClubData import ClubData
from Packets.Messages.Server.Login.LoginFailed import LoginFailed

import json

class Login(ByteStream):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        self.config = json.load(open("Config.json"))

    def process(self):
        if self.config["maintenance"]: 
            LoginFailed(self.device, "The Server is Currently Under Maintenance!\n Try Again Later").Send()  # 20103
        else:
            LoginOk(self.device).Send()  # 20104
            OwnHomeData(self.device).Send()  # 24101
            ClubData(self.device).Send()  # 24399