#!/bin/bash

# Small script to read powerstat load and dump into influxdb to visualize in grafana

VALUE=$(/usr/sbin/pwrstat -status | grep -oP "Load\.* \K([0-9]+)(?= Watt)")
echo $VALUE
curl -i -XPOST 'http://[redacted]:8086/write?db=[redacted-database]' --header 'Authorization: Token [user]:[pass]' --data-raw "load value=${VALUE}"
