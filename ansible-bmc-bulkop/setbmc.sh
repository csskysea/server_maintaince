#!/bin/bash

ipmitool user set name 3 cogenda
ipmitool user set password 3 cogenda_2018
ipmitool channel  setaccess 2 3 callin=on ipmi=on link=on privilege=4
ipmitool lan print 2

