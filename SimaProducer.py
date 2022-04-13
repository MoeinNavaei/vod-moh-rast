def SimaProducer(sima):
    import pandas as pd
    sima['producer'] = sima['producer'].str.strip()
#    sima['year'] = sima['year'].astype(str).replace('.0', '', regex=True)
    sima1 = pd.DataFrame()
    sima1['producer'] = sima['producer']
    sima1['year'] = sima['year']
    # sima1['year'].replace('nan', '', inplace=True)
    # sima1.fillna(method='ffill', inplace=True)
    for i in range(1, len(sima1)):
        print(i)
        if sima1.loc[i, 'year'] == 'nan':
            sima1.loc[i, 'year'] = sima1.loc[i-1, 'year']
    
    year_1395 = sima1.query('year == "1395"')
    del year_1395['year']
    year_1395.drop_duplicates(subset =['producer'], keep = 'last', inplace = True)
    year_1395 = year_1395.reset_index()
    del year_1395['index']
    
    year_1396 = sima1.query('year == "1396"')
    del year_1396['year']
    year_1396.drop_duplicates(subset =['producer'], keep = 'last', inplace = True)
    year_1396 = year_1396.reset_index()
    del year_1396['index']
    
    year_1397 = sima1.query('year == "1397"')
    del year_1397['year']
    year_1397.drop_duplicates(subset =['producer'], keep = 'last', inplace = True)
    year_1397 = year_1397.reset_index()
    del year_1397['index']
    
    year_1398 = sima1.query('year == "1398"')
    del year_1398['year']
    year_1398.drop_duplicates(subset =['producer'], keep = 'last', inplace = True)
    year_1398 = year_1398.reset_index()
    del year_1398['index']
    
    year_1399 = sima1.query('year == "1399"')
    del year_1399['year']
    year_1399.drop_duplicates(subset =['producer'], keep = 'last', inplace = True)
    year_1399 = year_1399.reset_index()
    del year_1399['index']
    
    year_1400 = sima1.query('year == "1400"')
    del year_1400['year']
    year_1400.drop_duplicates(subset =['producer'], keep = 'last', inplace = True)
    year_1400 = year_1400.reset_index()
    del year_1400['index']
    
    sima_producer = pd.DataFrame()
    sima_producer = year_1395.append([year_1396,year_1397,year_1398,year_1399,year_1400])
    sima_producer.drop_duplicates(subset =['producer'], keep = 'last', inplace = True)
    sima_producer = sima_producer.reset_index()
    del sima_producer['index']
    sima_producer.insert(1, '1395', '')
    sima_producer.insert(2, '1396', '')
    sima_producer.insert(3, '1397', '')
    sima_producer.insert(4, '1398', '')
    sima_producer.insert(5, '1399', '')
    sima_producer.insert(6, '1400', '')
    
    for i in range(0, len(sima_producer)):
        print(i)
        for j1 in range(0, len(year_1395)):
            if sima_producer.loc[i, 'producer'] == year_1395.loc[j1, 'producer']:
                sima_producer.loc[i, '1395'] = 1
                break
        for j1 in range(0, len(year_1396)):
            if sima_producer.loc[i, 'producer'] == year_1396.loc[j1, 'producer']:
                sima_producer.loc[i, '1396'] = 1
                break
        for j1 in range(0, len(year_1397)):
            if sima_producer.loc[i, 'producer'] == year_1397.loc[j1, 'producer']:
                sima_producer.loc[i, '1397'] = 1
                break
        for j1 in range(0, len(year_1398)):
            if sima_producer.loc[i, 'producer'] == year_1398.loc[j1, 'producer']:
                sima_producer.loc[i, '1398'] = 1
                break
        for j1 in range(0, len(year_1399)):
            if sima_producer.loc[i, 'producer'] == year_1399.loc[j1, 'producer']:
                sima_producer.loc[i, '1399'] = 1
                break
        for j1 in range(0, len(year_1400)):
            if sima_producer.loc[i, 'producer'] == year_1400.loc[j1, 'producer']:
                sima_producer.loc[i, '1400'] = 1
                break
    
    sima_producer = sima_producer.fillna(0)
    sima_producer.replace('', '0', inplace=True)
    sima_producer['1395'] = sima_producer['1395'].astype(int)
    sima_producer['1396'] = sima_producer['1396'].astype(int)
    sima_producer['1397'] = sima_producer['1397'].astype(int)
    sima_producer['1398'] = sima_producer['1398'].astype(int)
    sima_producer['1399'] = sima_producer['1399'].astype(int)
    sima_producer['1400'] = sima_producer['1400'].astype(int)
    for i in range(0, len(sima_producer)):
        print(i)
        sum_score = sima_producer.loc[i, '1395']+sima_producer.loc[i, '1396']+sima_producer.loc[i, '1397']+sima_producer.loc[i, '1398']+sima_producer.loc[i, '1399']+sima_producer.loc[i, '1400']
        sima_producer.loc[i, 'score'] = sum_score - 1
    return sima_producer
