from Packets.Messages.Client.Login import Login
from Packets.Messages.Client.KeepAlive import KeepAlive
from Packets.Messages.Client.GoHome import GoHome

Packets = {

    10101: Login,
    10108: KeepAlive,
    14109: GoHome
}
