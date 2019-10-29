clc
clear
syms x y z
ai = 884;
bi = 554;
ci = 713;
ri = 222;
aj = 120;
bj = 703;
cj = 771;
rj = 843;
ak = 938;
bk = 871;
ck = 583;
rk = 436;
al = 967;
bl = 653;
cl = 46;
rl = 529;
am = 593;
bm = 186;
cm = 989;
rm = 610;

eqn1 = 2*(aj-ai)*x+2*(bj-bi)*y+2*(cj-ci)*z == ri^2-rj^2-ai^2+aj^2-bi^2+bj^2-ci^2+cj^2;
eqn2 = 2*(ak-ai)*x+2*(bk-bi)*y+2*(ck-ci)*z == ri^2-rk^2-ai^2+ak^2-bi^2+bk^2-ci^2+ck^2;
eqn3 = 2*(al-ai)*x+2*(bl-bi)*y+2*(cl-ci)*z == ri^2-rl^2-ai^2+al^2-bi^2+bl^2-ci^2+cl^2;
% If we're using linear systems, really only need 3 equations for 3 unknowns
%eqn4 = 2*(am-ai)*x+2*(bm-bi)*y+2*(cm-ci)*z == ri^2-rm^2-ai^2+am^2-bi^2+bm^2-ci^2+cm^2;

sol = solve([eqn1,eqn2,eqn3],[x,y,z])

xSol = vpa(sol.x)
ySol = vpa(sol.y)
zSol = vpa(sol.z)