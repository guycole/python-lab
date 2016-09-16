#! /usr/bin/python
#
# Title:usbdemo1.py
# Description:
# Development Environment:OS X 10.10.5/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import usb.core
import usb.util

class UsbDemo:


    def execute(self):
        device = usb.core.find(idVendor=0x05c6, idProduct=0x6765)
        if device is None:
            raise ValueError('device not found')
        else:
            print 'device noted'

        reattach = False
        if device.is_kernel_driver_active(0):
            print 'active driver'
            reattach = True
            device.detach_kernel_driver(0)

        endpoint_in = device[0][(0,0)][0]
        endpoint_out = device[0][(0,0)][1]

        endpoint_out.write('RYRYRYR')

print 'start usbdemo1'

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    driver = UsbDemo()
    driver.execute()

print 'stop usbdemo1'
