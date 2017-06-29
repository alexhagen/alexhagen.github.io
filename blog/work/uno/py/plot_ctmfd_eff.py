import sys
import numpy as np
sys.path.append("/home/ahagen/code");
from pyg import twod as ahp
from pym import func as ahm
from pyg.colors import pu as colors

p = [3,4,5,7,10,11]
eta = 100.0*np.array([0.000636594,0.00546098,0.017974503,0.044561598,
	0.400733794,0.562310969]);
u_eta = [0.000318297,0.00119392,0.003396862,0.013368479,
	0.072016764,0.08676644];


eta_curve = ahm.curve(p,eta,u_y=u_eta,name='$\eta$');

figure = eta_curve.plot(linestyle='-');
figure.lines_off()
figure.markers_on()
figure.xlim(0,12)
figure.ylim(1E-2,100)
line = figure.add_hline(60.0, color=colors.brand_primary);
line.set_zorder(0);
figure.add_label(2,70.0,'$\eta=60\%$');
figure.add_label(2,30.0,'Theoretical Maximum for $40\,cm^{3}$');
figure.xlabel('Negative Pressure ($p_{neg}$) [$Pa \\times 10^{5}$]');
figure.ylabel('Intrinsic Efficiency '
	+'($\eta$) [$\%$]');
figure.ax.set_yscale('log');
figure.export('../img/ctmfd_eff',sizes=['cs'],
	formats=['pgf', 'pdf'],customsize=[4.25,2.125]);
figure.show()
