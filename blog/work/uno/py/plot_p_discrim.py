import sys
import numpy as np
sys.path.append("/home/ahagen/code");
#from ahpy.data import ctmfd as ahi
from pyg import twod as ahp
from pym import func as ahm
from pyg.colors import pu as colors

E = np.linspace(0,20,num=1000);
phi = 0.64*np.multiply(np.exp(-E/1.175),np.sinh(np.sqrt(1.0401*E)));
a = 1;
b = 2.45;
c = 0.1;
phi_dd = a*np.exp(-np.multiply((E-b),(E-b))/(2.0*c*c))
dd_curve = ahm.curve(E,phi_dd)
a = dd_curve.integrate(0, 20)
phi_dd = a*np.exp(-np.multiply((E-b),(E-b))/(2.0*c*c))

fiss_curve = ahm.curve(E, phi, name='cf')

print "-- 2.45 MeV"
print fiss_curve.integrate(2.45, 20.)/fiss_curve.integrate(0., 20.)
print "-- 2.80 MeV"
print fiss_curve.integrate(2.80, 20.)/fiss_curve.integrate(0., 20.)
print "-- 3.00 MeV"
print fiss_curve.integrate(3.00, 20.)/fiss_curve.integrate(0., 20.)

del fiss_curve

fiss_curve = ahm.curve(E,phi,name='$^{252}Cf$');
dd_curve = ahm.curve(E,1.5*phi_dd,name='$DD$');

figure = fiss_curve.plot(linestyle='-', linecolor=colors.pu_colors['newgold']);
figure = dd_curve.plot(linestyle='-', linecolor=colors.pu_colors['gray'],
					   addto=figure);
figure.lines_on();
figure.markers_off();
figure.legend();
figure.xlim(0,15);
figure.fill_between(E[E>2.8],np.zeros(np.size(E[E>2.8])),
	phi[E>2.8],fc='#F8981D');
figure.fill_between(dd_curve.x,np.zeros_like(dd_curve.x),
	dd_curve.y,fc='#746C66');
figure.add_data_pointer(4.5,point=0.025,string='$27.4\%$ of Fission Signal',place=(6.5,0.15));
figure.xlabel('Energy ($E$) [$MeV$]');
figure.ylabel('Flux '
	+'($\\varphi \left( E \\right)$) [ ]');
figure.export('../img/p_discrim',sizes=['cs'],
	formats=['pdf', 'pgf'],customsize=[7.25, 2.125]);
figure.show()
