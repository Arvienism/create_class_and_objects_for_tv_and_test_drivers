# import tv.py to this Python file
from tv import TV

# create an object name tv_1
tv_1 = TV()

# Asks if the user wants to turn on the tv
tv_status = input("Do you want to turn on the TV? (y/n): ").lower()
if tv_status == "y":
    tv_1.turn_on()
else:
    tv_1.turn_off()

if tv_1.status:    
# Asks if the user wants to set a channel
    channel = int(input("Enter the channel (1-120): "))
#    call the method to set a channel to this tv
    tv_1.set_channel(channel)

# Asks if the user wants to set a volume
    volume = int(input("Enter the Volume level (1-7)"))
#    call the method to set a volume to this tv
    tv_1.set_volume(volume)

# Asks if the user wants to increase the channel number by 1
    if input("Do you want to increase the channel number? (y/n)").lower() == "y":
#    call the method to increases the channel by 1
        tv_1.channel_up()

# Asks if the user wants to decrease the channel number by 1
    if input("Do you want to decrease the channel number? (y/n)").lower() == "y":
#    call the method to decrease the channel by 1
        tv_1.channel_down()

# Asks if the user wants to increase the volume level by 1
    if input("Do you want to increase the volume level? (y/n)").lower() == "y":
#    call the method to increases the volume level by 1
        tv_1.volume_up()

# Asks if the user wants to decrease the volume level by 1 
    if input("Do you want to decrease the volume level? (y/n)").lower() == "y":
#    call the method to decrease the volume level by 1 
        tv_1.volume_down()

# create an object name tv_2
tv_2 = TV()

# Asks if the user wants to turn on the tv
tv_status = input("Do you want to turn on the TV? (y/n): ").lower()
if tv_status == "y":
    tv_2.turn_on()
else:
    tv_2.turn_off()

if tv_2.status:    
# Asks if the user wants to set a channel
    channel = int(input("Enter the channel (1-120): "))
#    call the method to set a channel to this tv
    tv_2.set_channel()

# Asks if the user wants to set a volume
    volume = int(input("Enter the Volume level (1-7)"))
#    call the method to set a volume to this tv
    tv_2.set_volume()

# Asks if the user wants to increase the channel number by 1
    if input("Do you want to increase the channel number? (y/n)").lower() == "y":
#    call the method to increases the channel by 1
        tv_2.channel_up()

# Asks if the user wants to decrease the channel number by 1
    if input("Do you want to decrease the channel number? (y/n)").lower() == "y":
#    call the method to decrease the channel by 1
        tv_2.channel_down()

# Asks if the user wants to increase the volume level by 1
    if input("Do you want to increase the volume level? (y/n)").lower() == "y":
#    call the method to increases the volume level by 1
        tv_2.volume_up()

# Asks if the user wants to decrease the volume level by 1 
    if input("Do you want to decrease the volume level? (y/n)").lower() == "y":
#    call the method to decrease the volume level by 1 
        tv_2.volume_down()

# Display the tv1 and tv2
print(f"tv1's channel is {tv_1.get_channel} volume level is {tv_1.get_volume}" + '\n' +
      f"tv2's channel is {tv_2.get_channel} volume level is {tv_2.get_volume}")