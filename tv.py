# create a class name tv
class TV:
#   create a constructor and the parameters
    def __init__(self, status, channel=0, volume=0) -> None:
        self.status = True
        self.channel = channel
        self.volume = volume
#   create a method to turn "on" the tv
    def turn_on(self):
        self.status = True
        print(self.status + "The TV is on")
#   create a method to turn "off" the tv
    def turn_off(self):
        self.status = False
        print(self.status + "The TV is off")
#   create a method to return the channel to this tv
    def get_channel(self):
        return self.channel
#   create a method to set a channel to this tv
    def set_channel(self):
        if 1 <= self.channel <= 120 and self.status:
            self.channel
#   create a method to getting the volume to this tv
#   create a method to set a volume to this tv 
#   create a method to increase the channel number by 1
    def channel_up(self):
        if self.channel < 120 and self.status:
            self.channel += 1
#   create a method to decrease the channnel number by 1
    def channel_down(self):
        if self.channel > 1 and self.status:
            self.channel -= 1
#   create a method to increase the volume level by 1
#   create a method to decrease the volume level by 1