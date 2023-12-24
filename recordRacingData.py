import irsdk
import time
import csv

def main():
    ir = irsdk.IRSDK()
    try:
        # Attempt to connect to iRacing
        ir.startup()

        with open('iracing_data.csv', 'w', newline='') as csvfile:
            fieldnames = ['Timestamp', 'Speed', 'Brake', 'Throttle', 'Gear', 'VertAccel']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            while True:
                # Check if iRacing is connected
                if ir.is_connected:
                    ir.freeze_var_buffer_latest()
                    data = {
                        'Timestamp': time.time(),
                        'Speed': ir['Speed'],
                        'Brake': ir['Brake'],
                        'Throttle': ir['Throttle'],
                        'Gear': ir['Gear'],
                        'VertAccel': ir['VertAccel']
                    }
                    writer.writerow(data)

                    # Wait for 0.5 seconds before the next record
                    time.sleep(0.5)
                else:
                    print("Waiting for iRacing connection...")
                    time.sleep(1)

    except KeyboardInterrupt:
        # Gracefully exit on Ctrl+C
        pass
    finally:
        # Ensure iRacing connection is closed
        ir.shutdown()

if __name__ == '__main__':
    main()