#!/bin/bash

# Path to the Python interpreter in the virtual environment
VENV_PATH="/home/ankiz/Documents/mygit/airflow_job_trigger/.venv/bin/python"

# Path to the Python script to be executed
SCRIPT_PATH="/home/ankiz/Documents/mygit/airflow_job_trigger/example_1/example_1.py"

# Output file
OUTPUT_FILE="/home/ankiz/Documents/mygit/airflow_job_trigger/example_1/example_1.out"

# Write the time of script execution to the output file
echo "Script execution started at: $(date)" >> $OUTPUT_FILE

# Activate the virtual environment and run the Python script, then append the output or error to the output file
$VENV_PATH $SCRIPT_PATH >> $OUTPUT_FILE 2>&1

# Write the time of script completion to the output file
echo "Script execution completed at: $(date)" >> $OUTPUT_FILE
echo "-----------------------------------------" >> $OUTPUT_FILE