function [yy,tt] = onecos(freq,camp,fs,dur,tstart)
tt = tstart:1/fs:tstart + dur;
hi = exp(2i*pi*freq*tt);
yy = real(camp * hi);
end