from Utils.Writer import Writer
import json

class LoginFailed(Writer):

    def __init__(self, device, msg):
        super().__init__(device)
        self.id = 20103
        self.device = device
        self.msg = msg

    def encode(self):
        self.config = json.load(open("Config.json"))
        
        self.writeInt(10)  # Error Code
        
        self.writeString()
        self.writeString() # Server Host
        
        self.writeString("")  # Unknown
        self.writeString(self.config["updateURL"])  # Update URL
        self.writeString(self.msg)  # Pop Up Text

        self.writeInt(0) # maintenance time
        self.writeBoolean(False) # Unknown

        self.writeString()
        self.writeString()

        self.writeInt(0)
        self.writeInt(3)

        self.writeString()
        self.writeString()

        self.writeInt(0)
        self.writeInt(0)

        self.writeBoolean(False)
        self.writeBoolean(False)