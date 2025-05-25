import time
from Utils.Writer import Writer

class LoginOk(Writer):

    def __init__(self, device):
        self.id = 20104
        self.version = 1
        self.device = device
        super().__init__(self.device)

    def encode(self):
        self.writeInt(0)  # Account High ID
        self.writeInt(1)  # Account Low ID
        
        self.writeInt(0)  # Home High ID
        self.writeInt(1)  # Home Low ID
        
        self.writeString("erzkw78p83t73sbm6c4ms2ww8894fynmzc3xyntf")  # Player Token
        self.writeString("61576296792772")  # Facebook ID
        self.writeString("G:325378671")  # Game Center ID
        
        self.writeInt(2)  # Major
        self.writeInt(57)  # Minor
        self.writeInt(2)  # Build
        
        self.writeString("prod")  # Environment 
        
        self.writeInt(0)  # Session Count
        self.writeInt(0)  # Play Time Seconds
        self.writeInt(0)  # Days Since Started Playing
        
        self.writeString()  # Unknown
        self.writeString()  # Unknown
        self.writeString()  # Unknown
        
        self.writeInt(0)  # Unknown
        
        self.writeString()  # Unknown
        self.writeString("IT")  # Region
        self.writeString()  # Unknown
        
        self.writeInt(1)  # Unknown
        
        self.writeString()  # Unknown
        self.writeString()  # Unknown
        self.writeString()  # Unknown