%zvect([1-j,j,3+4*j,exp(j*0.3*pi),exp(2j*pi/5))])
%% 2.1
% z1 = 5 * exp(-j*pi/4);
% z2= 3^.5 + j;
% zvect([z1,z2]);
% zprint([z1,z2]);
% hold on, zcoords, ucplot, hold off
% zconj = conj([z1,z2]);
% invconj =[1/z1,1/z2];
%zvect(zconj)
%zvect(invconj)
%zcat([3+j,-1+2j,1+2j]);
%% 2.1-d
% zsum = z1 + z2;
% zvect(zsum);
% hold on
% zcat([z1,z2]);
%% 2.1-e
% zvect(z1*z2);
% hold on
% zvect(z1/z2);
% zprint([z1*z2,z1/z2])
%% 2.1-f

% subplot(2,2,1), zvect([z1,z2,z1+z2]), hold on, zcoords, ucplot, hold off
% subplot(2,2,2), zvect([z2,conj(z2)]), hold on, zcoords, ucplot, hold off 
% subplot(2,2,3), zvect([z1,1/z1]), hold on, zcoords, ucplot, hold off 
% subplot(2,2,4), zvect([z1*z2]), hold on, zcoords, ucplot, hold off 
%% 2.3
% M = 100;
% for k=1:M
%     x(k) = k;
%     yy(k)= cos(0.02*pi*x(k)*x(k) );
% end
% plot(x(1:M),yy(1:M) )

% M = 100;
% yy = cos(0.02*pi*(1:M).*(1:M));
% plot(1:M, yy)
%% 2.5
% xx = 1/60:1/60:180/60;
% yy = sqrt(xx.*xx - 0.5) + 0.25;
% hi = exp(j*2*pi*yy);
% plot(xx, real(exp(j*2*pi*yy)), 'mo--', xx, imag(exp(j*2*pi*yy)),'go-')
%% 2.6
% [xx0,tt0] = onecos(4,2.5*exp(-j*pi/6),100,0.8,-0.15);
% plot(tt0,xx0);
% title("Plot of a Sinusoid")
% xlabel("Time (sec)")
%% 2.7.2
[xx1,tt1] = add_sines([6,3,18],[2*exp(j*pi/4),3-j,1.2],99,1.5,-0.2);
period = 1/3;
DC = (xx1(34)-xx1(1))/period
%% 2.7.3
% [xx2,tt2] = add_sines([40,64,80],[4*exp(j*0.2),2.2*exp(-j*(pi/2)),1.1],164,10,0)
% stem(tt2(657:739),xx2(657:739))
% title("Plot of a Sinusoid")
% xlabel("Time (sec)")
