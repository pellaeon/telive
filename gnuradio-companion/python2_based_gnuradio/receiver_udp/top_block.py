#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: SQ5BPF Tetra live receiver 1ch simple UDP demo with fixed offset (gnuradio 3.7 version)
# Author: Jacek Lipkowski SQ5BPF
# Generated: Mon Sep  4 06:02:52 2023
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="SQ5BPF Tetra live receiver 1ch simple UDP demo with fixed offset (gnuradio 3.7 version)")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.xlate_offset_fine1 = xlate_offset_fine1 = 0
        self.samp_rate = samp_rate = 2000000
        self.freq = freq = 422729e3
        self.first_decim = first_decim = 32
        self.xlate_offset1 = xlate_offset1 = 500000
        self.variable_static_text_0 = variable_static_text_0 = "Please use M (mega) , k (kilo) sufixes where appropriate and press Enter after inputing text.\nPlease look at the gnuradio-companion console for possible errors (like PLL unlock etc)"
        self.udp_first_port = udp_first_port = 42001
        self.udp_dest_addr = udp_dest_addr = "127.0.0.1"
        self.sdr_ifgain = sdr_ifgain = 18
        self.sdr_gain = sdr_gain = 39
        self.ppm_corr = ppm_corr = -19
        self.out_sample_rate = out_sample_rate = 36000
        self.options_low_pass = options_low_pass = 12500
        self.if_samp_rate = if_samp_rate = samp_rate/first_decim
        self.frx1 = frx1 = freq+xlate_offset_fine1

        ##################################################
        # Blocks
        ##################################################
        _xlate_offset_fine1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._xlate_offset_fine1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_xlate_offset_fine1_sizer,
        	value=self.xlate_offset_fine1,
        	callback=self.set_xlate_offset_fine1,
        	label='Fine Tune',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._xlate_offset_fine1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_xlate_offset_fine1_sizer,
        	value=self.xlate_offset_fine1,
        	callback=self.set_xlate_offset_fine1,
        	minimum=-10000,
        	maximum=10000,
        	num_steps=200,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_xlate_offset_fine1_sizer, 3, 1, 1, 4)
        _sdr_ifgain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._sdr_ifgain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_sdr_ifgain_sizer,
        	value=self.sdr_ifgain,
        	callback=self.set_sdr_ifgain,
        	label='SDR IF Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._sdr_ifgain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_sdr_ifgain_sizer,
        	value=self.sdr_ifgain,
        	callback=self.set_sdr_ifgain,
        	minimum=0,
        	maximum=30,
        	num_steps=30,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_sdr_ifgain_sizer, 2, 3, 1, 1)
        _sdr_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._sdr_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_sdr_gain_sizer,
        	value=self.sdr_gain,
        	callback=self.set_sdr_gain,
        	label='SDR Input Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._sdr_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_sdr_gain_sizer,
        	value=self.sdr_gain,
        	callback=self.set_sdr_gain,
        	minimum=0,
        	maximum=42,
        	num_steps=42,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_sdr_gain_sizer, 2, 2, 1, 1)
        _ppm_corr_sizer = wx.BoxSizer(wx.VERTICAL)
        self._ppm_corr_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_ppm_corr_sizer,
        	value=self.ppm_corr,
        	callback=self.set_ppm_corr,
        	label='ppm',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._ppm_corr_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_ppm_corr_sizer,
        	value=self.ppm_corr,
        	callback=self.set_ppm_corr,
        	minimum=-100,
        	maximum=100,
        	num_steps=200,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_ppm_corr_sizer, 2, 1, 1, 1)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.freq,
        	callback=self.set_freq,
        	label='Frequency',
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._freq_text_box, 2, 0, 1, 1)
        self.wxgui_fftsink2_0_0_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=if_samp_rate,
        	fft_size=256,
        	fft_rate=32,
        	average=True,
        	avg_alpha=0.1,
        	title='Channel 1 FFT',
        	peak_hold=False,
        )
        self.GridAdd(self.wxgui_fftsink2_0_0_0.win, 0, 0, 1, 5)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=freq-xlate_offset1,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=True,
        	avg_alpha=0.1,
        	title='Full Spectrum\\n(click to tune)',
        	peak_hold=False,
        )
        self.GridAdd(self.wxgui_fftsink2_0.win, 1, 0, 1, 5)
        def wxgui_fftsink2_0_callback(x, y):
        	self.set_freq(x)

        self.wxgui_fftsink2_0.set_callback(wxgui_fftsink2_0_callback)
        self._variable_static_text_0_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.variable_static_text_0,
        	callback=self.set_variable_static_text_0,
        	label='Notice',
        	converter=forms.str_converter(),
        )
        self.GridAdd(self._variable_static_text_0_static_text, 4, 0, 2, 5)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq-xlate_offset1, 0)
        self.osmosdr_source_0.set_freq_corr(ppm_corr, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(sdr_gain, 0)
        self.osmosdr_source_0.set_if_gain(sdr_ifgain, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self._frx1_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.frx1,
        	callback=self.set_frx1,
        	label='Receive frequency',
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._frx1_static_text, 3, 0, 1, 1)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(first_decim, (firdes.low_pass(1, samp_rate, options_low_pass, options_low_pass*0.2)), xlate_offset1+xlate_offset_fine1, samp_rate)
        self.fractional_resampler_xx_0 = filter.fractional_resampler_cc(0, float(float(if_samp_rate)/float(out_sample_rate)))
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_gr_complex*1, udp_dest_addr, udp_first_port, 1472, False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.fractional_resampler_xx_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.fractional_resampler_xx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.wxgui_fftsink2_0_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.wxgui_fftsink2_0, 0))

    def get_xlate_offset_fine1(self):
        return self.xlate_offset_fine1

    def set_xlate_offset_fine1(self, xlate_offset_fine1):
        self.xlate_offset_fine1 = xlate_offset_fine1
        self._xlate_offset_fine1_slider.set_value(self.xlate_offset_fine1)
        self._xlate_offset_fine1_text_box.set_value(self.xlate_offset_fine1)
        self.set_frx1(self.freq+self.xlate_offset_fine1)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.xlate_offset1+self.xlate_offset_fine1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_if_samp_rate(self.samp_rate/self.first_decim)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1, self.samp_rate, self.options_low_pass, self.options_low_pass*0.2)))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_text_box.set_value(self.freq)
        self.wxgui_fftsink2_0.set_baseband_freq(self.freq-self.xlate_offset1)
        self.osmosdr_source_0.set_center_freq(self.freq-self.xlate_offset1, 0)
        self.set_frx1(self.freq+self.xlate_offset_fine1)

    def get_first_decim(self):
        return self.first_decim

    def set_first_decim(self, first_decim):
        self.first_decim = first_decim
        self.set_if_samp_rate(self.samp_rate/self.first_decim)

    def get_xlate_offset1(self):
        return self.xlate_offset1

    def set_xlate_offset1(self, xlate_offset1):
        self.xlate_offset1 = xlate_offset1
        self.wxgui_fftsink2_0.set_baseband_freq(self.freq-self.xlate_offset1)
        self.osmosdr_source_0.set_center_freq(self.freq-self.xlate_offset1, 0)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.xlate_offset1+self.xlate_offset_fine1)

    def get_variable_static_text_0(self):
        return self.variable_static_text_0

    def set_variable_static_text_0(self, variable_static_text_0):
        self.variable_static_text_0 = variable_static_text_0
        self._variable_static_text_0_static_text.set_value(self.variable_static_text_0)

    def get_udp_first_port(self):
        return self.udp_first_port

    def set_udp_first_port(self, udp_first_port):
        self.udp_first_port = udp_first_port

    def get_udp_dest_addr(self):
        return self.udp_dest_addr

    def set_udp_dest_addr(self, udp_dest_addr):
        self.udp_dest_addr = udp_dest_addr

    def get_sdr_ifgain(self):
        return self.sdr_ifgain

    def set_sdr_ifgain(self, sdr_ifgain):
        self.sdr_ifgain = sdr_ifgain
        self._sdr_ifgain_slider.set_value(self.sdr_ifgain)
        self._sdr_ifgain_text_box.set_value(self.sdr_ifgain)
        self.osmosdr_source_0.set_if_gain(self.sdr_ifgain, 0)

    def get_sdr_gain(self):
        return self.sdr_gain

    def set_sdr_gain(self, sdr_gain):
        self.sdr_gain = sdr_gain
        self._sdr_gain_slider.set_value(self.sdr_gain)
        self._sdr_gain_text_box.set_value(self.sdr_gain)
        self.osmosdr_source_0.set_gain(self.sdr_gain, 0)

    def get_ppm_corr(self):
        return self.ppm_corr

    def set_ppm_corr(self, ppm_corr):
        self.ppm_corr = ppm_corr
        self._ppm_corr_slider.set_value(self.ppm_corr)
        self._ppm_corr_text_box.set_value(self.ppm_corr)
        self.osmosdr_source_0.set_freq_corr(self.ppm_corr, 0)

    def get_out_sample_rate(self):
        return self.out_sample_rate

    def set_out_sample_rate(self, out_sample_rate):
        self.out_sample_rate = out_sample_rate
        self.fractional_resampler_xx_0.set_resamp_ratio(float(float(self.if_samp_rate)/float(self.out_sample_rate)))

    def get_options_low_pass(self):
        return self.options_low_pass

    def set_options_low_pass(self, options_low_pass):
        self.options_low_pass = options_low_pass
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1, self.samp_rate, self.options_low_pass, self.options_low_pass*0.2)))

    def get_if_samp_rate(self):
        return self.if_samp_rate

    def set_if_samp_rate(self, if_samp_rate):
        self.if_samp_rate = if_samp_rate
        self.wxgui_fftsink2_0_0_0.set_sample_rate(self.if_samp_rate)
        self.fractional_resampler_xx_0.set_resamp_ratio(float(float(self.if_samp_rate)/float(self.out_sample_rate)))

    def get_frx1(self):
        return self.frx1

    def set_frx1(self, frx1):
        self.frx1 = frx1
        self._frx1_static_text.set_value(self.frx1)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
