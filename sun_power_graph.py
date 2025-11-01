import numpy as np
import matplotlib.pyplot as plt

# Constants
S0 = 1361  # Solar constant in W/m^2

# Function to calculate solar declination angle
def solar_declination(day_of_year):
    return 46 * np.sin(np.deg2rad(360 / 365 * (day_of_year - 81)))

# Function to calculate solar radiation per unit area
def solar_radiation(latitude, day_of_year, hour):
    delta = solar_declination(day_of_year)
    latitude_rad = np.deg2rad(latitude)
    delta_rad = np.deg2rad(delta)
    hour_angle = np.deg2rad(15 * (hour - 12))
    
    cos_zenith = (np.sin(latitude_rad) * np.sin(delta_rad) + 
                  np.cos(latitude_rad) * np.cos(delta_rad) * np.cos(hour_angle))
    
    return S0 * np.maximum(0, cos_zenith)

# Define parameters
latitude = 46  # Fixed latitude at 23.45 degrees
days = np.linspace(1, 365, 365)  # Days of the year from 1 to 365
hours = np.linspace(0, 24, 100)  # Hours of the day from 0 to 24

# Create meshgrid for days and hours
D, H = np.meshgrid(days, hours)

# Calculate solar radiation for each combination of day and hour
I = solar_radiation(latitude, D, H)

# Plotting
plt.figure(figsize=(12, 6))
cp = plt.contourf(D, H, I, cmap='hot', levels=100)
plt.colorbar(cp, label='Solar Radiation (W/m^2)')
plt.title('Solar Radiation per Unit Area at Latitude 46°')
plt.xlabel('Day of the Year')
plt.ylabel('Hour of the Day')
plt.show()