import pandas as pd

khanegi=pd.read_excel(r'E:\python codes\vod moh rast\khanegi.xlsx')
sima=pd.read_excel(r'E:\python codes\vod moh rast\sima.xlsx')

del khanegi['ردیف']
del sima['ردیف']
#khanegi.insert(10, 'platform', 'khanegi')
#sima.insert(10, 'platform', 'sima')
total_raw = khanegi.append([sima])

total_raw['year'].fillna(method='ffill', inplace=True)  
total_raw['year'] = total_raw['year'].astype(int).astype(str)
total_1395 = total_raw.query('year == "1395"')
total_1396 = total_raw.query('year == "1396"')
total_1397 = total_raw.query('year == "1397"')
total_1398 = total_raw.query('year == "1398"')
total_1399 = total_raw.query('year == "1399"')
total_1400 = total_raw.query('year == "1400"')
total = total_1395.append([total_1396,total_1397,total_1398,total_1399,total_1400])
### Casts ###
total_casts = pd.DataFrame()
total_casts['year'] = total['year']
total_casts['casts'] = total['casts']
total_casts_unique = total_casts.copy()
total_casts_unique.drop_duplicates(subset =['casts'], keep = 'last', inplace = True)
### Director ###
total_director = pd.DataFrame()
total_director['year'] = total['year']
total_director['director'] = total['director']
total_director_unique = total_director.copy()
total_director_unique.drop_duplicates(subset =['director'], keep = 'last', inplace = True)
### Producer ###
total_Producer = pd.DataFrame()
total_Producer['year'] = total['year']
total_Producer['producer'] = total['producer']
total_Producer_unique = total_Producer.copy()
total_Producer_unique.drop_duplicates(subset =['producer'], keep = 'last', inplace = True)
### Writer ###
total_Writer = pd.DataFrame()
total_Writer['year'] = total['year']
total_Writer['writer'] = total['writer']
total_Writer_unique = total_Writer.copy()
total_Writer_unique.drop_duplicates(subset =['writer'], keep = 'last', inplace = True)
### produce_manager ###
total_produce_manager = pd.DataFrame()
total_produce_manager['year'] = total['year']
total_produce_manager['produce_manager'] = total['produce_manager']
total_produce_manager_unique = total_produce_manager.copy()
#total_produce_manager_unique = total_produce_manager_unique.drop(577)
total_produce_manager_unique.drop_duplicates(subset =['produce_manager'], keep = 'last', inplace = True)
### Cameraman ###
total_Cameraman = pd.DataFrame()
total_Cameraman['year'] = total['year']
total_Cameraman['cameraman'] = total['cameraman']
total_Cameraman_unique = total_Cameraman.copy()
total_Cameraman_unique.drop_duplicates(subset =['cameraman'], keep = 'last', inplace = True)
### Editor ###
total_Editor = pd.DataFrame()
total_Editor['year'] = total['year']
total_Editor['editor'] = total['editor']
total_Editor_unique = total_Editor.copy()
total_Editor_unique.drop_duplicates(subset =['editor'], keep = 'last', inplace = True)
########################### khanegi_sima_title ############################
from KhanegiSimaTitle import *

########################### Casts ############################
######### khanegi_casts #########
from KhanegiCasts import * 
######### sima_casts #########
from SimaCasts import *
######### migrate_casts #########
from Migration_casts import *

########################### Director ############################
######### khanegi_director #########
from KhanegiDirector import * 
######### sima_director #########
from SimaDirector import * 
######### migrate_director #########
from Migration_director import *

########################### Producer ############################
######### khanegi_producer #########
from KhanegiProducer import *
######### sima_producer #########
from SimaProducer import *
######### migrate_producer #########
from Migration_producer import *

########################### Writer ############################
######### khanegi_writer #########
from KhanegiWriter import *
######### sima_writer #########
from SimaWriter import *
######### migrate_writer #########
from Migration_writer import *

########################### ProducManager ############################
######### khanegi_ProducManager #########
from KhanegiProducManager import * 
######### sima_ProducManager #########
from SimaProducManager import *
######### migrate_ProducManager #########
from Migration_produc_manager import *

########################### Cameraman ############################
######### khanegi_Cameraman #########
from KhanegiCameraman import * 
######### sima_Cameraman #########
from SimaCameraman import *
######### migrate_Cameraman #########
from Migration_cameraman import *

########################### Editor ############################
######### khanegi_Editor #########
from KhanegiEditor import * 
######### sima_Editor #########
from SimaEditor import *
######### migrate_Editor #########
from Migration_editor import *

########################### RESULTS ############################
[khanegi_title_count, sima_title_count] = KhanegiSimaTitle(khanegi, sima)

[khanegi_casts, khanegi1] = KhanegiCasts(khanegi)
sima_casts = SimaCasts(sima)
[sima_casts,  khanegi_casts] = Migration_casts(sima_casts, khanegi_casts)

khanegi_director = KhanegiDirector(khanegi)
sima_director = SimaDirector(sima)
[sima_director,  khanegi_director] = Migration_director(sima_director, khanegi_director)

khanegi_producer = KhanegiProducer(khanegi)
sima_producer = SimaProducer(sima)
[sima_producer,  khanegi_producer] = Migration_producer(sima_producer, khanegi_producer)

khanegi_writer = KhanegiWriter(khanegi)
sima_writer = SimaWriter(sima)
[sima_writer,  khanegi_writer] = Migration_writer(sima_writer, khanegi_writer)

khanegi_produce_manager = KhanegiProducManager(khanegi)
sima_produce_manager = SimaProducManager(sima)
[sima_produce_manager,  khanegi_produce_manager] = Migration_produc_manager(sima_produce_manager, khanegi_produce_manager)

khanegi_cameraman = KhanegiCameraman(khanegi)
sima_cameraman = SimaCameraman(sima)
[sima_cameraman,  khanegi_cameraman] = Migration_cameraman(sima_cameraman, khanegi_cameraman)

khanegi_editor = KhanegiEditor(khanegi)
sima_editor = SimaEditor(sima)
[sima_editor,  khanegi_editor] = Migration_editor(sima_editor, khanegi_editor)
############################################################################

results = pd.DataFrame()
results.insert(0, 'x', '')
results.insert(1, 'سیما', '')
results.insert(2, 'نمایش خانگی', '')

results.loc[0, 'x'] = 'تعداد محتوا'

results.loc[1, 'x'] = 'تعداد بازیگران'
results.loc[2, 'x'] = 'درصد ماندگاری بازیگران'
results.loc[3, 'x'] = 'درصد کوچ بازیگران'

results.loc[4, 'x'] = 'تعداد کارگردانان'
results.loc[5, 'x'] = 'درصد ماندگاری کارگردانان'
results.loc[6, 'x'] = 'درصد کوچ کارگردنان'

results.loc[7, 'x'] = 'تعداد تهیه کنندگان'
results.loc[8, 'x'] = 'درصد ماندگاری تهیه کنندگان'
results.loc[9, 'x'] = 'درصد کوچ تهیه کنندگان'

results.loc[10, 'x'] = 'تعداد نویسندگان'
results.loc[11, 'x'] = 'درصد ماندگاری نویسندگان'
results.loc[12, 'x'] = 'درصد کوچ نویسندگان'

results.loc[13, 'x'] = 'تعداد مدیران تولید'
results.loc[14, 'x'] = 'درصد ماندگاری مدیر تولید'
results.loc[15, 'x'] = 'درصد کوچ مدیر تولید'

results.loc[16, 'x'] = 'تعداد فیلمبرداران'
results.loc[17, 'x'] = 'درصد ماندگاری فیلمبردار'
results.loc[18, 'x'] = 'درصد کوچ فیلمبردار'

results.loc[19, 'x'] = 'تعداد تدوینگران'
results.loc[20, 'x'] = 'درصد ماندگاری تدوینگر'
results.loc[21, 'x'] = 'درصد کوچ تدوینگر'

results.loc[0, 'سیما'] = len(sima_title_count)
results.loc[0, 'نمایش خانگی'] = len(khanegi_title_count)
########################## Casts #############################
results.loc[1, 'سیما'] = len(sima_casts)
k = 0
for i in range(0, len(sima_casts)):
    print(i)
    cast = sima_casts.loc[i, 'casts']
    if cast is not khanegi_casts['casts'] and sima_casts.loc[i, 'score'] > 1:
        k = k + 1
aaa = round(k*100/len(total_casts_unique), 1)
results.loc[2, 'سیما'] = aaa
aa = round(sima_casts['migrate'].sum()*100/len(total_casts_unique), 1)
results.loc[3, 'سیما'] = aa

results.loc[1, 'نمایش خانگی'] = len(khanegi_casts)
k = 0
for i in range(0, len(khanegi_casts)):
    print(i)
    cast = khanegi_casts.loc[i, 'casts']
    if cast is not sima_casts['casts'] and khanegi_casts.loc[i, 'score'] > 1:
        k = k + 1
bbb = round(k*100/len(total_casts_unique), 1)
results.loc[2, 'نمایش خانگی'] = bbb
bb = round(khanegi_casts['migrate'].sum()*100/len(total_casts_unique), 1)
results.loc[3, 'نمایش خانگی'] = bb
######################### Director ##############################
results.loc[4, 'سیما'] = len(sima_director)
k = 0
for i in range(0, len(sima_director)):
    print(i)
    cast = sima_director.loc[i, 'director']
    if cast is not khanegi_director['director'] and sima_director.loc[i, 'score'] > 1:
        k = k + 1
aaa = round(k*100/len(total_director_unique), 1)
results.loc[5, 'سیما'] = aaa
aa = round(sima_director['migrate'].sum()*100/len(total_director_unique), 1)
results.loc[6, 'سیما'] = aa

results.loc[4, 'نمایش خانگی'] = len(khanegi_director)
k = 0
for i in range(0, len(khanegi_director)):
    print(i)
    cast = khanegi_director.loc[i, 'director']
    if cast is not sima_director['director'] and khanegi_director.loc[i, 'score'] > 1:
        k = k + 1
bbb = round(k*100/len(total_director_unique), 1)
results.loc[5, 'نمایش خانگی'] = bbb
bb = round(khanegi_director['migrate'].sum()*100/len(total_director_unique), 1)
results.loc[6, 'نمایش خانگی'] = bb
######################### Producer ##############################
results.loc[7, 'سیما'] = len(sima_producer)
k = 0
for i in range(0, len(sima_producer)):
    print(i)
    cast = sima_producer.loc[i, 'producer']
    if cast is not khanegi_producer['producer'] and sima_producer.loc[i, 'score'] > 1:
        k = k + 1
aaa = round(k*100/len(total_Producer_unique), 1)
results.loc[8, 'سیما'] = aaa
aa = round(sima_producer['migrate'].sum()*100/len(total_Producer_unique), 1)
results.loc[9, 'سیما'] = aa

results.loc[7, 'نمایش خانگی'] = len(khanegi_producer)
k = 0
for i in range(0, len(khanegi_producer)):
    print(i)
    cast = khanegi_producer.loc[i, 'producer']
    if cast is not sima_producer['producer'] and khanegi_producer.loc[i, 'score'] > 1:
        k = k + 1
aaa = round(k*100/len(total_Producer_unique), 1)
results.loc[8, 'نمایش خانگی'] = aaa
aa = round(khanegi_producer['migrate'].sum()*100/len(total_Producer_unique), 1)
results.loc[9, 'نمایش خانگی'] = aa
######################### Writer ##############################
results.loc[10, 'سیما'] = len(sima_writer)
k = 0
for i in range(0, len(sima_writer)):
    print(i)
    cast = sima_writer.loc[i, 'writer']
    if cast is not khanegi_writer['writer'] and sima_writer.loc[i, 'score'] > 1:
        k = k + 1
aaa = round(k*100/len(total_Writer_unique), 1)
results.loc[11, 'سیما'] = aaa
aa = round(sima_writer['migrate'].sum()*100/len(total_Writer_unique), 1)
results.loc[12, 'سیما'] = aa

results.loc[10, 'نمایش خانگی'] = len(khanegi_writer)
k = 0
for i in range(0, len(khanegi_writer)):
    print(i)
    cast = khanegi_writer.loc[i, 'writer']
    if cast is not sima_writer['writer'] and khanegi_writer.loc[i, 'score'] > 1:
        k = k + 1
aaa = round(k*100/len(total_Writer_unique), 1)
results.loc[11, 'نمایش خانگی'] = aaa
aa = round(khanegi_writer['migrate'].sum()*100/len(total_Writer_unique), 1)
results.loc[12, 'نمایش خانگی'] = aa
######################### Producer_Manager ##############################
results.loc[13, 'سیما'] = len(sima_produce_manager)
k = 0
for i in range(0, len(sima_produce_manager)):
    print(i)
    cast = sima_produce_manager.loc[i, 'produce_manager']
    if cast is not khanegi_produce_manager['produce_manager'] and sima_produce_manager.loc[i, 'score'] > 1:
        k = k + 1
aaa = round(k*100/len(total_produce_manager_unique), 1)
results.loc[14, 'سیما'] = aaa
aa = round(sima_produce_manager['migrate'].sum()*100/len(total_produce_manager_unique), 1)
results.loc[15, 'سیما'] = aa

results.loc[13, 'نمایش خانگی'] = len(khanegi_produce_manager)
k = 0
for i in range(0, len(khanegi_produce_manager)):
    print(i)
    cast = khanegi_produce_manager.loc[i, 'produce_manager']
    if cast is not sima_produce_manager['produce_manager'] and khanegi_produce_manager.loc[i, 'score'] > 1:
        k = k + 1
aaa = round(k*100/len(total_produce_manager_unique), 1)
results.loc[14, 'نمایش خانگی'] = aaa
aa = round(khanegi_produce_manager['migrate'].sum()*100/len(total_produce_manager_unique), 1)
results.loc[15, 'نمایش خانگی'] = aa
########################## Cameraman #############################
results.loc[16, 'سیما'] = len(sima_cameraman)
k = 0
for i in range(0, len(sima_cameraman)):
    print(i)
    cast = sima_cameraman.loc[i, 'cameraman']
    if cast is not khanegi_cameraman['cameraman'] and sima_cameraman.loc[i, 'score'] > 1:
        k = k + 1
aaa = round(k*100/len(total_Cameraman_unique), 1)
results.loc[17, 'سیما'] = aaa
aa = round(sima_cameraman['migrate'].sum()*100/len(total_Cameraman_unique), 1)
results.loc[18, 'سیما'] = aa

results.loc[16, 'نمایش خانگی'] = len(khanegi_cameraman)
k = 0
for i in range(0, len(khanegi_cameraman)):
    print(i)
    cast = khanegi_cameraman.loc[i, 'cameraman']
    if cast is not sima_cameraman['cameraman'] and khanegi_cameraman.loc[i, 'score'] > 1:
        k = k + 1
aaa = round(k*100/len(total_Cameraman_unique), 1)
results.loc[17, 'نمایش خانگی'] = aaa
aa = round(khanegi_cameraman['migrate'].sum()*100/len(total_Cameraman_unique), 1)
results.loc[18, 'نمایش خانگی'] = aa
########################### Editor ############################
results.loc[19, 'سیما'] = len(sima_editor)
k = 0
for i in range(0, len(sima_editor)):
    print(i)
    cast = sima_editor.loc[i, 'editor']
    if cast is not khanegi_editor['editor'] and sima_editor.loc[i, 'score'] > 1:
        k = k + 1
aaa = round(k*100/len(total_Editor_unique), 1)
results.loc[20, 'سیما'] = aaa
aa = round(sima_editor['migrate'].sum()*100/len(total_Editor_unique), 1)
results.loc[21, 'سیما'] = aa

results.loc[19, 'نمایش خانگی'] = len(khanegi_editor)
k = 0
for i in range(0, len(khanegi_editor)):
    print(i)
    cast = khanegi_editor.loc[i, 'editor']
    if cast is not sima_editor['editor'] and khanegi_editor.loc[i, 'score'] > 1:
        k = k + 1
aaa = round(k*100/len(total_Editor_unique), 1)
results.loc[20, 'نمایش خانگی'] = aaa
aa = round(khanegi_editor['migrate'].sum()*100/len(total_Editor_unique), 1)
results.loc[21, 'نمایش خانگی'] = aa
#######################################################
#######################################################
#######################################################


results.to_excel('results2.xlsx', index=False)






















