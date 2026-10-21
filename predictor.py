# Molecular Property Predictor for Sustainable Chemistry
# MBZUAI MSc Computational Biology Portfolio - David A.

from rdkit import Chem
from rdkit.Chem import Descriptors

def analyze_molecule(smiles):
    """Predict key properties for sustainable chemical design"""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return "Invalid SMILES"
    
    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    hbd = Descriptors.NumHDonors(mol)
    
    # Simple biodegradability heuristic
    biodegradable = "Potentially biodegradable" if logp < 3.5 and mw < 500 else "Check further"
    
    return {
        "SMILES": smiles,
        "Molecular Weight": round(mw, 2),
        "LogP": round(logp, 2),
        "H-Bond Donors": hbd,
        "Sustainability Note": biodegradable
    }

# Example - eco-friendly surfactants
test_molecules = ["CCO", "CCCCCCCCCCCCO", "C1=CC=C(C=C1)O"]  # ethanol, dodecanol, phenol

for smi in test_molecules:
    print(analyze_molecule(smi))
