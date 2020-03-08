import os
import glob
import pandas as pd

os.chdir('data/source')

cats = [
 'astro-ph', 'cond-mat', 'gr-qc', 'hep-ex', 'hep-lat', 'hep-ph', 'hep-th',
 'math-ph', 'nlin', 'nucl-ex', 'nucl-th', 'physics', 'quant-ph', 'math', 'CoRR',
 'q-bio','q-fin', 'stat'
 ]

extension = 'csv'
all_files = ['extracted_'+i+'.csv' for i in cats]
print(all_files)
combined_csv = pd.concat([pd.read_csv(f) for f in all_files]).drop_duplicates(subset="id")
try:
    for f in all_files:
        os.remove(f) 
    combined_csv.to_csv('extracted_allCategory.csv', index= False, encoding = 'utf-8-sig')
except Exception as e:
    print('\n',e)

os.chdir(...)