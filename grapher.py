import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates


def plot_temp_data(timestamps, temps1, temps2):  
    plt.figure(figsize=(14, 7))

    # Plot temperatures
    plt.subplot(2, 1, 1)
    plt.plot(timestamps, temps1, label='Outside Temperature', color='blue', linestyle='-', marker='o')
    plt.plot(timestamps, temps2, label='Sensor Reading', color='green', linestyle='-', marker='o')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Temperature Over Time')
    plt.legend() 

    plt.tight_layout()
    plt.xticks(rotation=45) 

    plt.savefig("temperature_plot.png")
    plt.close() 


def plot_hum_data(timestamps, hums1, hums2):  
    plt.figure(figsize=(14, 7)) 
    plt.subplot(2, 1, 1)
    plt.plot(timestamps, hums1, label='Outside Humidity', color='blue', linestyle='-', marker='o')
    plt.plot(timestamps, hums2, label='Sensor Reading', color='green', linestyle='-', marker='o')
    plt.xlabel('Time')
    plt.ylabel('Humidity')
    plt.title('Humidity Over Time')
    plt.legend()
    plt.gca().xaxis.set_major_locator

    plt.tight_layout()
    plt.xticks(rotation=45) 
    plt.savefig("humidity_plot.png")
    plt.close() 

def plot_weather_data(input_file):
    timestamps = []
    temps1 = []
    hums1 = []
    temps2 = []
    hums2 = []

    with open(input_file, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if len(data) == 5:  # Ensure the line has all required data
                try:
                    timestamp = str(data[0])
                    temp1 = float(data[1])
                    hum1 = float(data[2])
                    temp2 = float(data[3])
                    hum2 = float(data[4])
                except ValueError as e:
                    print(f"Error parsing line: {line}")
                    print(e)
                    continue  # Skip lines with parsing errors
                
                timestamps.append(timestamp)
                temps1.append(temp1)
                hums1.append(hum1)
                temps2.append(temp2)
                hums2.append(hum2)  
            else:
                print(f"Skipping invalid line: {line}")


    timestamps = shorten_dataset(timestamps) 
    temps1 = shorten_dataset(temps1) 
    temps2 = shorten_dataset(temps2) 
    hums1 = shorten_dataset(hums1) 
    hums2 = shorten_dataset(hums2)
    plot_temp_data(timestamps, temps1, temps2) 
    plot_hum_data(timestamps, hums1, hums2)


def shorten_dataset(data):  
    shortened = []  
    count = 0
    for i in range (len(data)):  
        count +=1 
        if count == 5:  ## get every nth data point
            shortened.append(data[i]) 
            count = 0 
    
    return shortened



plot_weather_data("data_june5_day.txt")