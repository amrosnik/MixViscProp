from curation_pipeline.pipeline import prepare_dataset

input_args = {
    "NIST": "~/Downloads/pretrained_models/nist_dippr_source/NIST_Visc_Data.csv",  # Path to NIST data
    "DIPPR": "~/Downloads/pretrained_models/nist_dippr_source/logV_bp_mp.csv",  # Path to DIPPR data
    "bp_pred_path": "~/Downloads/pretrained_models/bp_data/bp_pred.csv",  # Path to boiling point data (already predicted)
    "mp_pred_path": "~/Downloadspretrained_models/mp_data/mp_pred.csv",  # Path to melting point data (already predicted)
    "dummy_mol": "CCO",  # Dummy compound for mixing in DIPPR pure component data
    "dippr_ref_T": 298,  # DIPPR temperature
    "test_split": 0.2,  # Fraction to hold out for testing
    "thresh_pure": 0.025,  # Settings for inconsistent pure data screening
    "thresh_logV": 0.5,  # Settings for inconsistent pure data screening
    "out_path":"~/Downloads/data_cleaned" # Location for files to be written to
    
}

prepare_dataset(input_args)
