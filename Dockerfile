from ubuntu:18.04
RUN for i in ppa:bladerf/bladerf \
		ppa:ettusresearch/uhd \
		ppa:myriadrf/drivers \
		ppa:myriadrf/gnuradio \
		ppa:gqrx/gqrx-sdr; \
		do \
		add-apt-repository -y $i || break; \
		done
RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y \
	git make libtool libncurses5-dev build-essential autoconf \
	automake vorbis-tools sox alsa-utils unzip xterm libxml2-dev socat \
	wget sudo vim nano gnuradio gnuradio-dev gr-osmosdr gr-iqbal gqrx-sdr python-numpy

# for debugging
RUN DEBIAN_FRONTEND=noninteractive apt install -y tmux qterminal vlc libsox-fmt-mp3

#COPY docker/files/* /tmp/
#RUN /tmp/adduser.sh

RUN echo "%sudo ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/nopwd
RUN echo 'export PATH="/tetra/bin:/app/bin:$PATH"' >> /etc/environment

WORKDIR /app
COPY --chown=user1:user1 . /app

RUN adduser user1 && adduser user1 sudo
USER user1
RUN cd /app && sudo make && sudo ./install.sh
RUN /app/scripts/install_telive.sh

RUN sudo sed -i 's|x-terminal-emulator|/usr/bin/xterm|' /etc/gnuradio/conf.d/grc.conf

CMD ["/app/main.sh"]
