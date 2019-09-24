function [cc,pp] = make_chirp(f1,f2,dur,fs)
%Make_chrip generate a linear-FM chirp signal
% 
% usage: cc = make_chirp(f1,f2,dur,fsamp)
% 
% f1 = starting freq
% f2 - ending freq
% dur = total time duration
% fsamp = sampling frequency
% this template code does not considere the initial phase, phi
% cc = (vector of) samples of the chirp signal
% pp = vector of the time instants for t = 0 to t=dur
% 
mu = (f2-f1)/(2*dur);
if (nargin < 4)
    fs = 10000;
end
tt = 0:1/fs:dur;
psi = 2*pi*(f1*tt+mu*tt.*tt);
cc = real(exp(j*psi));