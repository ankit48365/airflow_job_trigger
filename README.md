<h2>airflow_job_trigger - Steps and Pre-requisites</h2> 
<p>examples on showing how to trigger Python code from Airflow</p>

<p>
1. Clone this repo to your Local Repositry (preferable Linux Distribution)
2. On your Local Machine, run the below

    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt

3. Define Local Variables

    echo 'export AIRFLOW_EXAMPLES="/home/your_path_to_project_directory/"' >> ~/.bashrc
    echo 'export msg_local_variable="example 2 - This message comes via local variable on system"' >> ~/.bashrc
   
</p>
