#!/usr/bin/python

cmdline = 'ifconfig eth0 | grep "inet addr" | cut -d: -f2 | cut -d" " -f1'
var = os.popen(cmdline).read()
print var