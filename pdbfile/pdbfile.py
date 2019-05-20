import sys
import pprint

class PDBFile:
    """
    Deals with KEGG PDB files indexers.

    KEGG typically has PDB indexes for its proteins stored in ${organism_code}_pdb.list format.
    """

    def __init__(self, file_to_parse):
        # This class is all about filling that dictionary
        self.pdbs = {}
        self.file_to_parse = file_to_parse

    def all_pdbs(self):
        """
        Generate a dictionary containing all the PDB indexes for all the protein identifications for an specific file.

        Returns:

            (void): Fill the 'self.pdbs' variable with the data.
        """

        # Reset any previous PDB indexes.
        self.pdbs = {}

        with open(self.file_to_parse) as f:

            # Run through the PDB file.
            for line in f:

                # File has its data separated by tab char.
                record = line.split('\t')

                # First field is the protein identification
                protein_identification = record[0]

                # Remove the ${organism} code and its following ':' char from the protein identification.
                #protein_identification = protein_identification.replace( organism + ':', '' )

                # Remove any blank space.
                protein_identification = protein_identification.replace( ' ', '' )

                # Read the comments above.
                pdb_index = record[1]
                pdb_index = pdb_index.replace( 'pdb:', '' )
                pdb_index = pdb_index.replace( ' ', '' )

                # Remove any special 'new line' like char.
                protein_identification = protein_identification.rstrip('\r\n')
                pdb_index = pdb_index.rstrip('\r\n')

                # Initialize the dictionary.
                if not protein_identification in self.pdbs:
                    self.pdbs[ protein_identification ] = []

                # PDB file sometimes has duplicates. We're ignoring those to keep everything lean.
                if not pdb_index in self.pdbs[ protein_identification ]:
                    self.pdbs[ protein_identification ].append( pdb_index )

        return self.pdbs

