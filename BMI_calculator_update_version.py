# Import pandas library
import pandas as pd


inputData = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]


# initialize list
data = []
Health_Risk = ''
BMI_Category = ''
for item in inputData:
    BMI = item['WeightKg'] / (item['HeightCm'] / 100) ** 2  
    if BMI <= 18.4:
        BMI_Category = 'Underweight'
        Health_Risk = 'Malnutrition risk'
    elif 18.5 <= BMI <= 24.9:
        BMI_Category = 'normal weight'
        Health_Risk = 'low risk'
    elif 25 <= BMI <= 29.9:
        BMI_Category = 'Overweight'
        Health_Risk = 'enhanced risk'
    elif 30 <= BMI <= 34.9:
        BMI_Category = 'Moderately obese'
        Health_Risk = 'Medium risk'
    elif 35 <= BMI <= 39.9:
        BMI_Category = 'Severely obese'
        Health_Risk = 'High risk'
    elif BMI >= 40:
        BMI_Category = 'very severely obese'
        Health_Risk = 'very high risk'
    Gender = item['Gender']
    HeightCm = item['HeightCm']
    WeightKg = item['WeightKg']
    data.append([Gender,HeightCm, WeightKg, BMI, BMI_Category, Health_Risk])
   

# Create the pandas DataFrame
df = pd.DataFrame(data, columns = ['Gender', 'HeightCm', 'WeightKg','BMI', 'BMI Category', 'Health Risk'])
# saving the dataframe
df.to_csv('BMI.csv')
print(df)

def overweight_count(data):
    count_overweight = 0
    for item in data:
        if item[4] == 'Overweight':
            count_overweight += 1
    return count_overweight

print(overweight_count(data))



