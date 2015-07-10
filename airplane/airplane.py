#!/usr/bin/env python

from __future__ import print_function

import os, signal
import subprocess

import appdirs


class Airplane:
    def __init__(self):
        self.on = False

    def activate(self):
        self.on = True

        # Turn OFF WiFi
        self.wifi_contol(activate=False)

        # Turn OFF Bluetooth
        self.bluetooth_contol(activate=False)

        # Stop applications that rely on internet (cloud apps e.g. DropBox)

    def deactivate(self):
        #if self.status:
        #    print("Not currently running - no need to deactivate?")
        self.on = False

        # TODO: SHOULD RESTORE THE PREVIOUS SETTINGS (!) not turn on everything
        # Turn ON WiFi
        self.wifi_contol(activate=True)

        # Turn ON Bluetooth
        self.bluetooth_contol(activate=True)

    def shut_down(self):
        if self.on:
            print("Shutting down while in airplane mode ...")


    def wifi_contol(self, activate):
        out = subprocess.check_output(["networksetup -listallhardwareports"], shell=True)
        airport_interface = self.parse_networksetup(out)

        if activate:
            subprocess.call(["networksetup -setairportpower en0 on"], shell=True)
        else:
            subprocess.call(["networksetup -setairportpower en0 off"], shell=True)


    def bluetooth_contol(self, activate):
        #os.environ['PATH'] = ':'.join([os.getenv('PATH'), os.getenv('PYTHONPATH')])
        env_path = ':'.join([os.getenv('PATH'), '/usr/local/bin'])

        out = subprocess.Popen(["blueutil"], shell=True, env={"PATH": env_path})
        bluetooth_status = self.parse_blueutil(out)


        if activate:
            subprocess.Popen(["blueutil power 1"], shell=True, env={"PATH": env_path})
        else:
            subprocess.Popen(["blueutil power 0"], shell=True, env={"PATH": env_path})


    def parse_networksetup(self, output):
        #print(output)
        return 'en0'

    def parse_blueutil(self, output):
        #print(output)
        return '0'

