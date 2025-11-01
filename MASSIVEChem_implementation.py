import MASSiveChem.MASSiveChem as MC
from bokeh.plotting import show

mol_smi = 'CCCC'
apparatus_resolution = 0.01

show(MC.spectrum(mol_smi, False, apparatus_resolution))
