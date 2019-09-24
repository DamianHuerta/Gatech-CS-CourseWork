%% 2.2
% [x1,~] = onecos(800,100*exp(-j*pi/4),11025,.5,0);
% soundsc(x1);
% [x2,~] = onecos(1200,80*exp(j*pi/4),11025,.8,0);
% soundsc(x2);
% xx = [ x1, zeros(1,1103), x2]
% soundsc(xx)
% tt= (1/11025)*(1:length(xx));
% plot(tt,xx);
% soundsc(xx,22050)
%% 2.3
% x.Amp = 7;
% x.phase = -pi/2;
% x.freq = 100;
% x.fs = 11025;
% x.timeInterval = 0:(1/x.fs):0.05;
% x.values = x.Amp*cos(2*pi*(x.freq)*(x.timeInterval) + x.phase);
% x.name = 'My Signal';
% x %---------- echo the contents of the structure "x"
% plot(x.timeInterval, x.values)
% title(x.name)
%% 2.5 Piano Keyboard
%% 2.6
% plotspec(xx,22050);
% spectrogram(xx,512,384,512,22050,'yaxis')
% xx2 = xx + j*1e-14
% plotspec(xx2,22050)

% fs = 10000;
% xx3 = cos(2000*pi*(0:1/fs:0.5));
% spectrogram(xx3,512,384,512,fs,'yaxis');
% colorbar
% 
% xx4 = cos(2000*pi*(0:1/fs:0.5));
% plotspec(xx4+j*1e-9,fs,1024);
% colorbar

%% 3.1
dbstop if error
[xn,tn] = coscos(2,3,20,1);

%% 3.2
note = key2note(400*exp(j*pi/2),47,2,22050);
soundsc(note,22050)
%% 3.3 Synthesize a scale of octaves
scale.keys = [40,42,44,45,47,49,51,52,40,44,47,44,40];
% ---- NOTES: C D E F G A B C C E G E C
% key #40 is middle-C

scale.durations = 0.25 * ones(1,length(scale.keys));
fs = 22050;
xx = zeros(1,ceil(sum(scale.durations)*fs+length(scale.keys)) );
n1 = 1;
for kk = 1:length(scale.keys)
    keynum = scale.keys(kk);
    tone = key2note(4*exp(j*pi/2),keynum,scale.durations(kk),fs) + key2note(4*exp(j*pi/2),keynum+12,scale.durations(kk),fs);
    n2 = n1 + length(tone) - 1;
    xx(n1:n2) = xx(n1:n2) + tone;
    n1 = n2 + 1;
end
soundsc(xx,fs)

%% 3.4 Spectograms
spectrogram(xx,512,384,512,fs,'yaxis')
