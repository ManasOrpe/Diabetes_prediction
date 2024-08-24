import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import tkinter as tk
from tkinter import messagebox


dataset_path = "D:\Sem 6\Machine Learning  Algo\Project\diabetes.csv"
df = pd.read_csv(dataset_path)

X = df.drop('Outcome', axis=1)
y = df['Outcome']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


rf_classifier = RandomForestClassifier()


rf_classifier.fit(X_train, y_train)
print(rf_classifier.score(X_test,y_test))

def predict_diabetes():
    pregnancies = float(pregnancies_entry.get())
    glucose = float(glucose_entry.get())
    blood_pressure = float(blood_pressure_entry.get())
    skin_thickness = float(skin_thickness_entry.get())
    insulin = float(insulin_entry.get())\
        
    bmi = float(bmi_entry.get())
    diabetes_pedigree_function = float(diabetes_pedigree_function_entry.get())
    age = float(age_entry.get())
    
    
    prediction = rf_classifier.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
    
    if prediction[0] == 1:
        messagebox.showinfo("Prediction", "The patient is likely to have diabetes.")
    else:
        messagebox.showinfo("Prediction", "The patient is unlikely to have diabetes.")


root = tk.Tk()
root.title("Diabetes Prediction")


tk.Label(root, text="Pregnancies:").grid(row=0)
tk.Label(root, text="Glucose:").grid(row=1)
tk.Label(root, text="Blood Pressure:").grid(row=2)
tk.Label(root, text="Skin Thickness:").grid(row=3)
tk.Label(root, text="Insulin:").grid(row=4)
tk.Label(root, text="BMI:").grid(row=5)
tk.Label(root, text="Diabetes Pedigree Function:").grid(row=6)
tk.Label(root, text="Age:").grid(row=7)


pregnancies_entry = tk.Entry(root)
pregnancies_entry.grid(row=0, column=1)
glucose_entry = tk.Entry(root)
glucose_entry.grid(row=1, column=1)
blood_pressure_entry = tk.Entry(root)
blood_pressure_entry.grid(row=2, column=1)
skin_thickness_entry = tk.Entry(root)
skin_thickness_entry.grid(row=3, column=1)
insulin_entry = tk.Entry(root)
insulin_entry.grid(row=4, column=1)
bmi_entry = tk.Entry(root)
bmi_entry.grid(row=5, column=1)
diabetes_pedigree_function_entry = tk.Entry(root)
diabetes_pedigree_function_entry.grid(row=6, column=1)
age_entry = tk.Entry(root)
age_entry.grid(row=7, column=1)

predict_button = tk.Button(root, text="Predict", command=predict_diabetes)
predict_button.grid(row=8, columnspan=2)

root.mainloop()
