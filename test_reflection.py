import CFML_api
from CFML_api.API_Reflections_Utilities import ReflectionList
import numpy as np

cellv = np.asarray([5,5,8], dtype='float32')
angl = np.asarray([90,90,90], dtype='float32')

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
a=CFML_api.SpaceGroup(1)

reflection_list = ReflectionList(cell=cell, spg=a, lfriedel=True, job=job_info)
#reflection_list.compute_structure_factors(a, atom_list, job_info)
data_dict = reflection_list.compute_af0(a, atom_list, job_info)
#print(reflection_list.print_description())

# 辞書データからaf0の1次元配列を取得
af0_1d = data_dict['af0']  # 'data_dict' が辞書オブジェクト

# 1次元目と2次元目のサイズ
n_atoms = len(data_dict['atom'])
n_reflections = len(data_dict['h'])

# af0の2次元配列に復元
af0_2d = np.array(af0_1d).reshape(n_atoms, n_reflections)

print(af0_2d[4])
print(data_dict['h'])
