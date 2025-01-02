import network

def do_connect():
    wlan = network.WLAN(network.STA_IF) # create station interface
    wlan.active(True)       # activate the interface
    #print(wlan.scan())             # scan for access points
    #print(wlan.isconnected())
    # check if the station is connected to an AP
    wlan.connect('HUAWEI-0P1X28', 'Y1234567') # connect to an AP
    #wlan.config('mac')      # get the interface's MAC address
    print(wlan.ifconfig())         # get the interface's IP/netmask/gw/DNS addresses
    print("connect stat: ", wlan.isconnected())