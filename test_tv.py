# import tv.py to this Python file
from tv import TV

# create an object name tv_1
tv_1 = TV()

# Asks if the user wants to turn on the tv
try:
    tv_status = input("Do you want to turn on the TV1? (y/n): ").lower()
    if tv_status == "y":
        tv_1.turn_on()
    else:
        tv_1.turn_off()
except ValueError:
    print("Sorry! wrong input")
    

if tv_1.status:    
# Asks if the user wants to set a channel
    try:
        channel = int(input("Enter the channel (1-120): "))
#    call the method to set a channel to this tv
        tv_1.set_channel(channel)
    except ValueError:
        print("Sorry! wrong input")
    except:
        print("Sorry, channel number is out of range")

# Asks if the user wants to set a volume
    try:
        volume = int(input("Enter the Volume level (1-7): "))
#    call the method to set a volume to this tv
        tv_1.set_volume(volume)
    except ValueError:
        print("Sorry! wrong input")
    except:
        print("Sorry, volume level is out of range")
        
# Asks if the user wants to increase the channel number by 1
    try:
        while True:
            if input("Do you want to increase the channel number? (y/n): ").lower() == "y":
#    call the method to increases the channel by 1
                tv_1.channel_up()
            else:
                break
    except ValueError:
        print("Sorry! wrong input")
        
# Asks if the user wants to decrease the channel number by 1
    try:
        while True:
            if input("Do you want to decrease the channel number? (y/n): ").lower() == "y":
#    call the method to decrease the channel by 1
                tv_1.channel_down()
            else:
                break
    except ValueError:
        print("Sorry! wrong input")
        
# Asks if the user wants to increase the volume level by 1
    try:
        while True:
            if input("Do you want to increase the volume level? (y/n): ").lower() == "y":
#    call the method to increases the volume level by 1
                tv_1.volume_up()
            else:
                break
    except ValueError:
        print("Sorry! wrong input")
        
# Asks if the user wants to decrease the volume level by 1 
    try:
        while True:
            if input("Do you want to decrease the volume level? (y/n): ").lower() == "y":
#    call the method to decrease the volume level by 1 
                tv_1.volume_down()
            else:
                break
    except ValueError:
        print("Sorry! wrong input")
        
# create an object name tv_2
tv_2 = TV()

# Asks if the user wants to turn on the tv
try:
    tv_status = input("Do you want to turn on the TV2? (y/n): ").lower()
    if tv_status == "y":
        tv_2.turn_on()
    else:
        tv_2.turn_off()
except ValueError:
    print("Sorry! wrong input")
        
if tv_2.status:    
# Asks if the user wants to set a channel
    try:
        channel = int(input("Enter the channel (1-120): "))
#    call the method to set a channel to this tv
        tv_2.set_channel(channel)
    except ValueError:
        print("Sorry! wrong input")
    except:
        print("Sorry, channel number is out of range")

# Asks if the user wants to set a volume
    try:
        volume = int(input("Enter the Volume level (1-7): "))
#    call the method to set a volume to this tv
        tv_2.set_volume(volume)
    except ValueError:
        print("Sorry! wrong input")
    except:
        print("Sorry, volume level is out of range")

# Asks if the user wants to increase the channel number by 1
    try:
        while True:
            if input("Do you want to increase the channel number? (y/n): ").lower() == "y":
#    call the method to increases the channel by 1
                tv_2.channel_up()
            else:
                break
    except ValueError:
        print("Sorry! wrong input")
        
# Asks if the user wants to decrease the channel number by 1
    try:
        while True:
            if input("Do you want to decrease the channel number? (y/n): ").lower() == "y":
#    call the method to decrease the channel by 1
                tv_2.channel_down()
            else: 
                break
    except ValueError:
        print("Sorry! wrong input")
        
# Asks if the user wants to increase the volume level by 1
    try:
        while True:
            if input("Do you want to increase the volume level? (y/n): ").lower() == "y":
#    call the method to increases the volume level by 1
                tv_2.volume_up()
            else:
                break
    except ValueError:
        print("Sorry! wrong input")
        
# Asks if the user wants to decrease the volume level by 1 
    try:
        while True:
            if input("Do you want to decrease the volume level? (y/n): ").lower() == "y":
#    call the method to decrease the volume level by 1 
                tv_2.volume_down()
            else:
                break
    except ValueError:
        print("Sorry! wrong input")
        
# Display the tv1 and tv2
def display_boxed_message(tv_1, tv_2):
    """Function to display the TV settings in a boxed format"""
    tv1_message = f"tv1's channel is {tv_1.get_channel()} volume level is {tv_1.get_volume()}"
    tv2_message = f"tv2's channel is {tv_2.get_channel()} volume level is {tv_2.get_volume()}"
    longest_message = max(len(tv1_message), len(tv2_message))
    box_width = longest_message + 4  # Padding for the box

    print("\n" + "*" * box_width)
    print(f"* {tv1_message}{' ' * (box_width - len(tv1_message) - 3)}*")
    print(f"* {tv2_message}{' ' * (box_width - len(tv2_message) - 3)}*")
    print("*" * box_width)

display_boxed_message(tv_1, tv_2)