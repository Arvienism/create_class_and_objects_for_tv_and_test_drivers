# import tv.py to this Python file
from tv import TV

# create an object name tv_1
tv_1 = TV()

# Asks if the user wants to turn on the tv
while True:
    tv_status = input("Do you want to turn on the TV1? (y/n): ").lower()
    if tv_status == "y":
        tv_1.turn_on()
        break
    elif tv_status == "n":
        tv_1.turn_off()
        break
    else:
        print("Sorry! wrong input, please enter 'y' or 'n'")

if tv_1.status:    
# Asks if the user wants to set a channel
    while True:
        try:
            channel = int(input("Enter the channel (1-120): "))
            if channel >= 121:
                print("Sorry, channel number is out of range")
            elif channel <= 0:
                print("Sorry, channel number is out of range")
#    call the method to set a channel to this tv
            else:
                tv_1.set_channel(channel)
                break
        except ValueError:
            print("Sorry! wrong input")


# Asks if the user wants to set a volume
    while True:
        try:
            volume = int(input("Enter the volume level (1-7): "))
            if volume >= 8:
                print("Sorry, volume level is out of range")
            elif volume <= 0:
                print("Sorry, volume level is out of range")
#    call the method to set a volume to this tv
            else:
                tv_1.set_volume(volume)
                break
        except ValueError:
            print("Sorry! wrong input")
        
# Asks if the user wants to increase the channel number by 1
    while True:
        increase_channel = input("Do you want to increase the channel number? (y/n): ").lower()
#    call the method to increases the channel by 1
        if increase_channel == "y":
            tv_1.channel_up()
        elif increase_channel == "n":
            break
        else:
            print("Sorry! wrong input, please enter 'y' or 'n'")
            break
        
# Asks if the user wants to decrease the channel number by 1
    while True:
        decrease_channel = input("Do you want to decrease the channel number? (y/n): ").lower()
#    call the method to decrease the channel by 1
        if decrease_channel == "y":
            tv_1.channel_down()
        elif decrease_channel == "n":
            break
        else:
            print("Sorry! wrong input, please enter 'y' or 'n'")
            break
        
# Asks if the user wants to increase the volume level by 1
    while True:
        increase_volume = input("Do you want to increase the volume level? (y/n): ").lower()
#    call the method to increases the volume level by 1
        if increase_volume == "y":
            tv_1.volume_up()
        elif increase_volume == "n":
            break
        else:
            print("Sorry! wrong input, please enter 'y' or 'n'")
            break
        
# Asks if the user wants to decrease the volume level by 1 
    while True:
        decrease_volume = input("Do you want to decrease the volume level? (y/n): ").lower()
#    call the method to decrease the volume level by 1 
        if decrease_volume == "y":
            tv_1.volume_down()
        elif decrease_volume == "n":
            break
        else:
            print("Sorry! wrong input, please enter 'y' or 'n'")
            break
        
# create an object name tv_2
tv_2 = TV()

# Asks if the user wants to turn on the tv
while True:
    tv_status = input("Do you want to turn on the TV2? (y/n): ").lower()
    if tv_status == "y":
        tv_2.turn_on()
        break
    elif tv_status == "n":
        tv_2.turn_off()
        break
    else:
        print("Sorry! wrong input, please enter 'y' or 'n'")
        
if tv_2.status:    
# Asks if the user wants to set a channel
    while True:
        try:
            channel = int(input("Enter the channel (1-120): "))
            if channel >= 121:
                print("Sorry, channel number is out of range")
            elif channel <= 0:
                print("Sorry, channel number is out of range")
#    call the method to set a channel to this tv
            else:
                tv_2.set_channel(channel)
                break
        except ValueError:
            print("Sorry! wrong input")

# Asks if the user wants to set a volume
    while True:
        try:
            volume = int(input("Enter the volume level (1-7): "))
            if volume >= 8:
                print("Sorry, volume level is out of range")
            elif volume <= 0:
                print("Sorry, volume level is out of range")
#    call the method to set a volume to this tv
            else:
                tv_2.set_volume(volume)
                break
        except ValueError:
            print("Sorry! wrong input")

# Asks if the user wants to increase the channel number by 1
    while True:
        increase_channel = input("Do you want to increase the channel number? (y/n): ").lower()
#    call the method to increases the channel by 1
        if increase_channel == "y":
            tv_2.channel_up()
        elif increase_channel == "n":
            break
        else:
            print("Sorry! wrong input, please enter 'y' or 'n'")
            break
        
# Asks if the user wants to decrease the channel number by 1
    while True:
        decrease_channel = input("Do you want to decrease the channel number? (y/n): ").lower()
#    call the method to decrease the channel by 1
        if decrease_channel == "y":
            tv_2.channel_down()
        elif decrease_channel == "n":
            break
        else:
            print("Sorry! wrong input, please enter 'y' or 'n'")
            break
        
# Asks if the user wants to increase the volume level by 1
    while True:
        increase_volume = input("Do you want to increase the volume level? (y/n): ").lower()
#    call the method to increases the volume level by 1
        if increase_volume == "y":
            tv_2.volume_up()
        elif increase_volume == "n":
            break
        else:
            print("Sorry! wrong input, please enter 'y' or 'n'")
            break
        
# Asks if the user wants to decrease the volume level by 1 
    while True:
        decrease_volume = input("Do you want to decrease the volume level? (y/n): ").lower()
#    call the method to decrease the volume level by 1 
        if decrease_volume == "y":
            tv_2.volume_down()
        elif decrease_volume == "n":
            break
        else:
            print("Sorry! wrong input, please enter 'y' or 'n'")
            break
        
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