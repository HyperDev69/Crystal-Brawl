from Utils.Writer import Writer

class ClubData(Writer):
           def __init__(self, device):
               self.id = 24399
               self.device = device
               super().__init__(self.device)

           def encode(self):
               isInClub = False
               if isInClub:
                      pass