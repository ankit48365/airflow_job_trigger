<img alt="GitHub Actions Workflow Status" src="https://github.com/ankit48365/airflow_job_trigger/actions/workflows/python-app.yml/badge.svg">


<h2>airflow_job_trigger - Steps and Pre-requisites</h2>
<p>Examples on showing how to trigger Python code from Airflow:</p>

<ol>
  <li>Clone this repo to your Local Repository (preferable Linux Distribution).</li>
  <li>On your Local Machine, run the below:</li>
  <ul>
    <li><code>python3 -m venv .venv</code></li>
    <li><code>source .venv/bin/activate</code></li>
    <li><code>pip3 install -r requirements.txt</code></li>
  </ul>
  <li>Define Local Variables:</li>
  <ul>
    <li><code>echo 'export AIRFLOW_EXAMPLES="/home/your_path_to_project_directory/"' >> ~/.bashrc</code></li>
    <li><code>echo 'export msg_local_variable="example 2 - This message comes via local variable on system"' >> ~/.bashrc</code></li>
  </ul>
</ol>
