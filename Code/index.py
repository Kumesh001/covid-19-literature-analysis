import glob
import json
import numpy as np
import pandas as pd
import matplotlib as plt

import FileReader


root_path = 'C:/Users/Dell/Desktop/Covid-19/CORD-19-research-challenge'
metadata_path = f'{root_path}/metadata.csv'
meta_df = pd.read_csv(metadata_path,dtype={
    'pubmed_id':str,
    'Microsoft Academic Paper ID':str,
    'doi':str   
})

meta_df.head()

all_json= glob.glob(f'{root_path}/**/*.json',recursive=True)
len(all_json)
