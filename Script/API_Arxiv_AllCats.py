'''
Import packages
'''

import pandas as pd

source_filepath = "data/source"
cols= ['id', 'title', 'categories', 'abstract', 'updated','authors']
cats = [
 'astro-ph', 'cond-mat', 'gr-qc', 'hep-ex', 'hep-lat', 'hep-ph', 'hep-th',
 'math-ph', 'nlin', 'nucl-ex', 'nucl-th', 'physics', 'quant-ph', 'math', 'CoRR',
 'q-bio','q-fin', 'stat'
 ]

def API_ARXIV(cat, date_from, date_until):
    
    import arxivscraper

    df = pd.DataFrame(columns = cols)
    #for cat in cats:
    scraper = arxivscraper.Scraper(category = cat, date_from = date_from, date_until=date_until, t = 30)
    try:
         #adding the output to the dataset
        output = scraper.scrape()
        df_output = pd.DataFrame(output,columns = cols)
        print('\n Test')
        df = df.append(df_output)
        print('\n Completed' )
    except Exception as e:
        print(e )
    df.to_csv(source_filepath+"/extracted"+"_"+cat+".csv", encoding='utf-8-sig', index=False)
    pass
'''
Define Scraper and get data
'''
#define the instance 
date_from = str(input("Inserire data di inizio (yyyy-mm-dd): "))
date_until = str(input("Inserire data di fine (yyyy-mm-dd): "))
for cat in list(cats):
    API_ARXIV(cat, date_from, date_until)
    