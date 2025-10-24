import pandas as pd
import numpy as np 
from pathlib import Path

def get_salt_aqueous_data(nist_knovel_all,out_path=Path.cwd()):

    print(nist_knovel_all.head())

    # Count number of data points that are salts or where one species is water  
    salt_nist = nist_knovel_all.loc[nist_knovel_all["MOL_1"].str.contains(".",regex=False) |nist_knovel_all["MOL_2"].str.contains(".",regex=False) | (nist_knovel_all["MOL_1"] == "O") | (nist_knovel_all["MOL_2"] == "O") ]
    num_salt_nist = len(salt_nist)
    #print(num_salt_nist)
    #print(num_salt_nist/len(nist_knovel_all))

    return(salt_nist)