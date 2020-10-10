import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

lmin_wv, lmax_wv =10**-12, 10**3
lmin_nu, lmax_nu = 10**5.4, 10**20.5
lmin_eV, lmax_eV = 10**-9, 10**6 

def setup(ax):
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.tick_params(which='major', length=5)
    ax.tick_params(which='minor', width=0.75)
    ax.tick_params(which='minor', length=2.5)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1.1)
    ax.patch.set_alpha(0.0)

    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00)
x = [10^-2,10^-3,10^-4,10^-5,10^-6]
plt.figure(figsize=(8, 5.5))
plt.plot(x,x)

#Wavelength
ax = plt.subplot(8, 1, 2)
setup(ax)
ax.set_xlim(lmax_wv, lmin_wv)
ax.set_xscale('log')
ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=20))
ax.text(0.0, 0.1, "Wavelength (m)",
        fontsize=20, transform=ax.transAxes)

#the arrows
bbox_props = dict(boxstyle="rarrow,pad=0.4", fc="m", ec="b", lw=2)
t = ax.text(10**-11.5, 1.2, "γ Rays", ha="center", va="center", rotation=0,size=10,bbox=bbox_props)

bbox_props = dict(boxstyle="rarrow,pad=0.4", fc="m", ec="b", lw=2)
t = ax.text(10**-10.8, 0.7, "    Hard X-Rays  ", ha="center", va="center", rotation=0,size=10,bbox=bbox_props)

bbox_props = dict(boxstyle="square,pad=0.4", fc="m", ec="b", lw=2)
t = ax.text(10**-8.7, 1.2, "   Soft X-Rays  ", ha="center", va="center", rotation=0,size=10,bbox=bbox_props)

bbox_props = dict(boxstyle="square,pad=0.4", fc="m", ec="b", lw=2)
t = ax.text(10**-7.3, 0.7, "Ultraviolet", ha="center", va="center", rotation=0,size=10,bbox=bbox_props)

bbox_props = dict(boxstyle="square,pad=0.4", fc="goldenrod", ec="b", lw=2)
t = ax.text(10**-4.72, 0.7, "        Infrared        ", ha="center", va="center", rotation=0,size=10,bbox=bbox_props)

bbox_props = dict(boxstyle="square,pad=0.4", fc="goldenrod", ec="b", lw=2)
t = ax.text(10**-3.2, 1.2, "            Microwaves           ", ha="center", va="center", rotation=0,size=10,bbox=bbox_props)

bbox_props = dict(boxstyle="larrow,pad=0.4", fc="goldenrod", ec="b", lw=2)
t = ax.text(10, 0.7, "           Radio Waves            ", ha="center", va="center", rotation=0,size=10,bbox=bbox_props)

bbox_props = dict(boxstyle="square,pad=0.4", fc="None", ec="b", lw=0)
t = ax.text(10**-6.3, 1.07, "Visible", ha="center", va="center", rotation=0, size=10,bbox=bbox_props)

bbox_props = dict(boxstyle="square,pad=0.4", fc="None", ec="b", lw=0)
t = ax.text(10**-4.7, 2, "Electromagnetic Spectrum", ha="center", va="center", rotation=0, size=20, bbox=bbox_props)
ylim = .5
ymax = 0.9
plt.axvline(x=7.5*10**(-7.05), ymin= ylim, ymax=ymax, color='red', linestyle='-')
plt.axvline(x=7.05*10**(-7.05), ymin = ylim, ymax=ymax, color='orange', linestyle='-')
plt.axvline(x=6.6*10**(-7.05), ymin = ylim,  ymax=ymax, color='yellow', linestyle='-')
plt.axvline(x=6.15*10**(-7.05), ymin = ylim, ymax=ymax, color='green', linestyle='-')
plt.axvline(x=5.7*10**(-7.05), ymin = ylim, ymax=ymax, color='blue', linestyle='-')
plt.axvline(x=5.25*10**(-7.05), ymin = ylim, ymax=ymax, color='indigo', linestyle='-')
plt.axvline(x=4.8*10**(-7.05), ymin = ylim, ymax=ymax, color='violet', linestyle='-')

ax = plt.subplot(8, 1, 3)
setup(ax)
ax.set_xlim(lmin_nu, lmax_nu)
ax.set_xscale('log')
ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=20))
ax.text(0.0, 0.1, "Frequency (Hz)",
        fontsize=20, transform=ax.transAxes)

bbox_props = dict(boxstyle="square,pad=0.3", fc="grey", ec="black", lw=1)

t = ax.text(10**5.5, 0.9, "1km", ha="center", va="center", rotation=0,size=10,bbox=bbox_props)
t = ax.text(10**8.5, 0.9, "1m", ha="center", va="center", rotation=0,size=10, bbox=bbox_props)
t = ax.text(10**11.5, 0.9, "1mm", ha="center", va="center", rotation=0,size=10,bbox=bbox_props)
t = ax.text(10**14.5, 0.9, "1μm", ha="center", va="center", rotation=0,size=10,bbox=bbox_props)
t = ax.text(10**17.6, 0.9, "1nm", ha="center", va="center", rotation=0,size=10,bbox=bbox_props)
t = ax.text(10**18.5, 0.9, " 1Å ", ha="center", va="center", rotation=0,size=10,bbox=bbox_props)
t = ax.text(10**20.5, 0.95, "1pm", ha="center", va="center", rotation=0,size=10,bbox=bbox_props)

ax = plt.subplot(8, 1, 4)
setup(ax)
ax.set_xlim(lmin_eV, lmax_eV)
ax.set_xscale('log')
ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=20))
ax.text(0.0, 0.1, "Energy (eV)",
        fontsize=20, transform=ax.transAxes)
bbox_props = dict(boxstyle="square,pad=0.3", fc="grey", ec="red", lw=1)
t = ax.text(10**-8.5, 0.85, "1MHz", ha="center", va="center", rotation=0,size=9, bbox=bbox_props)

bbox_props = dict(boxstyle="square,pad=0.3", fc="grey", ec="red", lw=1)
t = ax.text(10**-5.5, 0.85, "1GHz", ha="center", va="center", rotation=0,size=10,bbox=bbox_props)


bbox_props = dict(boxstyle="square,pad=0.3", fc="grey", ec="black", lw=1)
t = ax.text(10**2, -0.4, "1keV", ha="center", va="center", rotation=0,size=10,bbox=bbox_props)

bbox_props = dict(boxstyle="square,pad=0.3", fc="grey", ec="black", lw=1)
t = ax.text(10**6, -0.4, "1MeV", ha="center", va="center", rotation=0,size=10,bbox=bbox_props)
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=1.05)
x = [1,2,3]
plt.savefig('Plot2-Astr414.png', dpi = 300)

plt.show()