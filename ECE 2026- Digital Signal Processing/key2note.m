function xx = key2note(X, keynum, dur, fsamp)
%KEY2NOTE produce a sinusoidal waveform correspondiing to a 
% given piano key number
% 
% usage: xx = key2note (X, keynum, dur)
% xx = the output sinusoidal waveform
% X = the output sinusoidal waveform
% keynum = the piano keyboard number of the desired note
% dur = the duration (in seconds) of the output note 
% fs = sampling frequency, use 11025 or 22050 Hz

tt = 0:1/fsamp:dur;
freq = 440 * 2^((keynum-49)/12);
xx = real(X*exp(j*2*pi*freq*tt));
end
