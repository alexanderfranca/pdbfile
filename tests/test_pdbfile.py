import sys
import pprint
import os
import unittest
from pdbfile.pdbfile import *
import re


class TestPDBFile( unittest.TestCase ):

    def setUp( self ):
        self.pdb = PDBFile(file_to_parse='./tests/fixtures/pdbs/hsa_pdb.list')

    def test_all_pdbs( self ):

        data = self.pdb.all_pdbs()

        self.assertEqual(len(data), 4769)

if __name__ == "__main__":
    unittest.main()
