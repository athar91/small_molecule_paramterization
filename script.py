
import parmed as pmd
parm = pmd.load_file('ligand.parm7', 'ligand.rst7')
parm.save('ligand.itp',format='gromacs')
parm.save('ligand.gro')
