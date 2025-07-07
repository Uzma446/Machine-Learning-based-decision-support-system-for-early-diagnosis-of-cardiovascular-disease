import pandas as pd
from pandas import read_excel
import numpy as np
from pandas import DataFrame
from tabulate import tabulate
import xlrd
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


d = pd.read_excel('Partial_PatientData1.xlsx', index_col=0)
df = pd.DataFrame(d)
df = df.apply(pd.to_numeric, errors='coerce')
loc = df.iloc[:, 5:6]
y1 = len(df.index)
cg = df.groupby('Disease label')
# dataset of MI
data = cg.get_group(1)
rows_of_MI = len(data.index)
data1 = cg.get_group(2)
rows_of_Angina = len(data1.index)
data2 = cg.get_group(3)
rows_of_SI = len(data2.index)
data3 = cg.get_group(4)
rows_of_NCCP = len(data3.index)

# probability_of_MI_hypo
pH1 = rows_of_MI / y1
# probability of Angina hypo
pH2 = rows_of_Angina / y1
# probability of SI hypo
pH3 = rows_of_SI / y1
# probability of NCCP hypo
pH4 = rows_of_NCCP / y1

# calculating parametric values of MI
BP = data.iloc[:, 1:3]
HR = data.iloc[:, 4:5]
ECG = data.iloc[:, 5:6]
Oxygen = data.iloc[:, 3:4]
High = BP[(BP['Resting BP Upper Limit'] > 129) | (BP['Resting BP Lower Limit'] > 80)]
Elevated = BP[((BP['Resting BP Upper Limit'] >= 120) & (BP['Resting BP Upper Limit'] <= 129) & (
            BP['Resting BP Lower Limit'] <= 80))]
Normal = BP[((BP['Resting BP Upper Limit'] >= 90) & (BP['Resting BP Upper Limit'] < 120) & (
            BP['Resting BP Lower Limit'] <= 80))]
Low = BP[((BP['Resting BP Upper Limit'] < 90) | (BP['Resting BP Upper Limit'] < 60))]
A = [Low, Normal, Elevated, High]
E1H1 = []

for i in A:
    A1 = len(i.index)
    pT = A1 / rows_of_MI
    E1H1.append(pT)
lowOxy = Oxygen[Oxygen['Oxygen saturation'] < 85]
ModerateOxy = Oxygen[(Oxygen['Oxygen saturation'] >= 85) & (Oxygen['Oxygen saturation'] <= 94)]
NormalOxy = Oxygen[(Oxygen['Oxygen saturation'] >= 95)]
B = [lowOxy, ModerateOxy, NormalOxy]
E2H1 = []

for i in B:
    B1 = len(i.index)
    pT_Oxy = B1 / rows_of_MI
    E2H1.append(pT_Oxy)
normal_ecg = ECG[ECG['Resting ECG transformed'] == 1]
left_ecg = ECG[ECG['Resting ECG transformed'] == 2]
ST_ecg = ECG[ECG['Resting ECG transformed'] == 3]
abnormal = ECG[ECG['Resting ECG transformed'] == 4]
n1 = len(normal_ecg.index)
l1 = len(left_ecg.index)
st1 = len(ST_ecg.index)
ab1 = len(abnormal.index)
pT1_ecg = n1 / rows_of_MI
pT2_ecg = l1 / rows_of_MI
pT3_ecg = st1 / rows_of_MI
pT4_ecg = ab1 / rows_of_MI
E4H1 = [pT1_ecg, pT2_ecg, pT3_ecg, pT4_ecg]

high_range = HR[HR['Heart rate'] > 100]
elevated_range = HR[(HR['Heart rate'] >= 90) & (HR['Heart rate'] <= 100)]
normal_range = HR[(HR['Heart rate'] >= 50) & (HR['Heart rate'] < 90)]
Athletic_range = HR[(HR['Heart rate'] >= 35) & (HR['Heart rate'] < 50)]
low_range = HR[HR['Heart rate'] < 35]
ListMI = [low_range, Athletic_range, normal_range, elevated_range, high_range]
E3H1 = []
for i in ListMI:
    C = len(i.index)
    pT_hr = C / rows_of_MI
    E3H1.append(pT_hr)
# dataset of Angina----------------------------------------------------------------------------------------
# calculating parametric values of Angina
BP1 = data1.iloc[:, 1:3]
HR1 = data1.iloc[:, 4:5]
ECG1 = data1.iloc[:, 5:6]
Oxygen1 = data1.iloc[:, 3:4]
High1 = BP1[(BP1['Resting BP Upper Limit'] > 129) | (BP1['Resting BP Lower Limit'] > 80)]
Elevated1 = BP1[((BP1['Resting BP Upper Limit'] >= 120) & (BP1['Resting BP Upper Limit'] <= 129) & (
            BP1['Resting BP Lower Limit'] <= 80))]
Normal1 = BP1[((BP1['Resting BP Upper Limit'] >= 90) & (BP1['Resting BP Upper Limit'] < 120) & (
            BP1['Resting BP Lower Limit'] <= 80))]
Low1 = BP1[((BP1['Resting BP Upper Limit'] < 90) | (BP1['Resting BP Upper Limit'] < 60))]
A1 = [Low1, Normal1, Elevated1, High1]
E1H2 = []
for i in A1:
    a = len(i.index)
    pT1 = a / rows_of_Angina
    E1H2.append(pT1)

lowOxy1 = Oxygen1[Oxygen1['Oxygen saturation'] < 85]
ModerateOxy1 = Oxygen1[(Oxygen1['Oxygen saturation'] >= 85) & (Oxygen1['Oxygen saturation'] <= 94)]
NormalOxy1 = Oxygen1[(Oxygen1['Oxygen saturation'] >= 95)]
B1 = [lowOxy1, ModerateOxy1, NormalOxy1]
E2H2 = []
for i in B1:
    B1 = len(i.index)
    pT_Oxy1 = B1 / rows_of_Angina
    E2H2.append(pT_Oxy1)
normal_ecg1 = ECG1[ECG1['Resting ECG transformed'] == 1]
left_ecg1 = ECG1[ECG1['Resting ECG transformed'] == 2]
ST_ecg1 = ECG1[ECG1['Resting ECG transformed'] == 3]
abnormal1 = ECG1[ECG1['Resting ECG transformed'] == 4]
n2 = len(normal_ecg1.index)
l2 = len(left_ecg1.index)
st2 = len(ST_ecg1.index)
ab2 = len(abnormal1.index)
pT1_ecg1 = n2 / rows_of_Angina
pT2_ecg1 = l2 / rows_of_Angina
pT3_ecg1 = st2 / rows_of_Angina
pT4_ecg1 = ab2 / rows_of_Angina
E4H2 = [pT1_ecg1, pT2_ecg1, pT3_ecg1, pT4_ecg1]

high_range1 = HR1[HR1['Heart rate'] > 100]
elevated_range1 = HR1[(HR1['Heart rate'] >= 90) & (HR1['Heart rate'] <= 100)]
normal_range1 = HR1[(HR1['Heart rate'] >= 50) & (HR1['Heart rate'] < 90)]
Athletic_range1 = HR1[(HR1['Heart rate'] >= 35) & (HR1['Heart rate'] < 50)]
low_range1 = HR1[HR1['Heart rate'] < 35]
ListAngina = [low_range1, Athletic_range1, normal_range1, elevated_range1, high_range1]
E3H2 = []

for i in ListAngina:
    k1 = len(i.index)
    pT_hr1 = k1 / rows_of_Angina
    E3H2.append(pT_hr1)
##dataset of SI----------------------------------------------------------------------------------------
# calculating parametric values of SI
BP2 = data2.iloc[:, 1:3]
HR2 = data2.iloc[:, 4:5]
ECG2 = data2.iloc[:, 5:6]
Oxygen2 = data2.iloc[:, 3:4]
High2 = BP2[(BP2['Resting BP Upper Limit'] > 129) | (BP2['Resting BP Lower Limit'] > 80)]
Elevated2 = BP2[((BP2['Resting BP Upper Limit'] >= 120) & (BP2['Resting BP Upper Limit'] <= 129) & (
            BP2['Resting BP Lower Limit'] <= 80))]
Normal2 = BP2[((BP2['Resting BP Upper Limit'] >= 90) & (BP2['Resting BP Upper Limit'] < 120) & (
            BP2['Resting BP Lower Limit'] <= 80))]
Low2 = BP2[((BP2['Resting BP Upper Limit'] < 90) | (BP2['Resting BP Upper Limit'] < 60))]
A2 = [Low2, Normal2, Elevated2, High2]
E1H3 = []

for i in A2:
    a2 = len(i.index)
    pT2 = a2 / rows_of_SI
    E1H3.append(pT2)
lowOxy2 = Oxygen2[Oxygen2['Oxygen saturation'] < 85]
ModerateOxy2 = Oxygen2[(Oxygen2['Oxygen saturation'] >= 85) & (Oxygen2['Oxygen saturation'] <= 94)]
NormalOxy2 = Oxygen2[(Oxygen2['Oxygen saturation'] >= 95)]
B2 = [lowOxy2, ModerateOxy2, NormalOxy2]
E2H3 = []

for i in B2:
    B2 = len(i.index)
    pT_Oxy2 = B2 / rows_of_SI
    E2H3.append(pT_Oxy2)
normal_ecg2 = ECG2[ECG2['Resting ECG transformed'] == 1]
left_ecg2 = ECG2[ECG2['Resting ECG transformed'] == 2]
ST_ecg2 = ECG2[ECG2['Resting ECG transformed'] == 3]
abnormal2 = ECG2[ECG2['Resting ECG transformed'] == 4]
n3 = len(normal_ecg2.index)
l3 = len(left_ecg2.index)
st3 = len(ST_ecg2.index)
ab3 = len(abnormal2.index)
pT1_ecg2 = n3 / rows_of_SI
pT2_ecg2 = l3 / rows_of_SI
pT3_ecg2 = st3 / rows_of_SI
pT4_ecg2 = ab3 / rows_of_SI
E4H3 = [pT1_ecg2, pT2_ecg2, pT3_ecg2, pT4_ecg2]

high_range2 = HR2[HR2['Heart rate'] > 100]
elevated_range2 = HR2[(HR2['Heart rate'] >= 90) & (HR2['Heart rate'] <= 100)]
normal_range2 = HR2[(HR2['Heart rate'] >= 50) & (HR2['Heart rate'] < 90)]
Athletic_range2 = HR2[(HR2['Heart rate'] >= 35) & (HR2['Heart rate'] < 50)]
low_range2 = HR2[HR2['Heart rate'] < 35]
ListSI = [low_range2, Athletic_range2, normal_range2, elevated_range2, high_range2]

E3H3 = []
for i in ListSI:
    si = len(i.index)
    pT_hr2 = si / rows_of_SI
    E3H3.append(pT_hr2)
# dataset of NCCP
# calculating parametric values of NCCP------------------------------------------------------------------------
BP3 = data3.iloc[:, 1:3]
HR3 = data3.iloc[:, 4:5]
ECG3 = data3.iloc[:, 5:6]
Oxygen3 = data3.iloc[:, 3:4]
High3 = BP3[(BP3['Resting BP Upper Limit'] > 129) | (BP3['Resting BP Lower Limit'] > 80)]
Elevated3 = BP3[((BP3['Resting BP Upper Limit'] >= 120) & (BP3['Resting BP Upper Limit'] <= 129) & (
            BP3['Resting BP Lower Limit'] <= 80))]
Normal3 = BP3[((BP3['Resting BP Upper Limit'] >= 90) & (BP3['Resting BP Upper Limit'] < 120) & (
            BP3['Resting BP Lower Limit'] <= 80))]
Low3 = BP3[((BP3['Resting BP Upper Limit'] < 90) | (BP3['Resting BP Upper Limit'] < 60))]
A3 = [Low3, Normal3, Elevated3, High3]
E1H4 = []

for i in A3:
    a3 = len(i.index)
    pT3 = a3 / rows_of_NCCP
    E1H4.append(pT3)
lowOxy3 = Oxygen3[Oxygen3['Oxygen saturation'] < 85]
ModerateOxy3 = Oxygen3[(Oxygen3['Oxygen saturation'] >= 85) & (Oxygen3['Oxygen saturation'] <= 94)]
NormalOxy3 = Oxygen3[(Oxygen3['Oxygen saturation'] >= 95)]
B3 = [lowOxy3, ModerateOxy3, NormalOxy3]
E2H4 = []

for i in B3:
    B3 = len(i.index)
    pT_Oxy3 = B3 / rows_of_NCCP
    E2H4.append(pT_Oxy3)
normal_ecg3 = ECG3[ECG3['Resting ECG transformed'] == 1]
left_ecg3 = ECG3[ECG3['Resting ECG transformed'] == 2]
ST_ecg3 = ECG3[ECG3['Resting ECG transformed'] == 3]
abnormal3 = ECG3[ECG3['Resting ECG transformed'] == 4]
n4 = len(normal_ecg3.index)
l4 = len(left_ecg3.index)
st4 = len(ST_ecg3.index)
ab4 = len(abnormal3.index)
pT1_ecg3 = n4 / rows_of_NCCP
pT2_ecg3 = l4 / rows_of_NCCP
pT3_ecg3 = st4 / rows_of_NCCP
pT4_ecg3 = ab4 / rows_of_NCCP
E4H4 = [pT1_ecg3, pT2_ecg3, pT3_ecg3, pT4_ecg3]

high_range3 = HR3[HR3['Heart rate'] > 100]
elevated_range3 = HR3[(HR3['Heart rate'] >= 90) & (HR3['Heart rate'] <= 100)]
normal_range3 = HR3[(HR3['Heart rate'] >= 50) & (HR3['Heart rate'] < 90)]
Athletic_range3 = HR3[(HR3['Heart rate'] >= 35) & (HR3['Heart rate'] < 50)]
low_range3 = HR3[HR3['Heart rate'] < 35]
ListNCCP = [low_range3, Athletic_range3, normal_range3, elevated_range3, high_range3]

E3H4 = []
for i in ListNCCP:
    n = len(i.index)
    pT_hr3 = n / rows_of_NCCP
    E3H4.append(pT_hr3)


@app.route('/', methods=['POST'])
def getvalue():
    OV = request.form['OV']
    ECG = request.form['ECG']
    HRV = request.form['HRV']
    UBP = request.form['UBP']
    LBP = request.form['LBP']

    OXV = int(OV) #my[0][2]
    ECGV = int(ECG) #my[0][4]
    HR = int(HRV) #my[0][3]
    BPU = int(UBP) #my[0][0]
    BPL = int(LBP) #my[0][1]

    if BPU > 129 or BPL > 80:  # High BP range
        # print('high')
        y = 3
        mi_bp = E1H1[y]
        an_bp = E1H2[y]
        si_bp = E1H3[y]
        nc_bp = E1H4[y]
    elif (BPU >= 120 and BPU <= 129) and (BPL <= 80):  # Elevated BP range
        # print('Elevated')
        y = 2
        mi_bp = E1H1[y]
        an_bp = E1H2[y]
        si_bp = E1H3[y]
        nc_bp = E1H4[y]
    elif (BPU >= 90 and BPU < 120) and BPL <= 80:  # Normal BP range
        # print('Normal')
        y = 1
        mi_bp = E1H1[y]
        an_bp = E1H2[y]
        si_bp = E1H3[y]
        nc_bp = E1H4[y]
    else:  # Low BP range
        # print('low')
        y = 0
        mi_bp = E1H1[y]
        an_bp = E1H2[y]
        si_bp = E1H3[y]
        nc_bp = E1H4[y]

        # Oximeter values
    if OXV >= 95:  # normal range
        # print('Normal')
        y = 2
        mi_oxi = E2H1[y]
        an_oxi = E2H2[y]
        si_oxi = E2H3[y]
        nc_oxi = E2H4[y]
    elif OXV >= 85 and OXV <= 94:  # Moderate range
        # print('Moderate')
        y = 1
        mi_oxi = E2H1[y]
        an_oxi = E2H2[y]
        si_oxi = E2H3[y]
        nc_oxi = E2H4[y]
    else:  # low range
        # print('low')
        y = 0
        mi_oxi = E2H1[y]
        an_oxi = E2H2[y]
        si_oxi = E2H3[y]
        nc_oxi = E2H4[y]
    if HR > 100:  # high range
        # print('high')
        y = 4
        mi_hr = E3H1[y]
        an_hr = E3H2[y]
        si_hr = E3H3[y]
        nc_hr = E3H4[y]
    elif HR >= 90 and HR <= 100:  # elevated range
        # print('elevated')
        y = 3
        mi_hr = E3H1[y]
        an_hr = E3H2[y]
        si_hr = E3H3[y]
        nc_hr = E3H4[y]
    elif HR >= 50 and HR < 90:  # normal range
        # print('Normal')
        y = 2
        mi_hr = E3H1[y]
        an_hr = E3H2[y]
        si_hr = E3H3[y]
        nc_hr = E3H4[y]
    elif HR >= 35 and HR < 50:  # Athletic range
        # print('Athletic')
        y = 1
        mi_hr = E3H1[y]
        an_hr = E3H2[y]
        si_hr = E3H3[y]
        nc_hr = E3H4[y]
    else:  # low range
        # print('low')
        y = 0
        mi_hr = E3H1[y]
        an_hr = E3H2[y]
        si_hr = E3H3[y]
        nc_hr = E3H4[y]
    if ECGV == 1:
        y = 0
        mi_ecg = E4H1[y]
        an_ecg = E4H2[y]
        si_ecg = E4H3[y]
        nc_ecg = E4H4[y]
    elif ECGV == 2:
        y = 1
        mi_ecg = E4H1[y]
        an_ecg = E4H2[y]
        si_ecg = E4H3[y]
        nc_ecg = E4H4[y]
    elif ECGV == 3:
        y = 2
        mi_ecg = E4H1[y]
        an_ecg = E4H2[y]
        si_ecg = E4H3[y]
        nc_ecg = E4H4[y]
    elif ECGV == 4:
        y = 3
        mi_ecg = E4H1[y]
        an_ecg = E4H2[y]
        si_ecg = E4H3[y]
        nc_ecg = E4H4[y]

    probH1 = mi_bp * mi_oxi * mi_hr * mi_ecg * pH1
    probH2 = an_bp * an_oxi * an_hr * an_ecg * pH2
    probH3 = si_bp * si_oxi * si_hr * si_ecg * pH3
    probH4 = nc_bp * nc_oxi * nc_hr * nc_ecg * pH4

    if (probH1 > probH2) and (probH1 > probH3) and (probH1 > probH4):
        print1 = "MI"
        print2 = probH1
    elif (probH2 > probH1) and (probH2 > probH3) and (probH2 > probH4):
        print1 = "Angina"
        print2 = probH2
    elif (probH3 > probH1) and (probH3 > probH2) and (probH3 > probH4):
        print1 = "SI"
        print2 = probH3
    elif (probH4 > probH1) and (probH4 > probH2) and (probH4 > probH3):
        print1 = "NCCP"
        print2 = probH4


    return render_template('Pass.html', Print1=print1, Print2=print2)
if __name__ == '__main__':
    app.run()
