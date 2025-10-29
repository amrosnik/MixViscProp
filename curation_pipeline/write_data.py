import numpy as np
import pandas as pd
import os
from pathlib import Path 

def write_data(nist_knovel_all, test_mols, input_args):

    # Average over all data that looks like duplicates before checkpointing
    nist_knovel_all_nodup = nist_knovel_all.groupby(
        ["MOL_1", "MOL_2", "MolFrac_1"]
    ).mean()
    nist_knovel_all_nodup.reset_index(inplace=True)

    nist_knovel_all_nodup["test_1"] = nist_knovel_all_nodup["MOL_1"].apply(
        lambda smi: smi in test_mols
    )
    nist_knovel_all_nodup["test_2"] = nist_knovel_all_nodup["MOL_2"].apply(
        lambda smi: smi in test_mols
    )
    nist_knovel_all_nodup = nist_knovel_all_nodup[
        ["MOL_1", "MOL_2", "MolFrac_1", "T", "logV", "test_1", "test_2"]
    ]
    test_data = nist_knovel_all_nodup[
        nist_knovel_all_nodup["test_1"] | nist_knovel_all_nodup["test_2"]
    ].dropna()
    train_data = nist_knovel_all_nodup[
        ~(nist_knovel_all_nodup["test_1"] | nist_knovel_all_nodup["test_2"])
    ].dropna()

    # check if out_path exists before writing files 
    outpath = Path(input_args["out_path"]) 
    if not outpath.exists():
        outpath.mkdir()

    data_path = outpath / "data.csv"
    data_features_path = outpath / "data_features.csv"
    test_path = outpath / "test.csv"
    test_features_path = outpath / "test_features.csv"

    train_data[["MOL_1", "MOL_2", "logV"]].to_csv(
        data_path, index=False
    )
    train_data[["MolFrac_1", "T"]].to_csv(
        data_features_path, index=False
    )
    test_data[["MOL_1", "MOL_2", "logV"]].to_csv(
        test_path, index=False
    )
    test_data[["MolFrac_1", "T"]].to_csv(
        test_features_path, index=False
    )
