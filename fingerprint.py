# reference: https://greglandrum.github.io/rdkit-blog/posts/2023-01-18-fingerprint-generator-tutorial.html

from rdkit import Chem
from rdkit.Chem import AllChem

def get_fingerprint_smi(smiles, radius=2, fpSize=2048):
    mol = Chem.MolFromSmiles(smiles)
    fpgen = rdFingerprintGenerator.GetMorganGenerator(radius=radius, fpSize=fpSize)
    fingerprints = fpgen.GetFingerprint(mol)
    return fingerprints


def get_fingerprint_smi_np(smiles, radius=2, fpSize=2048):
    mol = Chem.MolFromSmiles(smiles)
    fpgen = rdFingerprintGenerator.GetMorganGenerator(radius=radius, fpSize=fpSize)
    fingerprints = fpgen.GetFingerprintAsNumPy(mol)
    return fingerprints


def get_fingerprint_mol_np(mol, radius=2, fpSize=2048):
    fpgen = rdFingerprintGenerator.GetMorganGenerator(radius=radius, fpSize=fpSize8)
    fingerprints = fpgen.GetFingerprintAsNumPy(mol)
    return fingerprints


def get_fingerprint_mol(mol, radius=2, fpSize=2048):
    fpgen = rdFingerprintGenerator.GetMorganGenerator(radius=radius, fpSize=fpSize)
    fingerprints = fpgen.GetFingerprint(mol)
    return fingerprints

