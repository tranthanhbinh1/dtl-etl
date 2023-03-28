# Singapore Exchange derivative data pipeline
The program aims to automatically download derivative data published daily from SGX - Singapore Stock exchange.

The program includes 2 parts: 
- An Airflow job to automatically download data at 9am - UTC+8.
- An manual job that takes in user input (date, which file to download).

The code is structured as follow:
- airflow: the job's DAG is stored here.
- config: where all the default values are stored.
- crawler: the main component of the project, use to download files.
- data: some of the data that I downloaded using the this program.
- test: all the unit tests that were performed in this projects.
- utils: all the utility functions needed for the main component.
- IDs list: an text file that I use to store the lastest ID.
- job_logging: a log file that store some of the logs during the execution of this project.
- requirements: all the required dependencies for this project.

Improvements still need to be made for the following functions:
- Manual job, right now the date argument is still inaccurate with a big margin of error, therefore an alternative has been implemented with file ID as an indicator.
- The manuall job was made with a scope of being able to accept config files, but as of now it has not been implemented.

To run the project, clone it, create a virtual environent, and install:
```
pip install -r requirements.txt
```
Activate the environment.
To run the manual job, run:
```
python -m crawler.manu_job [date] [optional: file index]
```
To run the alternate manual job, run:
```
python -m crawler.manu_job_alternate [id] [optional: file index]
```

