import os
import pandas as pd
import matplotlib.pyplot as plt

# Get the current path
current_path = os.getcwd()

# Join paths to create the full file path
file_path = os.path.join(current_path, "Lab06", "travel.csv")

# Load the data from the CSV file
data = pd.read_csv(file_path)

# Display the first few rows of the data
print("All data:")
print(data.head())

# Print the column names to check if they are correct
print("Column names:")
print(data.columns)

# Cleaning column names (if needed)
data.columns = data.columns.str.strip()

# Check if 'Lat' and 'Lng' columns exist
if 'Lat' not in data.columns or 'Lng' not in data.columns:
    print("Columns 'Lat' and 'Lng' not found in the data.")
else:
    # Plotting the points
    plt.figure(figsize=(8, 6))
    plt.scatter(data['Lat'], data['Lng'], color='blue')  # Points in blue

    # Adding labels to the points with slight offsets
    for i, row in data.iterrows():
        plt.text(row['Lat'] + 0.01, row['Lng'] + 0.01, f"T{i+1}", fontsize=9)

    # Define the order in which to connect the points
    order = [1, 5, 3, 6, 7, 4, 8, 2, 9, 10, 1]  # Specified order (1-based index)

    # Subtract 1 from each element in the order to convert to 0-based index
    order = [x - 1 for x in order]

    # Extract Lat and Lng in the specified order
    latitudes = data['Lat'].iloc[order]
    longitudes = data['Lng'].iloc[order]

    # Draw a red line connecting the points
    plt.plot(latitudes, longitudes, color='red', linestyle='-', linewidth=2)

    # Plot the ordered points again to ensure they are visible on top
    plt.scatter(latitudes, longitudes, color='blue')  # Points in blue

    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.title('Route of Traveling Salesman Problem')
    plt.grid(True)
    plt.show()