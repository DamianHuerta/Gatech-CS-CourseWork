function [qq,ww] = make_siren(fm,fd,fa,fs,tst,dur)
% fm: center/midle frequency
% fd: frequency deviation parameter
% fa: frequency of the sinusoidal phase function
% fs: sampling rate
% tst: starting time
% dur: duration of the synthesized signal

ww = tst:1/fs:(tst+dur);
the = 2*pi*(fm*ww+(fd/fa/2/pi)*sin(2*pi*fa*ww));
qq = cos(the);
