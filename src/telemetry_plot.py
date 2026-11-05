import fastf1
import matplotlib.pyplot as plt

# 1. Enable cache for faster data loading
fastf1.Cache.enable_cache('cache')

def analyze_driver_telemetry(year, grand_prix, session_type, driver_code):
    print(f"Loading data for {grand_prix} {year} ({session_type}) - Driver: {driver_code}...")
    
    # 2. Load session and laps
    session = fastf1.get_session(year, grand_prix, session_type)
    session.load(laps=True, telemetry=True)
    
    # 3. Select the driver's fastest lap
    laps = session.laps.pick_driver(driver_code)
    fastest_lap = laps.pick_fastest()
    
    # 4. Get telemetry for the fastest lap
    telemetry = fastest_lap.get_telemetry()
    
    distance = telemetry['Distance']
    speed = telemetry['Speed']
    throttle = telemetry['Throttle']
    brake = telemetry['Brake']
    
    # 5. Create plots (Speed Trace)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    
    # Speed Plot
    ax1.plot(distance, speed, label=f'{driver_code} Speed', color='red', linewidth=2)
    ax1.set_ylabel('Speed [Km/h]')
    ax1.set_title(f'Telemetry Analysis - {fastest_lap["Driver"]} ({year} {grand_prix})')
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.legend()
    
    # Throttle / Brake Plot
    ax2.plot(distance, throttle, label='Throttle [%]', color='green', linewidth=1.5)
    ax2.plot(distance, brake * 100, label='Brake [On/Off]', color='blue', linewidth=1.5, linestyle='--')
    ax2.set_xlabel('Distance [m]')
    ax2.set_ylabel('Controls')
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example: Analyze Max Verstappen's telemetry
    analyze_driver_telemetry(2023, 'Bahrain', 'Q', 'VER')