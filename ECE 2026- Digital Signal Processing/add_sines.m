function [zz,tt] = add_sines(freqs,Camps,fs,dur,tstart)
    %ADD_SINES synthesize a signal sum of complex exponentials
    % usage:
    %[xx,tt] = add_sines(freqs,Camps,dur,tstart)
    % freqs = vector of frequencies (usually none are negative
    % Camps = vectoor of COMPLEX amplitudes
    % dur = total time duration of the signal
    % tstart = starting time
    % xx = vector of sinusoidal values
    % tt = vector of times, for the time axos
    %     
    % Note: freqs and Camps myst be the same length
    % Camps(1) corresponds to the frequency freqs(1),
    % Camps(2) corresponds to frequency freqs(2), etc.
    % The tt vector should be generated with a small time increment define by 
    % sampling rate, fs.
    %     
    % Make use of onecos

    if length(freqs) ~= length(Camps)
      error(123, "There is not the same number of frequencies as complex amplitudes");  
    end
    len = tstart:1/fs:tstart+dur;   
    func = zeros(1,length(len));
    
    for i = 1:length(freqs)
        [xx,yy] = onecos(freqs(i),Camps(i),fs,dur,tstart);
        func = func + xx;
    end
    zz = func;
    tt = tstart:1/fs:tstart+dur;
    plot(tt,zz)
    end