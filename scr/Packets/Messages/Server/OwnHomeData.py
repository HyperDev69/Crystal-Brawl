from Utils.Writer import Writer
from Logic.Milestones import Milestones
import json

class OwnHomeData(Writer):

    def __init__(self, device):
        self.id = 24101
        self.device = device
        super().__init__(self.device)

    def encode(self):
        self.config = json.load(open('Config.json'))
        
        self.writeVint(362687)  # Timestamp
        self.writeVint(0)  # Unknown
        
        self.writeVint(9999)  # Trophies
        self.writeVint(9999)  # Highest trophies
        
        self.writeVint(1488)  # Experience
        
        self.writeScID(28, 18)  # Profile icon
        
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        
        self.writeVint(0)  # Coins Got (?)
        self.writeVint(1)  # Control Mode [0 = tap to move 1 = joystick 2 = double joystick]
        self.writeBoolean(False)  # Battle Hints
        
        self.writeVint(0)  # Coins Boubler Coins
        self.writeVint(0)  # Coins Boost Seconds
        self.writeVint(0)  # Unknown
        self.writeVint(0)  # Timestamp
        self.writeVint(100)  # Box Cost (coins)
        self.writeVint(10)  # Box Cost (gems)
        self.writeVint(20)  # Coins boost cost
        self.writeVint(50)  # Coin boost %
        self.writeVint(50)  # Coin doubler cost
        self.writeVint(100)  # Coins doubled
        self.writeVint(1)  # Coin boost hours
        
        # Boxes Array
        self.writeVint(1)  # Def brawlers chips
        self.writeVint(2)  # Rare brawlers chips
        self.writeVint(10)  # Epic brawlers chips
        self.writeVint(60)  # Legendary brawlers chips
        # Boxes Array Ends
        
        # Brawlers Cost Array 
        self.writeVint(3)  # Def brawlers cost
        self.writeVint(10)  # Rare brawlers cost
        self.writeVint(70)  # Epic brawlers cost
        self.writeVint(500)  # Legendary brawlers cost
        # Brawlers Cost Array Ends
        
        # Events Count Array
        self.writeVint(4)  # Events count
        # Events Count Array Ends

        # Events Array
        self.writeVint(1)  # Event index
        self.writeVint(1)  # Brawlers needed to unlock event
        self.writeVint(2)  # Event index
        self.writeVint(3)  # Brawlers needed to unlock event
        self.writeVint(3)  # Event index
        self.writeVint(6)  # Brawlers needed to unlock event  
        self.writeVint(4)  # Event index
        self.writeVint(8)  # Brawlers needed to unlock event
        self.writeVint(3)  # Unknown
        # Events Array Ends
        
        # Available Events Array
        self.writeVint(1)  # Slot index
        self.writeVint(1)  # Slot number
        self.writeVint(0)  # Timer
        self.writeVint(60060)  # Time left
        self.writeVint(8)  # Bonus coins (when event type is 0 or 1)
        self.writeVint(0)  # Unknown
        self.writeVint(60)  # Coins to win
        self.writeVint(0)  # Type (0 = normal event 1 = double coins 2 = double xp 3 = both)
        self.writeScID(15, 5)
        self.writeVint(0)  # Coins collected
        self.writeVint(3)  # Event type
        self.writeString()  # Text on event (TID)    
        self.writeBoolean(False)  # "All experience collected" if True
  
        self.writeVint(2)  # Slot index
        self.writeVint(2)  # Slot number
        self.writeVint(0)  # Timer
        self.writeVint(16860)  # Time left
        self.writeVint(16)  # Bonus coins (when event type is 0 or 1)
        self.writeVint(0)  # Unknown
        self.writeVint(40)  # Coins to win
        self.writeVint(0)  # Type (0 = normal event 1 = double coins 2 = double xp 3 = both)
        self.writeScID(15, 15)  # Map
        self.writeVint(0)  # Coins collected
        self.writeVint(3)  # Event type
        self.writeString()  # Text on event (TID)   
        self.writeBoolean(False)  # "All experience collected" if True
 
        self.writeVint(3)  # Slot index 
        self.writeVint(3)  # Slot number
        self.writeVint(1)  # Timer
        self.writeVint(360)  # Time left
        self.writeVint(4)  # Bonus coins (when event type is 0 or 1)
        self.writeVint(0)  # Unknown
        self.writeVint(16)  # Coins to win
        self.writeVint(0)  # Type (0 = normal event 1 = double coins 2 = double xp 3 = both)
        self.writeScID(15, 14)  # Map
        self.writeVint(0)  # Coins collected
        self.writeVint(3)  # Event type
        self.writeString()  # Text on event (TID)
        self.writeBoolean(False)  # "All experience collected" if True
        # Available Events Array Ends
 
        # Coming Soon Events Array
        self.writeVint(4) # Event Slots Count
        for x in range(4):  # Like This for Better Management
            self.writeVint(0)  # Slot Index
            self.writeVint(x + 1) # Slot Number
            self.writeVint(6800) # New Event Timer 
            self.writeVint(0) # Time left
            self.writeVint(0) # # Bonus coins (when event type is 0 or 1)
            self.writeVint(0) # Unknown
            self.writeVint(0) # Coins to win
            self.writeVint(1) # Type (0 = normal event 1 = double coins 2 = double xp 3 = both)
            self.writeScID(15, 0) # Map
            self.writeVint(0) # Collected Coins
            self.writeVint(0) # Map Status (1 = New Event, 2 = First Win, 3 = Nothing)
            self.writeString("TID_WEEKEND_EVENT") # Text on Event (TID)
            self.writeBoolean(False) # "All experience collected" if True
        # Coming Soon Events Array Ends
        
        # Brawlers Upgrades Array
        self.writeVint(5)
        self.writeVint(1)
        self.writeVint(2)
        self.writeVint(3)
        self.writeVint(4)
        self.writeVint(5)
        # Brawlers Upgrades Array Ends
        
        # Milestones Array
        Milestones.MilestonesArray(self) 
        # Milestones Array Ends
        
        # Player IDs related to the menu
        self.writeVint(0)  # High ID
        self.writeVint(1)  # Low ID
        
        self.writeVint(0)  # High ID
        self.writeVint(1)  # Low ID
        
        self.writeVint(0)  # High ID
        self.writeVint(1)  # Low ID
        
        self.writeVint(0)  # High ID
        self.writeVint(1)  # Low ID
        
        # Name Array
        self.writeString("Player") # Player Name
        self.writeBoolean(True)  # Name set by user
        # Name Array Ends
        
        self.writeInt(0)  # Unknown
        self.writeVint(5)  # Unknown

        # Unlocked Brawlers and Upgrades Array 
        self.writeVint(64 + 3) # Count + Resources Array Count
        for x in range(64):
            self.writeScID(23, x) # Brawler ID
            self.writeVint(5)  # Power Level
        # Unlocked Brawlers and Upgrades Array End
            
        # Resources Array
        self.writeScID(5, 1) # Resource ID
        self.writeVint(self.config["gold"]) # Coins Amount

        self.writeScID(5, 5)  # Resource ID
        self.writeVint(self.config["chips"])  # Chips
        
        self.writeScID(5, 6)  # Resource ID
        self.writeVint(self.config["elixir"])  # Elixir
        # Resources Array End
        
        
        # Brawlers Trophies Array
        self.writeVint(64) # Count
        for x in range(64):
            self.writeScID(16, x)   # Brawler ID
            self.writeVint(500)  # Brawler Trophies
        # Brawlers Trophies Array End


        # Brawlers Trophies for Rank Array
        self.writeVint(64) # Count
        for x in range(64):
            self.writeScID(16, x) # Brawler ID
            self.writeVint(500) # Brawler Trophies for Rank
        # Brawlers Trophies for Rank Array End
        
        
        # Unknown Brawlers Array
        self.writeVint(16) # Count
        for x in range(16):
            self.writeScID(16, x) # Brawler ID
            self.writeVint(1)
        # Unknown Brawlers Array End
          
        # Unknown Brawlers Array
        self.writeVint(16) # Count
        for x in range(16):
            self.writeScID(16, x) # Brawler ID
            self.writeVint(2)
        # Unknown Brawlers Array End
        
        self.writeVint(self.config["gems"])  # Gems    
        self.writeVint(self.config["gems"])  # Free Gems
        
        self.writeVint(0)
        self.writeVint(0)
        
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        
        self.writeVint(2)  # Tutorial State
        self.writeVint(362687)  # Timestamp