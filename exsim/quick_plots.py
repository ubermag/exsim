import matplotlib.pyplot as plt
import matplotlib
import ubermagutil.units as uu
from . import ltem


def ltem_phase(field, /, kx=0.1, ky=0.1):
    phase, _ = ltem.phase(field, kx=kx, ky=ky)
    phase.real.mpl_scalar(cmap='gray',
                          interpolation='spline16',
                          colorbar_label=r'$\phi$ (radians)')


def ltem_ft_phase(field, /, kx=0.1, ky=0.1):
    _, ft_phase = ltem.phase(field, kx=kx, ky=ky)
    fig, ax = plt.subplots()
    (ft_phase.conjugate * ft_phase).plane('z').real.mpl_scalar(
        ax=ax, cmap='gray', interpolation='spline16',
        colorbar_label=r'$\widetilde{\phi}$ (radians$^{-1}$)')
    multiplier = uu.si_max_multiplier(ft_phase.mesh.region.edges)
    ax.add_patch(matplotlib.patches.Ellipse(
        xy=(0, 0),
        width=ft_phase.mesh.cell[0] * kx * 2 / multiplier,
        height=ft_phase.mesh.cell[1] * ky * 2 / multiplier,
        edgecolor='red',
        facecolor='none',
        linewidth=3,
        label='Tikhonov filter'))
    ax.legend(frameon=True)


def ltem_defocus(field, /, kx=0.1, ky=0.1,
                 Cs=0, df_length=0.2e-3, U=None, wavelength=None):
    phase, _ = ltem.phase(field, kx=kx, ky=ky)
    defocus = ltem.defocus_image(phase, Cs=Cs, df_length=df_length,
                                 U=U, wavelenght=wavelength)
    defocus.mpl_scalar(cmap='gray', interpolation='spline16',
                       colorbar_label='Intensity (counts)')