import CFML_api
from CFML_api.API_Reflections_Utilities import ReflectionList
import numpy as np

cellv = np.asarray([5,5,8], dtype='float32')
angl = np.asarray([90,90,80], dtype='float32')

cell = CFML_api.Cell(cellv, angl)

# Create list from string
print("========\nCreate atom_list from string")
dat = [
'loop_                     ',
'_atom_site_label          ',
'_atom_site_fract_x        ',
'_atom_site_fract_y        ',
'_atom_site_fract_z        ',
'_atom_site_U_iso_or_equiv ',
'Sr 0.00000 0.00000 0.25000 0.00608',
'Ti 0.50000 0.00000 0.00000 0.00507',
'O1 0.00000 0.50000 0.25000 0.01646',
'O2 0.75000 0.25000 0.00000 0.02026',
'N 0.70000 0.30000 0.00000 0.02026']
atom_list = CFML_api.AtomList(dat)

dat = [
'Title SrTiO3',
'Npatt 1',
'Patt_1 XRAY_2THE  1.54056    1.54056    1.00      0.0        135.0',
'UVWXY        0.025  -0.00020   0.01200   0.00150  0.00465',
'STEP         0.05 ',
'Backgd       50.000']

job_info = CFML_api.JobInfo(dat)
a=CFML_api.SpaceGroup(5)

reflection_list = ReflectionList(cell=cell, spg=a, lfriedel=True, job=job_info)
# reflection_list.compute_structure_factors(a, atom_list, job_info)
reflection_list.compute_af0(a, atom_list, job_info)
# print(reflection_list.print_description())
