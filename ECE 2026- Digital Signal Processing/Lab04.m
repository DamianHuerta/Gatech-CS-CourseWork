%% 2.3.1 MATLAB Syntehsis of Chirp Signals
%     fsamp = 10000;
%     dur = 4;
%     tt = 0: 1/fsamp:dur;
%     f1 = 400;
%     mu = 1000;
%     psi = 2*pi*(0.1+f1*tt + mu*tt.*tt);
%     xx = real(10*exp(j*psi));
%     soundsc(xx,fsamp)
%     
%% 3.1.1
%% 3.1.2
[xx,fs] = audioread("Lab4voice.wav")
xx = xx'
sec = length(xx)/fs;
fc1 = 25;
fc2 = 400;
fc3 = 1000;
[c1,~] = onecos(fc1,1,fs,sec,0);
[c2,~] = onecos(fc2,1,fs,sec,0);
[c3,~] = onecos(fc3,1,fs,sec,0);
c1 = xx.*c1(1:end-1);
c2 = xx.*c2(1:end-1);
c3 = xx.*c3(1:end-1);
audiowrite('Lab4out1.wav',c1,fs);
audiowrite('Lab4out2.wav',c2,fs);
audiowrite('Lab4out3.wav',c3,fs);
% soundsc(c1,fs)
% soundsc(c2,fs)
% soundsc(c3,fs)

%% 3.2
fs = 10000;
[chirp] = make_chirp(2200,500,1,fs);
soundsc(chirp,fs)

%% 3.3
spectrogram(chirp,512,384,1024,10000,'yaxis')
fres = 10;
FF = -fs/2:fres:fs/2;
spectrogram(chirp,512,384,FF,fs,'yaxis')




