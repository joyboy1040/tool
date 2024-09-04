import pandas as pd
import matplotlib.pyplot as plt

def process_and_plot(df):
    # Initialize lists
    DataPoints = df['Data_Points'].tolist()
    Deformation = df['Deformation'].tolist()
    AngleList = []

    # Calculate the angle and create AngleList
    lengthOfData = len(DataPoints)
    angle = 360 / (lengthOfData - 1)
    angleSum = 0

    for i in range(lengthOfData):
        AngleList.append(angleSum)
        angleSum += angle

    # Create a new DataFrame with the calculated data
    data_dict = {
        'DataPoints': DataPoints,
        'Deformation': Deformation,
        'AngleList': AngleList,
    }
    new_df = pd.DataFrame(data_dict)

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(new_df['AngleList'], new_df['Deformation'], marker='o')
    plt.xlabel("Angle (Degrees)", fontsize=16)
    plt.ylabel("Deformations (in Inch)", fontsize=16)
    
    plt.grid(True)
    plt.xticks(range(0, 400, 40))
    
    
    return new_df, plt
