import os
import pandas as pd

# Define the SLA thresholds for response time (in milliseconds) and throughput (requests per second)
RESPONSE_TIME_SLA = 1000  # 1 second for response time
THROUGHPUT_SLA = 100  # 100 requests per second

DIRECTORY = "script/results"

# Create a dictionary to store SLA data for each JTL file
sla_data = {}

# List of JTL files from the script/results directory
# They have the following format: test_<num_requests>_<iterations>.jtl
# Request: 10, 25, 50
# Iterations: 50, 100, 500

jtl_files = []

# List JTL files in the specified directory
for filename in os.listdir(DIRECTORY):
    if filename.endswith(".jtl"):
        jtl_files.append(os.path.join(DIRECTORY, filename))

# Process each JTL file
for jtl_file in jtl_files:
    # Load the JTL file into a DataFrame
    df = pd.read_csv(jtl_file)

    # Calculate SLA compliance for response time
    total_requests = len(df)
    sla_requests = len(df[df['elapsed'] <= RESPONSE_TIME_SLA])  # Use 'elapsed' column for response time
    sla_percentage = (sla_requests / total_requests) * 100

    # Calculate SLA compliance for throughput (requests per second)
    # Use the 'elapsed' column to calculate the duration of the test
    test_duration_ms = df['elapsed'].max()  # Maximum duration of the test in milliseconds
    test_duration_sec = test_duration_ms / 1000.0  # Convert to seconds

    actual_throughput = total_requests / test_duration_sec
    throughput_percentage = (actual_throughput / THROUGHPUT_SLA) * 100

    # Extract test configuration from the file name
    _, num_requests, iterations = os.path.basename(jtl_file).split("_")
    iterations = iterations.replace(".jtl", "")

    # Store SLA data in the dictionary
    sla_data[jtl_file] = {
        'ResponseTimeSLA': sla_percentage,
        'ThroughputSLA': throughput_percentage,
        'NumRequests': num_requests,
        'Iterations': iterations
    }

# Print SLA data for each JTL file
for jtl_file, data in sla_data.items():
    print(f"JTL File: {jtl_file}")
    print(f"Response Time SLA: {data['ResponseTimeSLA']:.2f}%")
    print(f"Throughput SLA: {data['ThroughputSLA']:.2f}%")
    print(f"Num Requests: {data['NumRequests']}")
    print(f"Iterations: {data['Iterations']}")
    print()
