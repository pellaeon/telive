# telive - Tetra Live Monitor
(c) 2014-2015 Jacek Lipkowski <sq5bpf@lipkowski.org>

telive is a program which can be used to display information like
signalling, calls etc from a Tetra network. It is also possible to
log the signalling information, listen to the audio in realtime and
to record the audio. Playing the audio and recompressing it into ogg
is done via external scripts.

Please read telive_doc.pdf, either in this directory or here:
https://github.com/sq5bpf/telive/raw/master/telive_doc.pdf

## `rxx` Quick Guide

Keys:

- ? - show help in the status window
- m - toggle mutessi
- M - toggle mute
- r - refresh screen
- R - toggle record
- a - toggle alldump
- l - toggle logging
- s - stop play (if there are multiple channels active, this will end the active playback and search for
- another channel to play).
- V/v – increase/decrease verbosity
- f – toggle SSI filter disabled/enabled/inverted (inverted passes traffic not matching the filter)
- F – enter SSI filter expression
- t – toggle between the usage identifier window, and the frequency window
- z – forget all information learned by telive, read the receiver parameters again

# Docker (under Wayland host, latest)

Build Docker image:

```
docker build -t telive .
```

## Start with Audio

You will need [x11docker](https://github.com/mviereck/x11docker). You might also need to `chmod 777` your RTL-SDR usb dev file under `/dev/bus/usb`.

Run:

```
x11docker --share /dev/bus/usb --user=RETAIN -I --pulseaudio=tcp telive
```

Note:
* [x11docker pulseaudio issue](https://github.com/mviereck/x11docker/issues/527)

Debug:

```
x11docker --share /dev/bus/usb --user=RETAIN -I --pulseaudio=tcp telive qterminal
```

# Docker (under X11 host, untested, old)

To build and run docker container:

```
cd docker
./run.sh
```

## Audio

Enable PulseAudio to receive connections on host (this also works if you're using Pipewire):

```
pactl load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1/16
```

Then start `rxx` normally, it should connect to the host's PulseAudio server. You should see connection like this:

```
ESTAB    0    0   127.0.1.1:4713   127.0.0.1:34386
```

## Transcode recording

Inside the container, execute:

```
/tetra/bin/tetrad
```

OGG output will be stored in `/tetra/out`, copy with:

```
docker cp <CONTAINERID>:/tetra/out .
```

## Edit .grc (gnuradio-companion) files

Run:
```
cd ~/projects/telive
docker run -e  DISPLAY=$DISPLAY --privileged -v /tmp/.X11-unix:/tmp/.X11-unix -v $PWD:/mnt -u $USER -it telive /bin/bash
```

Inside the container shell, run `gnuradio-companion /mnt/receiver_udp/XXX` to edit.

Note: these grc files don't open correctly in newer gnuradio-companion versions.

# Disclaimer

The program is licenced under GPL v3 (license text is also included in the 
file LICENSE). I may not be held responsible for anything associated with 
the use of this tool.


This was a quick hack written in my spare time, and for my own pleasure,
and because of this the code is really ugly. The code is also based on wrong 
assumptions - using the usage identifier as the key is not a good way of 
following calls (but it works most of the time). Maybe one day this will
be rewritten to look better (or not).

-----------------------------------

## Fork

This fork by @pellaeon combines @sq5bpf's and @mehdilauters's docker pull request and updates it.
