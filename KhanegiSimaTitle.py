

def KhanegiSimaTitle(khanegi, sima):
    import pandas as pd
    khanegi['title'] = khanegi['title'].str.strip()
#    khanegi['year'] = khanegi['year'].astype(str).replace('\.0', '', regex=True)
    khanegi_title = pd.DataFrame()
    khanegi_title['year'] = khanegi['year']
    khanegi_title['title'] = khanegi['title']
    for i in range(1, len(khanegi)):
        print(i)
        if khanegi_title.loc[i, 'year'] == 'nan' and khanegi_title.loc[i, 'title'] == 'nan':
            khanegi_title.loc[i, 'year'] = khanegi_title.loc[i-1, 'year']
            khanegi_title.loc[i, 'title'] = khanegi_title.loc[i-1, 'title']
    khanegi_title1395 = khanegi_title.query('year == "1395"')
    khanegi_title1396 = khanegi_title.query('year == "1396"')
    khanegi_title1397 = khanegi_title.query('year == "1397"')
    khanegi_title1398 = khanegi_title.query('year == "1398"')
    khanegi_title1399 = khanegi_title.query('year == "1399"')
    khanegi_title1400 = khanegi_title.query('year == "1400"')
    khanegi_title = pd.DataFrame()
    khanegi_title = khanegi_title1395.append([khanegi_title1396,khanegi_title1397,khanegi_title1398,khanegi_title1399,khanegi_title1400])
    khanegi_title_count = khanegi_title.copy()
    khanegi_title_count.drop_duplicates(subset =['title'], keep = 'last', inplace = True)
    khanegi_title_count = khanegi_title_count.reset_index()
    del khanegi_title_count['index']
    
    sima['title'] = sima['title'].str.strip()
#    sima['year'] = sima['year'].astype(str).replace('.0', '', regex=True)
    sima_title = pd.DataFrame()
    sima_title['year'] = sima['year']
    sima_title['title'] = sima['title']
    for i in range(1, len(sima)):
        print(i)
        if sima_title.loc[i, 'year'] == 'nan' and sima_title.loc[i, 'title'] == 'nan':
            sima_title.loc[i, 'year'] = sima_title.loc[i-1, 'year']
            sima_title.loc[i, 'title'] = sima_title.loc[i-1, 'title']
    sima_title1395 = sima_title.query('year == "1395"')
    sima_title1396 = sima_title.query('year == "1396"')
    sima_title1397 = sima_title.query('year == "1397"')
    sima_title1398 = sima_title.query('year == "1398"')
    sima_title1399 = sima_title.query('year == "1399"')
    sima_title1400 = sima_title.query('year == "1400"')
    sima_title = pd.DataFrame()
    sima_title = sima_title1395.append([sima_title1396,sima_title1397,sima_title1398,sima_title1399,sima_title1400])
    sima_title_count = sima_title.copy()
    sima_title_count.drop_duplicates(subset =['title'], keep = 'last', inplace = True)
    sima_title_count = sima_title_count.reset_index()
    del sima_title_count['index']
    
    return khanegi_title_count, sima_title_count















