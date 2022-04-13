def KhanegiEditor(khanegi):
    import pandas as pd
    khanegi['editor'] = khanegi['editor'].str.strip()
#    khanegi['year'] = khanegi['year'].astype(str).replace('\.0', '', regex=True)
    khanegi1 = pd.DataFrame()
    khanegi1['editor'] = khanegi['editor']
    khanegi1['year'] = khanegi['year']
    for i in range(1, len(khanegi1)):
        print(i)
        if khanegi1.loc[i, 'year'] == 'nan':
            khanegi1.loc[i, 'year'] = khanegi1.loc[i-1, 'year']
    
    year_1395 = khanegi1.query('year == "1395"')
    del year_1395['year']
    year_1395.drop_duplicates(subset =['editor'], keep = 'last', inplace = True)
    year_1395 = year_1395.reset_index()
    del year_1395['index']
    
    year_1396 = khanegi1.query('year == "1396"')
    del year_1396['year']
    year_1396.drop_duplicates(subset =['editor'], keep = 'last', inplace = True)
    year_1396 = year_1396.reset_index()
    del year_1396['index']
    
    year_1397 = khanegi1.query('year == "1397"')
    del year_1397['year']
    year_1397.drop_duplicates(subset =['editor'], keep = 'last', inplace = True)
    year_1397 = year_1397.reset_index()
    del year_1397['index']
    
    year_1398 = khanegi1.query('year == "1398"')
    del year_1398['year']
    year_1398.drop_duplicates(subset =['editor'], keep = 'last', inplace = True)
    year_1398 = year_1398.reset_index()
    del year_1398['index']
    
    year_1399 = khanegi1.query('year == "1399"')
    del year_1399['year']
    year_1399.drop_duplicates(subset =['editor'], keep = 'last', inplace = True)
    year_1399 = year_1399.reset_index()
    del year_1399['index']
    
    year_1400 = khanegi1.query('year == "1400"')
    del year_1400['year']
    year_1400.drop_duplicates(subset =['editor'], keep = 'last', inplace = True)
    year_1400 = year_1400.reset_index()
    del year_1400['index']
    
    khanegi_editor = pd.DataFrame()
    khanegi_editor = year_1395.append([year_1396,year_1397,year_1398,year_1399,year_1400])
    khanegi_editor.drop_duplicates(subset =['editor'], keep = 'last', inplace = True)
    khanegi_editor = khanegi_editor.reset_index()
    del khanegi_editor['index']
    khanegi_editor.insert(1, '1395', '')
    khanegi_editor.insert(2, '1396', '')
    khanegi_editor.insert(3, '1397', '')
    khanegi_editor.insert(4, '1398', '')
    khanegi_editor.insert(5, '1399', '')
    khanegi_editor.insert(6, '1400', '')
    
    for i in range(0, len(khanegi_editor)):
        print(i)
        for j1 in range(0, len(year_1395)):
            if khanegi_editor.loc[i, 'editor'] == year_1395.loc[j1, 'editor']:
                khanegi_editor.loc[i, '1395'] = 1
                break
        for j1 in range(0, len(year_1396)):
            if khanegi_editor.loc[i, 'editor'] == year_1396.loc[j1, 'editor']:
                khanegi_editor.loc[i, '1396'] = 1
                break
        for j1 in range(0, len(year_1397)):
            if khanegi_editor.loc[i, 'editor'] == year_1397.loc[j1, 'editor']:
                khanegi_editor.loc[i, '1397'] = 1
                break
        for j1 in range(0, len(year_1398)):
            if khanegi_editor.loc[i, 'editor'] == year_1398.loc[j1, 'editor']:
                khanegi_editor.loc[i, '1398'] = 1
                break
        for j1 in range(0, len(year_1399)):
            if khanegi_editor.loc[i, 'editor'] == year_1399.loc[j1, 'editor']:
                khanegi_editor.loc[i, '1399'] = 1
                break
        for j1 in range(0, len(year_1400)):
            if khanegi_editor.loc[i, 'editor'] == year_1400.loc[j1, 'editor']:
                khanegi_editor.loc[i, '1400'] = 1
                break
    
    khanegi_editor = khanegi_editor.fillna(0)
    khanegi_editor.replace('', '0', inplace=True)
    khanegi_editor['1395'] = khanegi_editor['1395'].astype(int)
    khanegi_editor['1396'] = khanegi_editor['1396'].astype(int)
    khanegi_editor['1397'] = khanegi_editor['1397'].astype(int)
    khanegi_editor['1398'] = khanegi_editor['1398'].astype(int)
    khanegi_editor['1399'] = khanegi_editor['1399'].astype(int)
    khanegi_editor['1400'] = khanegi_editor['1400'].astype(int)
    for i in range(0, len(khanegi_editor)):
        print(i)
        sum_score = khanegi_editor.loc[i, '1395']+khanegi_editor.loc[i, '1396']+khanegi_editor.loc[i, '1397']+khanegi_editor.loc[i, '1398']+khanegi_editor.loc[i, '1399']+khanegi_editor.loc[i, '1400']
        khanegi_editor.loc[i, 'score'] = sum_score - 1
    return khanegi_editor