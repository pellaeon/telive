#!/usr/bin/env bash

gnuradio-companion /app/gnuradio-companion/python2_based_gnuradio/receiver_udp/telive_1ch_simple_gr37_udp.grc &
xterm -hold -e "cd ~/tetra/osmo-tetra-sq5bpf/src/ && ./receiver1udp 1" &
xterm -hold -geom 203x60 -e 'export PATH="/tetra/bin:/app/bin:$PATH" && cd /app && ./rxx' &
/bin/bash
