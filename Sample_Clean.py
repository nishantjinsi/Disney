
# coding: utf-8

# In[19]:

import pandas as pd
import numpy as np

df = pd.read_csv('/home/dbadmin/Desktop/econometric_table_v40.csv')



condition_for_OUW = np.all(np.array([df.progcode == "OUW",df.year == 2013]), axis=0)

df  = df[~condition_for_OUW]
ACA_deletion_condition = np.all(np.array([df.progcode == "ACA"]),axis=0)
df = df[~ACA_deletion_condition]

EXH_deletion_condition = np.all(np.array([df.progcode == "EXH"]),axis=0)
df = df[~EXH_deletion_condition]
EXP_deletion_condition = np.all(np.array([df.progcode == "EXP"]),axis=0)
df = df[~EXP_deletion_condition]
FVD_deletion_condition = np.all(np.array([df.progcode == "FVD"]),axis=0)
df = df[~FVD_deletion_condition]
YDI_deletion_condition = np.all(np.array([df.progcode == "YDI"]),axis=0)
df = df[~YDI_deletion_condition]
PRT_deletion_condition = np.all(np.array([df.progcode == "PRT"]),axis=0)
df = df[~PRT_deletion_condition]
SNF_deletion_condition = np.all(np.array([df.progcode == "SNF"]),axis=0)
df = df[~SNF_deletion_condition]
TWT_deletion_condition = np.all(np.array([df.progcode == "TWT"]),axis=0)
df = df[~TWT_deletion_condition]
WLG_deletion_condition = np.all(np.array([df.progcode == "WLG"]),axis=0)
df = df[~WLG_deletion_condition]
DWR_deletion_condition = np.all(np.array([df.progcode == "DWR"]),axis=0)
df = df[~DWR_deletion_condition]
BLX_deletion_condition = np.all(np.array([df.progcode == "BLX"]),axis=0)
df = df[~BLX_deletion_condition]
QST_deletion_condition = np.all(np.array([df.progcode == "QST"]),axis=0)
df = df[~QST_deletion_condition]
RIS_deletion_condition = np.all(np.array([df.progcode == "RIS"]),axis=0)
df = df[~RIS_deletion_condition]

Deletion_DWS_conditions1 = np.logical_and(df.progcode == "DWS", df.week == 33)
Deletion_DWS_conditions2 = np.logical_and(Deletion_DWS_conditions1, df.year==2010)
df = df[~Deletion_DWS_conditions2]
Deletion_BOD_conditions1 = np.logical_and(df.progcode == "BOD", df.week == 33)
Deletion_BOD_conditions2 = np.logical_and(Deletion_BOD_conditions1, df.year==2011)
df = df[~Deletion_BOD_conditions2]
Deletion_SBG_conditions1 = np.logical_and(df.progcode == "SBG", df.week == 37)
Deletion_SBG_conditions2 = np.logical_and(Deletion_SBG_conditions1, df.year==2012)
df = df[~Deletion_SBG_conditions2]
Deletion_SBG_conditions1 = np.logical_and(df.progcode == "SBG", df.week == 38)
Deletion_SBG_conditions2 = np.logical_and(Deletion_SBG_conditions1, df.year==2012)
df = df[~Deletion_SBG_conditions2]
Deletion_SBG_conditions1 = np.logical_and(df.progcode == "SBG", df.week == 39)
Deletion_SBG_conditions2 = np.logical_and(Deletion_SBG_conditions1, df.year==2012)
df = df[~Deletion_SBG_conditions2]

DWR_deletion_condition = np.logical_and( df.progcode == "DWR",  df.tc_date =='03Apr2012'   )
df = df[~DWR_deletion_condition]
FLF_deletion_condition = np.logical_and( df.progcode == "FLF",  df.tc_date =='16Mar2010'   )
df = df[~FLF_deletion_condition]
SCD_deletion_condition = np.logical_and( df.progcode == "SCD",  df.tc_date =='09Apr2012'   )
df = df[~SCD_deletion_condition]
VVV_deletion_condition = np.logical_and( df.progcode == "VVV",  df.tc_date =='23Mar2010'   )
df = df[~VVV_deletion_condition]

df.target_date = pd.to_datetime(df.target_date, format= '%d%b%Y')
df.loc[(df['target_date']>= '2007-09-24') & (df['target_date'] < '2008-09-22'),'season'] = 2007
df.loc[(df['target_date']>= '2008-09-22') & (df['target_date'] < '2009-09-21'),'season'] = 2008
df.loc[(df['target_date']>= '2009-09-21') & (df['target_date'] < '2010-09-20'),'season'] = 2009
df.loc[(df['target_date']>= '2010-09-20') & (df['target_date'] < '2011-09-19'),'season'] = 2010
df.loc[(df['target_date']>= '2011-09-19') & (df['target_date'] < '2012-09-14'),'season'] = 2011
df.loc[(df['target_date']>= '2012-09-14') & (df['target_date'] < '2013-09-14'),'season'] = 2012
df.loc[(df['target_date']>= '2013-09-14') & (df['target_date'] < '2014-09-14'),'season'] = 2013



Season_condition = np.logical_and( df.season >= 2007,  df.season <= 2014   )
df = df[Season_condition]

df.tc_date = pd.to_datetime(df.tc_date, format= '%d%b%Y')
df.loc[(df['tc_date']>= '2014-02-01') & (df['tc_date'] < '2015-06-01'),'MidSeason'] = 1
df.loc[(df['tc_date']>= '2013-02-01') & (df['tc_date'] < '2013-06-01'),'MidSeason'] = 1
df.loc[(df['tc_date']>= '2012-02-01') & (df['tc_date'] < '2012-06-01'),'MidSeason'] = 1
df.loc[(df['tc_date']>= '2011-02-01') & (df['tc_date'] < '2011-06-01'),'MidSeason'] = 1
df.loc[(df['tc_date']>= '2010-02-01') & (df['tc_date'] < '2010-06-01'),'MidSeason'] = 1
df.loc[(df['tc_date']>= '2009-02-01') & (df['tc_date'] < '2009-06-01'),'MidSeason'] = 1
df.loc[(df['tc_date']>= '2008-02-01') & (df['tc_date'] < '2008-06-01'),'MidSeason'] = 1
df.loc[(df['tc_date']>= '2007-02-01') & (df['tc_date'] < '2007-06-01'),'MidSeason'] = 1

Assigning_REV_conditions = np.logical_and( df.progcode == "REV", df.year == 2011)
df["model_ind"][Assigning_REV_conditions]=1

BSH_assign_condition = np.all(np.array([df.progcode == "BSH"]),axis=0)
df["model_ind"][BSH_assign_condition]=1
df["new_series"][BSH_assign_condition]=1
SFE_assign_condition = np.all(np.array([df.progcode == "SFE"]),axis=0)
df["model_ind"][BSH_assign_condition]=1
df["new_series"][BSH_assign_condition]=1
MVS_assign_condition = np.all(np.array([df.progcode == "MVS"]),axis=0)
df["model_ind"][BSH_assign_condition]=1
df["new_series"][BSH_assign_condition]=1
HGM_assign_condition = np.all(np.array([df.progcode == "HGM"]),axis=0)
df["model_ind"][BSH_assign_condition]=1
df["new_series"][BSH_assign_condition]=1
CRS_assign_condition = np.all(np.array([df.progcode == "CRS"]),axis=0)
df["model_ind"][BSH_assign_condition]=1
df["new_series"][BSH_assign_condition]=1
FRV_assign_condition = np.all(np.array([df.progcode == "FRV"]),axis=0)
df["model_ind"][BSH_assign_condition]=1
df["new_series"][BSH_assign_condition]=1
MGM_assign_condition = np.all(np.array([df.progcode == "MGM"]),axis=0)
df["model_ind"][BSH_assign_condition]=1
df["new_series"][BSH_assign_condition]=1
MIX_assign_condition = np.all(np.array([df.progcode == "MIX"]),axis=0)
df["model_ind"][BSH_assign_condition]=1
df["new_series"][BSH_assign_condition]=1
RES_assign_condition = np.all(np.array([df.progcode == "RES"]),axis=0)
df["model_ind"][BSH_assign_condition]=1
df["new_series"][BSH_assign_condition]=1

df['Lnc3'] = np.log(df['c3'])
df['LnLeadin'] = np.log(df['leadin_prev_halfhour'])
df['Ln_PctAware'] = np.log(df['awn_all_pctaware'])

df['Ln_PctAwareUnaided'] = np.log(df['awn_all_pctawareunaided'])

df['Ln_Top2Box_AmgTtl'] = np.log(df['awn_all_top2box_amgttl'])


df['Day1'] = df.dow=='M'
df['Day1'] = df.Day1.astype(int)

df['Day2'] = df.dow=='TU'
df['Day2'] = df.Day2.astype(int)

df['Day3'] = df.dow=='W'
df['Day3'] = df.Day3.astype(int)

df['Day4'] = df.dow=='TH'
df['Day4'] = df.Day4.astype(int)

df['Day5'] = df.dow=='F'
df['Day5'] = df.Day5.astype(int)

df['Day6'] = df.dow=='SA'
df['Day6'] = df.Day6.astype(int)

df['Day7'] = df.dow=='SU'
df['Day7'] = df.Day7.astype(int)

df['Time1'] = df.cor_time=='20:00:00'
df['Time1'] = df.Time1.astype(int)

df['Time2'] = df.cor_time=='20:30:00'
df['Time2'] = df.Time2.astype(int)

df['Time3'] = df.cor_time=='21:00:00'
df['Time3'] = df.Time3.astype(int)

df['Time4'] = df.cor_time=='21:30:00'
df['Time4'] = df.Time4.astype(int)

df['Time5'] = df.cor_time=='22:00:00'
df['Time5'] = df.Time5.astype(int)
df['Time6'] = df.cor_time=='22:30:00'
df['Time6'] = df.Time6.astype(int)
df['Time7'] = df.cor_time=='23:00:00'
df['Time7'] = df.Time7.astype(int)
df['Time8'] = df.cor_time=='23:30:00'
df['Time8'] = df.Time8.astype(int)

df['IsDrama'] = (df.prog_type=='Drama') | (df.prog_type=='Comedy/Drama')
df['IsDrama'] = df.IsDrama.astype(int)
df['IsReality'] = (df.prog_type=='Reality')
df['IsReality'] = df.IsReality.astype(int)
df['IsComedy'] = (df.prog_type=='Comedy') | (df.prog_type=='Comedy/Drama') 
df['IsComedy'] = df.IsComedy.astype(int)

df['season07'] = df.season==2007
df['season07'] = df.season07.astype(int)
df['season08'] = df.season==2008
df['season08'] = df.season08.astype(int)
df['season09'] = df.season==2009
df['season09'] = df.season09.astype(int)
df['season10'] = df.season==2010
df['season10'] = df.season10.astype(int)
df['season11'] = df.season==2011
df['season11'] = df.season11.astype(int)
df['season12'] = df.season==2012
df['season12'] = df.season12.astype(int)
df['season13'] = df.season==2013
df['season13'] = df.season13.astype(int)
df['season14'] = df.season==2014
df['season14'] = df.season14.astype(int)



df['Wed10pm']=df.Day3 * df.Time5
df['Wed10pm'] = df.Wed10pm.astype(int)
df['Thu8pm']=df.Day4 * df.Time1
df['Thu8pm'] = df.Thu8pm.astype(int)
df['Sun10pm']=df.Day7 * df.Time5
df['Sun10pm'] = df.Sun10pm.astype(int)


# In[35]:

df = pd.read_csv('/home/dbadmin/Desktop/econometric_table_v40.csv')



condition_for_OUW = np.all(np.array([df.progcode == "OUW",df.year == 2013]), axis=0)
df  = df[~condition_for_OUW]

Assigning_OUW_conditions1 = np.logical_and(df.progcode == "OUW", df.week == 40)
df["nationalcable_actual_trps"][Assigning_OUW_conditions1]=30

ACA_deletion_condition = np.all(np.array([df.progcode == "ACA"]),axis=0)
df = df[~ACA_deletion_condition]

EXH_deletion_condition = np.all(np.array([df.progcode == "EXH"]),axis=0)
df = df[~EXH_deletion_condition]
EXP_deletion_condition = np.all(np.array([df.progcode == "EXP"]),axis=0)
df = df[~EXP_deletion_condition]
FVD_deletion_condition = np.all(np.array([df.progcode == "FVD"]),axis=0)
df = df[~FVD_deletion_condition]
YDI_deletion_condition = np.all(np.array([df.progcode == "YDI"]),axis=0)
df = df[~YDI_deletion_condition]
PRT_deletion_condition = np.all(np.array([df.progcode == "PRT"]),axis=0)
df = df[~PRT_deletion_condition]
SNF_deletion_condition = np.all(np.array([df.progcode == "SNF"]),axis=0)
df = df[~SNF_deletion_condition]
TWT_deletion_condition = np.all(np.array([df.progcode == "TWT"]),axis=0)
df = df[~TWT_deletion_condition]
WLG_deletion_condition = np.all(np.array([df.progcode == "WLG"]),axis=0)
df = df[~WLG_deletion_condition]
DWR_deletion_condition = np.all(np.array([df.progcode == "DWR"]),axis=0)
df = df[~DWR_deletion_condition]
BLX_deletion_condition = np.all(np.array([df.progcode == "BLX"]),axis=0)
df = df[~BLX_deletion_condition]
QST_deletion_condition = np.all(np.array([df.progcode == "QST"]),axis=0)
df = df[~QST_deletion_condition]
RIS_deletion_condition = np.all(np.array([df.progcode == "RIS"]),axis=0)
df = df[~RIS_deletion_condition]

Deletion_DWS_conditions1 = np.logical_and(df.progcode == "DWS", df.week == 33)
Deletion_DWS_conditions2 = np.logical_and(Deletion_DWS_conditions1, df.year==2010)
df = df[~Deletion_DWS_conditions2]
Deletion_BOD_conditions1 = np.logical_and(df.progcode == "BOD", df.week == 33)
Deletion_BOD_conditions2 = np.logical_and(Deletion_BOD_conditions1, df.year==2011)
df = df[~Deletion_BOD_conditions2]
Deletion_SBG_conditions1 = np.logical_and(df.progcode == "SBG", df.week == 37)
Deletion_SBG_conditions2 = np.logical_and(Deletion_SBG_conditions1, df.year==2012)
df = df[~Deletion_SBG_conditions2]
Deletion_SBG_conditions1 = np.logical_and(df.progcode == "SBG", df.week == 38)
Deletion_SBG_conditions2 = np.logical_and(Deletion_SBG_conditions1, df.year==2012)
df = df[~Deletion_SBG_conditions2]
Deletion_SBG_conditions1 = np.logical_and(df.progcode == "SBG", df.week == 39)
Deletion_SBG_conditions2 = np.logical_and(Deletion_SBG_conditions1, df.year==2012)
df = df[~Deletion_SBG_conditions2]

df.tc_date = pd.to_datetime(df.tc_date, format= '%d%b%Y')

DWR_deletion_condition = np.logical_and( df.progcode == "DWR",  df.tc_date =='2012-04-03'   )
df = df[~DWR_deletion_condition]
FLF_deletion_condition = np.logical_and( df.progcode == "FLF",  df.tc_date =='2010-03-16'   )
df = df[~FLF_deletion_condition]
SCD_deletion_condition = np.logical_and( df.progcode == "SCD",  df.tc_date =='2012-04-09'   )
df = df[~SCD_deletion_condition]
VVV_deletion_condition = np.logical_and( df.progcode == "VVV",  df.tc_date =='2010-03-23'   )
df = df[~VVV_deletion_condition]

Deletion_MNP_conditions1 = np.logical_and(df.progcode == "MNP", df.week == 36)
Deletion_MNP_conditions2 = np.logical_and(Deletion_MNP_conditions1, df.year==2011)
df["target_date"][Deletion_MNP_conditions2]=np.NaN
Deletion_MNP_conditions1 = np.logical_and(df.progcode == "MNP", df.week == 37)
Deletion_MNP_conditions2 = np.logical_and(Deletion_MNP_conditions1, df.year==2011)
df["target_date"][Deletion_MNP_conditions2]=np.NaN
Deletion_MNP_conditions1 = np.logical_and(df.progcode == "MNP", df.week == 38)
Deletion_MNP_conditions2 = np.logical_and(Deletion_MNP_conditions1, df.year==2011)
df["target_date"][Deletion_MNP_conditions2]=np.NaN
Deletion_LMS_conditions1 = np.logical_and(df.progcode == "LMS", df.week == 35)
Deletion_LMS_conditions2 = np.logical_and(Deletion_LMS_conditions1, df.year==2011)
df["target_date"][Deletion_LMS_conditions2]='29Aug2011'

Deletion_LMS_conditions1 = np.logical_and(df.progcode == "LMS", df.week == 36)
Deletion_LMS_conditions2 = np.logical_and(Deletion_LMS_conditions1, df.year==2011)
df["target_date"][Deletion_LMS_conditions2]=np.NaN


df.target_date = pd.to_datetime(df.target_date, format= '%d%b%Y')
df.loc[(df['target_date']>= '2007-09-24') & (df['target_date'] < '2008-09-22'),'season'] = 2007
df.loc[(df['target_date']>= '2008-09-22') & (df['target_date'] < '2009-09-21'),'season'] = 2008
df.loc[(df['target_date']>= '2009-09-21') & (df['target_date'] < '2010-09-20'),'season'] = 2009
df.loc[(df['target_date']>= '2010-09-20') & (df['target_date'] < '2011-09-19'),'season'] = 2010
df.loc[(df['target_date']>= '2011-09-19') & (df['target_date'] < '2012-09-14'),'season'] = 2011
df.loc[(df['target_date']>= '2012-09-14') & (df['target_date'] < '2013-09-14'),'season'] = 2012
df.loc[(df['target_date']>= '2013-09-14') & (df['target_date'] < '2014-09-14'),'season'] = 2013
df.loc[(df['target_date']>= '2014-09-14') & (df['target_date'] < '2015-09-14'),'season'] = 2014




Season_condition = np.logical_and( df.season >= 2007,  df.season <= 2014   )
Season_condition2 = np.logical_and(Season_condition, df.season != np.NaN)
df = df[Season_condition2]



TRL_assign_condition = np.all(np.array([df.progcode == "TRL"]),axis=0)
df["season"][TRL_assign_condition ]=2011

df.tc_date = pd.to_datetime(df.tc_date, format= '%d%b%Y')
df.loc[(df['tc_date']>= '2014-02-01') & (df['tc_date'] < '2015-06-01'),'midseason'] = 1
df.loc[(df['tc_date']>= '2013-02-01') & (df['tc_date'] < '2013-06-01'),'midseason'] = 1
df.loc[(df['tc_date']>= '2012-02-01') & (df['tc_date'] < '2012-06-01'),'midseason'] = 1
df.loc[(df['tc_date']>= '2011-02-01') & (df['tc_date'] < '2011-06-01'),'midseason'] = 1
df.loc[(df['tc_date']>= '2010-02-01') & (df['tc_date'] < '2010-06-01'),'midseason'] = 1
df.loc[(df['tc_date']>= '2009-02-01') & (df['tc_date'] < '2009-06-01'),'midseason'] = 1
df.loc[(df['tc_date']>= '2008-02-01') & (df['tc_date'] < '2008-06-01'),'midseason'] = 1
df.loc[(df['tc_date']>= '2007-02-01') & (df['tc_date'] < '2007-06-01'),'midseason'] = 1

df.midseason.fillna(0,inplace=True)

Assigning_REV_conditions = np.logical_and( df.progcode == "REV", df.year == 2011)
df["model_ind"][Assigning_REV_conditions]=1

BSH_assign_condition = np.all(np.array([df.progcode == "BSH"]),axis=0)
df["model_ind"][BSH_assign_condition]=1
df["new_series"][BSH_assign_condition]=1
SFE_assign_condition = np.all(np.array([df.progcode == "SFE"]),axis=0)
df["model_ind"][SFE_assign_condition]=1
df["new_series"][SFE_assign_condition]=1
MVS_assign_condition = np.all(np.array([df.progcode == "MVS"]),axis=0)
df["model_ind"][MVS_assign_condition]=1
df["new_series"][MVS_assign_condition]=1
HGM_assign_condition = np.all(np.array([df.progcode == "HGM"]),axis=0)
df["model_ind"][HGM_assign_condition]=1
df["new_series"][HGM_assign_condition]=1
CRS_assign_condition = np.all(np.array([df.progcode == "CRS"]),axis=0)
df["model_ind"][CRS_assign_condition]=1
df["new_series"][CRS_assign_condition]=1
FRV_assign_condition = np.all(np.array([df.progcode == "FRV"]),axis=0)
df["model_ind"][FRV_assign_condition]=1
df["new_series"][FRV_assign_condition]=1
MGM_assign_condition = np.all(np.array([df.progcode == "MGM"]),axis=0)
df["model_ind"][MGM_assign_condition]=1
df["new_series"][MGM_assign_condition]=1
MIX_assign_condition = np.all(np.array([df.progcode == "MIX"]),axis=0)
df["model_ind"][MIX_assign_condition]=1
df["new_series"][MIX_assign_condition]=1
RES_assign_condition = np.all(np.array([df.progcode == "RES"]),axis=0)
df["model_ind"][RES_assign_condition]=1
df["new_series"][RES_assign_condition]=1

DFY_condition = np.logical_and( df.progcode == 'DFY',  df.season == 2008   )
df = df[~DFY_condition]

SCO_condition = np.logical_and( df.progcode == 'SCO',  df.season == 2009   )
df = df[~SCO_condition]
df['Lnc3'] = np.log(df['c3'])
df['LnLeadin'] = np.log(df['leadin_prev_halfhour'])
df['Ln_PctAware'] = np.log(df['awn_all_pctaware'])

df['Ln_PctAwareUnaided'] = np.log(df['awn_all_pctawareunaided'])

df['Ln_Top2Box_AmgTtl'] = np.log(df['awn_all_top2box_amgttl'])


df['Day1'] = df.dow=='M'
df['Day1'] = df.Day1.astype(int)

df['Day2'] = df.dow=='TU'
df['Day2'] = df.Day2.astype(int)

df['Day3'] = df.dow=='W'
df['Day3'] = df.Day3.astype(int)

df['Day4'] = df.dow=='TH'
df['Day4'] = df.Day4.astype(int)

df['Day5'] = df.dow=='F'
df['Day5'] = df.Day5.astype(int)

df['Day6'] = df.dow=='SA'
df['Day6'] = df.Day6.astype(int)

df['Day7'] = df.dow=='SU'
df['Day7'] = df.Day7.astype(int)

df['Time1'] = df.cor_time=='20:00:00'
df['Time1'] = df.Time1.astype(int)

df['Time2'] = df.cor_time=='20:30:00'
df['Time2'] = df.Time2.astype(int)

df['Time3'] = df.cor_time=='21:00:00'
df['Time3'] = df.Time3.astype(int)

df['Time4'] = df.cor_time=='21:30:00'
df['Time4'] = df.Time4.astype(int)

df['Time5'] = df.cor_time=='22:00:00'
df['Time5'] = df.Time5.astype(int)
df['Time6'] = df.cor_time=='22:30:00'
df['Time6'] = df.Time6.astype(int)
df['Time7'] = df.cor_time=='23:00:00'
df['Time7'] = df.Time7.astype(int)
df['Time8'] = df.cor_time=='23:30:00'
df['Time8'] = df.Time8.astype(int)

df['IsDrama'] = (df.prog_type=='Drama') | (df.prog_type=='Comedy/Drama')
df['IsDrama'] = df.IsDrama.astype(int)
df['IsReality'] = (df.prog_type=='Reality')
df['IsReality'] = df.IsReality.astype(int)
df['IsComedy'] = (df.prog_type=='Comedy') | (df.prog_type=='Comedy/Drama') 
df['IsComedy'] = df.IsComedy.astype(int)

df['season07'] = df.season==2007
df['season07'] = df.season07.astype(int)
df['season08'] = df.season==2008
df['season08'] = df.season08.astype(int)
df['season09'] = df.season==2009
df['season09'] = df.season09.astype(int)
df['season10'] = df.season==2010
df['season10'] = df.season10.astype(int)
df['season11'] = df.season==2011
df['season11'] = df.season11.astype(int)
df['season12'] = df.season==2012
df['season12'] = df.season12.astype(int)
df['season13'] = df.season==2013
df['season13'] = df.season13.astype(int)
df['season14'] = df.season==2014
df['season14'] = df.season14.astype(int)



df['Wed10pm']=df.Day3 * df.Time5
df['Wed10pm'] = df.Wed10pm.astype(int)
df['Thu8pm']=df.Day4 * df.Time1
df['Thu8pm'] = df.Thu8pm.astype(int)
df['Sun10pm']=df.Day7 * df.Time5
df['Sun10pm'] = df.Sun10pm.astype(int)




# In[34]:




# In[32]:




# In[ ]:



