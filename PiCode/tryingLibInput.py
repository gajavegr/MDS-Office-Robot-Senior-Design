import libinput

def read_key_events():
    # init libinput
    li = libinput.LibInput(udev=True)
    li.udev_assign_seat('seat0')
    
    # loop which reads events
    for event in li.get_event():
    
        # test the event.type to filter out only keyboard events 
        if event.type == libinput.constant.Event.KEYBOARD_KEY:
        
            # get the details of the keyboard event
            kbev = event.get_keyboard_event()
            kcode = kbev.get_key() # constants in  libinput.define.Key.KEY_xxx
            kstate = kbev.get_key_state() # constants   libinput.constant.KeyState.PRESSED or .RELEASED 
            
            # your key handling will look something like this...
            if kstate == libinput.constant.KeyState.PRESSED:
                print(f"Key {kcode} pressed") 
                
            elif kstate == libinput.constant.KeyState.RELEASED:
                
                if kbev.get_key() == libinput.define.Key.KEY_ENTER:
                    print("Enter key released")
                    
                elif kcode == libinput.define.Key.KEY_SPACE:
                    print("Space bar released")
                else:
                    print(f"Key {kcode} released")

read_key_events()