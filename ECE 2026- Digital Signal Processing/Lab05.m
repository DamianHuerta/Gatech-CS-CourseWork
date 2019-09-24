%% 2.2
fs = 8000;
fm = 1000;
fd = 40;
fa = 3;
tt = 0:1/fs:3;
the = 2*pi*(fm*tt+(fd/fa/2/pi)*sin(2*pi*fa*tt));
xx = cos(the);
soundsc(xx);
%% 2.3
spectrogram(xx,512,384,512,fs,'yaxis');
%% 3.1
[hi, kk]= make_chirp(0,1000,4,11000,22000);
soundsc(hi,22000);
spectrogram(hi,256,200,512,22000,'yaxis')
[bye, ii]= make_chirp(0,1000,4,11000,8000);
spectrogram(bye,256,200,512,8000,'yaxis')
%% 3.2 
[zz ~] = make_siren(2000,377,4,8000,0,4);
soundsc(zz,8000);
spectrogram(zz,256,200,512,8000,'yaxis');
[oo ~] = make_siren(2000,377,4,4000,0,4);
soundsc(oo,4000)
%spectrogram(oo,256,200,512,4000,'yaxis');
%% 3.3
T = 20;
fs = 1;
Amp = 9;
tStop = 600;
tt = 0:1/fs:tStop;
qq = rem(tt,T);
xx = Amp*(abs(qq-(0.5*T))-.25*T);
plot(tt(1:3*T),xx(1:3*T));
axis tight;
spectrogram(xx,128,100,512,fs,'yaxis');
