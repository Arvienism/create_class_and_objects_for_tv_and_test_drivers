# import tv.py to this Python file
from tv import TV

# create an object name tv_1
tv_1 = TV()

# Asks if the user wants to turn on the tv
tv_1.turn_on()
tv_status = input("Do you want to turn on the TV? (y/n): ").lower()
if tv_status != "y":
    tv_status = False
    tv_1.turn_off(tv_status)
else:
    tv_status = True
    tv_1.turn_on(tv_status)
    
# Asks if the user wants to set a channel
channel = int(input("Enter the channel (1-120): "))
#    call the method to set a channel to this tv
tv_1.set_channel(channel)

# Asks if the user wants to set a volume
volume = int(input("Enter the Volume level (1-7)"))
#    call the method to set a volume to this tv
tv_1.set_volume(volume)

# Asks if the user wants to increase the channel number by 1
increase_channel = input("Do you want to increase the channel number? (y/n)").lower()
#    call the method to increases the channel by 1
tv_1.channel_up(increase_channel)

# Asks if the user wants to decrease the channel number by 1
decrease_channel = input("Do you want to decrease the channel number? (y/n)").lower()
#    call the method to decrease the channel by 1
tv_1.channel_up(decrease_channel)

# Asks if the user wants to increase the volume level by 1
#    call the method to increases the volume level by 1

# Asks if the user wants to decrease the volume level by 1 
#    call the method to decrease the volume level by 1 

# create an object name tv_2
tv_2 = TV()

# Asks if the user wants to turn on the tv
tv_2.turn_on()
tv_status = input("Do you want to turn on the TV? (y/n): ").lower()
if tv_status != "y":
    tv_status = False
    tv_2.turn_off(tv_status)
else:
    tv_status = True
    tv_2.turn_on(tv_status)
    
# Asks if the user wants to set a channel
channel = int(input("Enter the channel (1-120): "))
#    call the method to set a channel to this tv
tv_2.set_channel(channel)

# Asks if the user wants to set a volume
volume = int(input("Enter the Volume level (1-7)"))
#    call the method to set a volume to this tv
tv_2.set_volume(volume)

# Asks if the user wants to increase the channel number by 1
increase_channel = input("Do you want to increase the channel number? (y/n)").lower()
#    call the method to increases the channel by 1
tv_2.channel_up(increase_channel)

# Asks if the user wants to decrease the channel number by 1
decrease_channel = input("Do you want to decrease the channel number? (y/n)").lower()
#    call the method to decrease the channel by 1
tv_2.channel_up(decrease_channel)

# Asks if the user wants to increase the volume level by 1
#    call the method to increases the volume level by 1

# Asks if the user wants to decrease the volume level by 1 
#    call the method to decrease the volume level by 1 