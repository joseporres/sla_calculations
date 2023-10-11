#!/bin/bash

# Function to run JMeter tests
run_jmeter_test() {
  local num_requests=$1
  local iterations=$2
  local jmx_file=$3

  echo "Running JMeter tests with $num_requests requests and $iterations iterations..."

  docker run -v "$(pwd)/jmeter:/jmeter" -v "$(pwd)/results:/results" \
    --name jmeter -it --rm --network host \
    -e numofreq=$num_requests -e loopCount=$iterations \
    justb4/jmeter -n -t /jmeter/$jmx_file -l /results/test_${num_requests}_${iterations}.jtl

  echo "JMeter tests with $num_requests requests and $iterations iterations completed."
}

# Run JMeter tests with different configurations
run_jmeter_test 10 50 test.jmx
run_jmeter_test 10 100 test.jmx
run_jmeter_test 10 500 test.jmx

run_jmeter_test 25 50 test.jmx
run_jmeter_test 25 100 test.jmx
run_jmeter_test 25 500 test.jmx

run_jmeter_test 50 50 test.jmx
run_jmeter_test 50 100 test.jmx
run_jmeter_test 50 500 test.jmx
