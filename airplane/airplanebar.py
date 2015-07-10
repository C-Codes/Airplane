#!/usr/bin/env python

from __future__ import print_function

import os, sys
import time, datetime
import rumps
import webbrowser

from airplane import Airplane

icon_on = "airplane-mode-on.png"
icon_off = "airplane-mode-off.png"

airplane_active = False

class AirplaneStatusBarApp(rumps.App):
    def __init__(self):
        self.ap_handler = Airplane()
        super(AirplaneStatusBarApp, self).__init__(">", quit_button=None) #airplane

    @rumps.clicked("Airplane Mode")
    def airplane_mode(self, sender):
        global airplane_active
        airplane_active = not airplane_active
        sender.state = airplane_active

        if airplane_active:
            self.icon = icon_on
            self.ap_handler.activate()
        else:
            self.icon = icon_off
            self.ap_handler.deactivate()

        #status = "Airplane Mode OFF"
        #msg = "Airplane Mode is inactive"
        #time_st = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') #'%Y-%m-%d %H:%M:%S'
        #rumps.notification("Airplane "+str(time_st), "Status: "+str(status), str(msg))

    #@rumps.clicked("Status")
    #def status(self, _):
    #    '''
    #    Checking status of airplane mode
    #    '''
    #    status = "Airplane Mode OFF"
    #    msg = "Airplane Mode is inactive"
    #    time_st = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') #'%Y-%m-%d %H:%M:%S'
    #    rumps.notification("Airplane "+str(time_st), "Status: "+str(status), str(msg))

    @rumps.clicked('Quit')
    def clean_quit_application(self, _):
        self.ap_handler.shut_down()
        rumps.quit_application()


def main(argv):
    ap_bar = AirplaneStatusBarApp()

    if os.path.isfile(icon_off) and os.path.isfile(icon_on):
        ap_bar.icon=icon_off
        ap_bar.template = True

    ap_bar.run()


if __name__ == "__main__":
    main(sys.argv[1:])

