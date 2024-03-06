from flask import Flask,jsonify,request
from flask_cors import CORS
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl 

app = Flask(__name__)
CORS(app)


# sample_data = {"message": "Server is up and running!sknf"}

# @app.route('/api/data', methods=['GET'])
# def get_data():
#     return jsonify(sample_data)


@app.route('/api/data',methods=['POST'])
def process_data():
    FruitWeight = ctrl.Antecedent(np.arange(79, 109, 1), 'FruitWeight')
    TSS = ctrl.Antecedent(np.arange(1, 25, 1), 'TSS')
    PH = ctrl.Antecedent(np.arange(3.8, 5.5, 0.1), 'PH')
    DietaryFiber = ctrl.Antecedent(np.arange(2, 2.70, 0.1), 'DietaryFiber')
    TotalFat = ctrl.Antecedent(np.arange(35, 51, 1), 'TotalFat')
    Firmness = ctrl.Antecedent(np.arange(20,46,1), 'Firmness')
    VitaminC = ctrl.Antecedent(np.arange(19, 26, 1), 'VitaminC')
    VitaminA = ctrl.Antecedent(np.arange(39, 53, 1), 'VitaminA')
    VitaminD = ctrl.Antecedent(np.arange(19,31,1), 'VitaminD')
    Sodium = ctrl.Antecedent(np.arange(7, 12, 0.1), 'Sodium')
    Iron = ctrl.Antecedent(np.arange(1, 10, 0.1), 'Iron')
    Calcium = ctrl.Antecedent(np.arange(3,11,0.1), 'Calcium')
    Potassium = ctrl.Antecedent(np.arange(300, 377, 1), 'Potassium')
    Ethylene = ctrl.Antecedent(np.arange(120,593,1), 'Ethylene')
    RipeningStage = ctrl.Consequent(np.arange(1, 120, 1), 'RipeningStage')
    



    FruitWeight['VVLFW'] = fuzz.trimf(FruitWeight.universe , [79 , 79 , 81])
    FruitWeight['VLFW'] = fuzz.trimf(FruitWeight.universe , [81 , 83 , 85])
    FruitWeight['LFW'] = fuzz.trimf(FruitWeight.universe , [83 , 85 , 90])
    FruitWeight['MFW'] = fuzz.trimf(FruitWeight.universe , [85 , 90 , 95])
    FruitWeight['SHFW']= fuzz.trimf(FruitWeight.universe , [90 , 95 , 100])
    FruitWeight['HFW'] = fuzz.trimf(FruitWeight.universe , [95 , 100 , 105])
    FruitWeight['VHFW'] = fuzz.trimf(FruitWeight.universe , [100 , 105 , 108])
    FruitWeight['VVHFW'] = fuzz.trimf(FruitWeight.universe , [105 , 108 , 108])
    
    

    TSS['VVLTSS'] = fuzz.trimf(TSS.universe , [1 , 1 , 3])
    TSS['VLTSS'] = fuzz.trimf(TSS.universe , [1 , 3 , 5])
    TSS['LTSS'] = fuzz.trimf(TSS.universe , [3 , 5 , 7])
    TSS['MTSS'] = fuzz.trimf(TSS.universe , [5 , 7 , 11])
    TSS['SHTSS'] = fuzz.trimf(TSS.universe , [7 , 11 , 15])
    TSS['HTSS'] = fuzz.trimf(TSS.universe , [11, 15, 19])
    TSS['VHTSS'] = fuzz.trimf(TSS.universe , [15 , 19 , 24])
    TSS['VVHTSS'] = fuzz.trimf(TSS.universe , [19 , 24 , 24])
    
    PH['VVLPH'] = fuzz.trimf(PH.universe , [3.8 , 3.8 , 4.0])
    PH['VLPH'] = fuzz.trimf(PH.universe , [3.8 , 4.0 , 4.2])
    PH['LPH'] = fuzz.trimf(PH.universe , [4.0 , 4.2 , 4.4])
    PH['MPH'] = fuzz.trimf(PH.universe , [4.2 , 4.4 , 4.6])
    PH['SHPH'] = fuzz.trimf(PH.universe , [4.4 , 4.6 , 4.9])
    PH['HPH'] = fuzz.trimf(PH.universe , [4.6 , 4.9 , 5.1])
    PH['VHPH'] = fuzz.trimf(PH.universe , [4.9 , 5.1 , 5.4])
    PH['VVHPH'] = fuzz.trimf(PH.universe , [5.1 , 5.4 , 5.4])
    
    DietaryFiber['VVLDF'] = fuzz.trimf(DietaryFiber.universe , [2 , 2 , 2.15])
    DietaryFiber['VLDF'] = fuzz.trimf(DietaryFiber.universe , [2 , 2.15 , 2.20])
    DietaryFiber['LDF'] = fuzz.trimf(DietaryFiber.universe , [2.15 , 2.20 , 2.30])
    DietaryFiber['MDF'] = fuzz.trimf(DietaryFiber.universe , [2.20 , 2.30 , 2.40])
    DietaryFiber['SHDF']= fuzz.trimf(DietaryFiber.universe , [2.30 , 2.40 , 2.45])
    DietaryFiber['HDF'] = fuzz.trimf(DietaryFiber.universe , [2.30 , 2.40 , 2.50])
    DietaryFiber['VHDF'] = fuzz.trimf(DietaryFiber.universe , [2.40 , 2.50 , 2.60])
    DietaryFiber['VVHDF'] = fuzz.trimf(DietaryFiber.universe , [2.50 , 2.60 , 2.60])
    
    TotalFat['VVLTF'] = fuzz.trimf(TotalFat.universe , [35 , 35 , 36])
    TotalFat['VLTF'] = fuzz.trimf(TotalFat.universe , [35 , 36 , 39])
    TotalFat['LTF'] = fuzz.trimf(TotalFat.universe , [36 , 39 , 41])
    TotalFat['MTF'] = fuzz.trimf(TotalFat.universe , [39 , 41 , 43])
    TotalFat['SHTF'] = fuzz.trimf(TotalFat.universe , [41 , 43 , 45])
    TotalFat['HTF'] = fuzz.trimf(TotalFat.universe , [41 , 43 , 47])
    TotalFat['VHTF'] = fuzz.trimf(TotalFat.universe , [43 , 47 , 51])
    TotalFat['VVHTF'] = fuzz.trimf(TotalFat.universe , [47 , 51 , 51])
    
    Firmness['VVLFr'] = fuzz.trimf(Firmness.universe , [20 , 20 , 25])
    Firmness['VLFr'] = fuzz.trimf(Firmness.universe , [20 , 25 , 27])
    Firmness['LFr'] = fuzz.trimf(Firmness.universe , [25 , 27 , 31])
    Firmness['MFr'] = fuzz.trimf(Firmness.universe , [27 , 31 , 35])
    Firmness['SHFr'] = fuzz.trimf(Firmness.universe , [31 , 35 , 39])
    Firmness['HFr'] = fuzz.trimf(Firmness.universe , [35 , 39 , 42])
    Firmness['VHFr'] = fuzz.trimf(Firmness.universe , [39 , 42 , 46])
    Firmness['VVHFr'] = fuzz.trimf(Firmness.universe , [42 , 46 , 46])
    
    VitaminC['VVLVC'] = fuzz.trimf(VitaminC.universe , [19, 19, 21])
    VitaminC['VLVC'] = fuzz.trimf(VitaminC.universe , [19, 21, 21.5])
    VitaminC['LVC'] = fuzz.trimf(VitaminC.universe , [21, 21.5, 22])
    VitaminC['MVC'] = fuzz.trimf(VitaminC.universe , [21.5, 22, 23])
    VitaminC['SHVC']= fuzz.trimf(VitaminC.universe , [22, 23, 23.5])
    VitaminC['HVC'] = fuzz.trimf(VitaminC.universe , [23, 23.5, 24])
    VitaminC['VHVC'] = fuzz.trimf(VitaminC.universe , [23.5, 24, 25])
    VitaminC['VVHVC'] = fuzz.trimf(VitaminC.universe , [24, 25, 25])
    
    VitaminA['VVLVA'] = fuzz.trimf(VitaminA.universe , [39, 39, 40])
    VitaminA['VLVA'] = fuzz.trimf(VitaminA.universe , [39, 40, 41])
    VitaminA['LVA'] = fuzz.trimf(VitaminA.universe , [40, 41, 43])
    VitaminA['MVA'] = fuzz.trimf(VitaminA.universe , [41, 43, 45])
    VitaminA['SHVA'] = fuzz.trimf(VitaminA.universe , [43, 45, 46])
    VitaminA['HVA'] = fuzz.trimf(VitaminA.universe , [45, 46, 47])
    VitaminA['VHVA'] = fuzz.trimf(VitaminA.universe , [46, 47, 52])
    VitaminA['VVHVA'] = fuzz.trimf(VitaminA.universe , [47 , 52 , 52])
    
    VitaminD['VVLVD'] = fuzz.trimf(VitaminD.universe , [19,19, 20])
    VitaminD['VLVD'] = fuzz.trimf(VitaminD.universe , [19, 20, 22])
    VitaminD['LVD'] = fuzz.trimf(VitaminD.universe , [20, 22, 25])
    VitaminD['MVD'] = fuzz.trimf(VitaminD.universe , [22, 25, 26])
    VitaminD['SHVD'] = fuzz.trimf(VitaminD.universe , [25, 26, 27])
    VitaminD['HVD'] = fuzz.trimf(VitaminD.universe , [26, 27, 29])
    VitaminD['VHVD'] = fuzz.trimf(VitaminD.universe , [27, 29, 31])
    VitaminD['VVHVD'] = fuzz.trimf(VitaminD.universe , [29, 31, 31])
    
    
    Sodium['VVLS'] = fuzz.trimf(Sodium.universe , [7, 8, 8.25])
    Sodium['VLS'] = fuzz.trimf(Sodium.universe , [8, 8.25, 8.5])
    Sodium['LS'] = fuzz.trimf(Sodium.universe , [8.25, 8.5, 9])
    Sodium['MS'] = fuzz.trimf(Sodium.universe , [8.5, 9, 9.5])
    Sodium['SHS']= fuzz.trimf(Sodium.universe , [9, 9.5, 9.7])
    Sodium['HS'] = fuzz.trimf(Sodium.universe , [9.5, 9.7, 10.25])
    Sodium['VHS'] = fuzz.trimf(Sodium.universe , [9.7, 10.25, 11])
    Sodium['VVHS'] = fuzz.trimf(Sodium.universe , [10.25, 11, 11])
    
    
    Iron['VVLI'] = fuzz.trimf(Iron.universe , [1, 2, 2.5])
    Iron['VLI'] = fuzz.trimf(Iron.universe , [2, 2.5, 3])
    Iron['LI'] = fuzz.trimf(Iron.universe , [2.5, 3, 4])
    Iron['MI'] = fuzz.trimf(Iron.universe , [3, 4, 5.5])
    Iron['SHI']= fuzz.trimf(Iron.universe , [4, 5.5, 5.7])
    Iron['HI'] = fuzz.trimf(Iron.universe , [5.5, 5.7, 6])
    Iron['VHI'] = fuzz.trimf(Iron.universe , [5.7, 6, 8.5])
    Iron['VVHI'] = fuzz.trimf(Iron.universe , [6, 8.5, 8.5])
    
    Calcium['VVLCA'] = fuzz.trimf(Calcium.universe , [3, 3, 4.5])
    Calcium['VLCA'] = fuzz.trimf(Calcium.universe , [3, 4.5, 5])
    Calcium['LCA'] = fuzz.trimf(Calcium.universe , [4.5, 5, 6])
    Calcium['MCA'] = fuzz.trimf(Calcium.universe , [5, 6, 7])
    Calcium['SHCA']= fuzz.trimf(Calcium.universe , [6, 7, 8])
    Calcium['HCA'] = fuzz.trimf(Calcium.universe , [7, 8, 9.75])
    Calcium['VHCA'] = fuzz.trimf(Calcium.universe , [8, 9.75, 11])
    Calcium['VVHCA'] = fuzz.trimf(Calcium.universe , [9.75, 11, 11])
    
    Potassium['VVLP'] = fuzz.trimf(Potassium.universe , [300, 300, 300.5])
    Potassium['VLP'] = fuzz.trimf(Potassium.universe , [300, 300.5, 301])
    Potassium['LP'] = fuzz.trimf(Potassium.universe , [300.5, 301, 305])
    Potassium['MP'] = fuzz.trimf(Potassium.universe , [301, 305, 307])
    Potassium['SHP']= fuzz.trimf(Potassium.universe , [305, 307, 315])
    Potassium['HP'] = fuzz.trimf(Potassium.universe , [307, 315, 325])
    Potassium['VHP'] = fuzz.trimf(Potassium.universe , [315, 325, 376])
    Potassium['VVHP'] = fuzz.trimf(Potassium.universe , [325, 376, 376])
    
    Ethylene['VVLE'] = fuzz.trimf(Ethylene.universe , [120 , 120 , 160])
    Ethylene['VLE'] = fuzz.trimf(Ethylene.universe , [120 , 160 , 200])
    Ethylene['LE'] = fuzz.trimf(Ethylene.universe , [160 , 200 , 240])
    Ethylene['ME'] = fuzz.trimf(Ethylene.universe , [200 , 240 , 350])
    Ethylene['SHE'] = fuzz.trimf(Ethylene.universe , [240 , 350 , 420])
    Ethylene['HE'] = fuzz.trimf(Ethylene.universe , [340 , 420 , 500])
    Ethylene['VHE'] = fuzz.trimf(Ethylene.universe , [420 , 500 , 595])
    Ethylene['VVHE'] = fuzz.trimf(Ethylene.universe , [500 , 595 , 595])
    
    
    RipeningStage['NR'] = fuzz.trimf(RipeningStage.universe , [0 , 0 , 30])
    RipeningStage['UR'] = fuzz.trimf(RipeningStage.universe , [0 , 30 , 40])
    RipeningStage['JR'] = fuzz.trimf(RipeningStage.universe , [30 , 40 , 50])
    RipeningStage['PR'] = fuzz.trimf(RipeningStage.universe , [40 , 50 , 65])
    RipeningStage['LR'] = fuzz.trimf(RipeningStage.universe , [50 , 65 , 90])
    RipeningStage['FR'] = fuzz.trimf(RipeningStage.universe , [75 , 100 , 105])
    RipeningStage['OR'] = fuzz.trimf(RipeningStage.universe , [100, 105, 110])
    RipeningStage['OOR'] = fuzz.trimf(RipeningStage.universe , [105 , 120 , 120])
    
    Rule1 = ctrl.Rule(FruitWeight['VVHFW'] & TSS['VVLTSS'] & PH['VVLPH'] & DietaryFiber['VVHDF'] & Firmness['VVHFr'] & TotalFat['VVLTF'] & VitaminC['VLVC'] & VitaminA['MVA'] & VitaminD['VLVD'] & Sodium['VVHS'] & Iron['VVLI'] & Calcium['VVLCA'] & Potassium['VVLP'] & Ethylene['VVLE'],RipeningStage['NR'])
    
    
    
    Rule2 = ctrl.Rule(FruitWeight['VHFW'] & TSS['VLTSS'] & PH['VLPH'] & DietaryFiber['VHDF'] & Firmness['VHFr'] & TotalFat['VLTF'] & VitaminC['MVC'] & VitaminA['HVA'] & VitaminD['VHVD'] & Sodium['VHS'] & Iron['VLI'] & Calcium['VLCA'] & Potassium['VLP'] & Ethylene['VLE'], RipeningStage['UR'])
    
    
    Rule3 = ctrl.Rule(FruitWeight['HFW'] & TSS['LTSS'] & PH['LPH'] & DietaryFiber['HDF'] & Firmness['HFr'] & TotalFat['LTF'] & VitaminC['MVC'] & VitaminA['MVA'] & VitaminD['MVD'] & Sodium['HS'] & Iron['LI'] & Calcium['LCA'] & Potassium['LP'] & Ethylene['ME']  ,RipeningStage['JR'])
    
    
    Rule4 = ctrl.Rule(FruitWeight['SHFW'] & TSS['MTSS'] & PH['MPH'] & DietaryFiber['SHDF'] & Firmness['SHFr'] & TotalFat['MTF'] & VitaminC['VVHVC'] & VitaminA['VVHVA'] & VitaminD['VHVD'] & Sodium['SHS'] & Iron['MI'] & Calcium['MCA'] & Potassium['MP'] & Ethylene['SHE'] ,RipeningStage['PR'])
    
    
    
    Rule5 = ctrl.Rule(FruitWeight['MFW'] & TSS['SHTSS'] & PH['SHPH'] & DietaryFiber['MDF'] & Firmness['MFr'] & TotalFat['SHTF'] & VitaminC['SHVC'] & VitaminA['SHVA'] & VitaminD['SHVD'] & Sodium['MS'] & Iron['SHI'] & Calcium['SHCA'] & Potassium['SHP'] & Ethylene['SHE'] ,RipeningStage['LR'])
    
    
    Rule6 = ctrl.Rule(FruitWeight['LFW'] & TSS['HTSS'] & PH['HPH'] & DietaryFiber['LDF'] & Firmness['LFr'] & TotalFat['HTF'] & VitaminC['VVLVC'] & VitaminA['VVLVA'] & VitaminD['VVLVD'] & Sodium['LS'] & Iron['HI'] & Calcium['HCA'] & Potassium['HP'] & Ethylene['HE'] ,RipeningStage['FR'])
    
    
    Rule7 = ctrl.Rule(FruitWeight['VLFW'] & TSS['VHTSS'] & PH['VHPH'] & DietaryFiber['VLDF'] & Firmness['VLFr'] & TotalFat['VHTF'] & VitaminC['HVC'] & VitaminA['VHVA'] & VitaminD['VHVD'] & Sodium['VLS'] & Iron['VHI'] & Calcium['VHCA'] & Potassium['VHP'] & Ethylene['VHE'] ,RipeningStage['OR'])
    
    
    Rule8 = ctrl.Rule(FruitWeight['VVLFW'] & TSS['VVHTSS'] & PH['VVHPH'] & DietaryFiber['VVLDF'] & Firmness['VVLFr'] & TotalFat['VVHTF'] & VitaminC['HVC'] & VitaminA['VVHVA'] & VitaminD['VVHVD'] & Sodium['VVLS'] & Iron['VVHI'] & Calcium['VVHCA'] & Potassium['VVHP'] & Ethylene['VVHE'] ,RipeningStage['OOR'])
    
    
    tipping = ctrl.ControlSystem([Rule1, Rule2, Rule3, Rule4, Rule5, Rule6,Rule7, Rule8])
    Tip =ctrl.ControlSystemSimulation(tipping)
    
    datans = request.get_json()

    input_fruit_weight = float(datans.get('Weight', 0))
    input_tss = float(datans.get('Tss', 0))
    input_ph = float(datans.get('Ph', 0))
    input_dietary_fiber = float(datans.get('DietaryFibre', 0))
    input_total_fat = float(datans.get('TotalFat', 0))
    input_firmness = float(datans.get('Firmness', 0))
    input_vitamin_c = float(datans.get('Vitamin_C', 0))
    input_vitamin_a = float(datans.get('Vitamin_A', 0))
    input_vitamin_d = float(datans.get('Vitamin_D', 0))
    input_sodium = float(datans.get('Sodium', 0))
    input_iron = float(datans.get('Iron', 0))
    input_calcium = float(datans.get('Calcium', 0))
    input_potassium = float(datans.get('Potassium', 0))
    input_ethylene = float(datans.get('Ethylene', 0))

    print(input_fruit_weight)
    print(input_tss)
    print(input_ph)
    print(input_dietary_fiber)
    print(input_total_fat)
    print(input_firmness)
    print(input_vitamin_c)
    print(input_vitamin_d)

    Tip.input['FruitWeight'] = input_fruit_weight
    Tip.input['TSS'] = input_tss
    Tip.input['PH'] = input_ph
    Tip.input['DietaryFiber'] = input_dietary_fiber
    Tip.input['TotalFat'] = input_total_fat
    Tip.input['Firmness'] = input_firmness
    Tip.input['VitaminC'] = input_vitamin_c
    Tip.input['VitaminA'] = input_vitamin_a
    Tip.input['VitaminD'] = input_vitamin_d
    Tip.input['Sodium'] = input_sodium
    Tip.input['Iron'] = input_iron
    Tip.input['Calcium'] = input_calcium
    Tip.input['Potassium'] = input_potassium
    Tip.input['Ethylene'] = input_ethylene
   
    Tip.compute()
    

    ans = Tip.output['RipeningStage']


    data = {
        "message" : ans
    }

    return jsonify(data) 


if __name__ == '__main__':
    app.run(host= '127.0.0.1' ,debug=True)