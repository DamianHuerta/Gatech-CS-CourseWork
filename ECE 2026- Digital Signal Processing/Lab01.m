% % 3.3
% 
% [xx, fs]=audioread('ECE2026LAB01.wav');
% sec = length(xx)/fs;
% x = .2:1/fs:.42;
% xx = xx' 
% plot(x,xx(1601:3361),'r--');
% 
% % 3.4.1
% xh = xx * 0.5;
% le = length(xh);
% xhr= xh(end:-1:1);
% audiowrite('ECE2026lab01out.wav',xhr,fs);
% 
% % 3.4.2
% xhr2 = xhr
% xhr2(1:2:end) = xhr2(1:2:end) * -1;
% audiowrite('ECE2026lab01outb.wav',xhr2,fs);
% so = audioplayer(xhr2,fs)
% play(so)

% 3.5
audioobject = audiorecorder(8000,16,1);
recordblocking(audioobject,5);
myvoice = audioplayer(audioobject,8000);
play(audioobject)
hello = getaudiodata(audioobject)
plot(hello)
audiowrite('MyvoiceLab01.wav',hello,8000)