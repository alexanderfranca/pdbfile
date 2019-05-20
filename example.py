# -*- coding: utf-8 -*-

import pprint

from pdbfile.pdbfile import *

pdb = PDBFile(file_to_parse='./tests/fixtures/pdbs/hsa_pdb.list')

data = pdb.all_pdbs()

pprint.pprint(data['hsa:10009'])




