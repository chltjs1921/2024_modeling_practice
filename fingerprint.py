# reference: https://greglandrum.github.io/rdkit-blog/posts/2023-01-18-fingerprint-generator-tutorial.html

from rdkit import Chem
from rdkit.Chem import AllChem

def get_fingerprint_smi(smiles):
    mol = Chem.MolFromSmiles(smiles)
    fpgen = AllChem.GetRDKitFPGenerator()
    fingerprints = fpgen.GetFingerprint(mol)
    return fingerprints

def get_fingerprint_mol(mol):
    fpgen = AllChem.GetRDKitFPGenerator()
    fingerprints = fpgen.GetFingerprint(mol)
    return fingerprints
