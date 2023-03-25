Introduction
This Data Engineering Mini Project was built in order to automatically download derivatives data from SGX through their website. The project has two main parts:
 The first script, named auto_job , is utilized with Airflow as a scheduler in order to download the files every day at 9 AM.
The second script, named manu_job, is used when users want to manually download files based on options that users can specify in the command line.
The project requires some Python libraries to run properly: wget, requests,   apache-airflow, other dependencies are all bundled with Python (3.7 and above)

Installation and Usage
Installation
Open the project, go to the project directory
 Create a Virtual Environment, in this case, I used Python 3.10.6, but Python 3.7 and above should be fine
Install all the dependencies listed in the file requirements.txt.
The SSH Operator is not required, but I used this on my Local machine, the normal approach would be using the BashOperator.
	Usage
To download the file manually, cd to the project directory, and run the module as script with: python -m crawler.test [date] [optional: link_index] 
The default option is downloading all 4 files
Date follow the format: YYY-MMM-DDD
The optional link index is as follow:
	- 0 for Tick
	- 1 for Tick Data Structure
	- 2 for Trade Cancelation
	- 3 for Trade Cancelation Data Structure
Downloading files
Historical files (or today’s file) should be downloaded given the users’ input date and optional.
Today’s file should be downloaded via the automatic job, or else can also be downloaded via the manual job, given specified options in the command line.


Logging:
Logging is implemented when downloading the files, there are 2 types of logs: a console logger that logs to stdout and a file logger that logs to a file name job_logging.log
In this project, I decided that when download a job manually, both stdout and file logging should be implemented, and when downloading through schedule with Airflow, only file logging is implemented
The reason behind is simple, I thought that when downloading manually, the logs should be stdout to inform the user about problems right when it’s executed, additional file logging is also important to keep the consistency for the log file.
With the scheduled job, I thought that file logging is enough, as it’s schedule and run in the background, so no need to print anything to stdout.
With both file and stdout implemented, it should help to debug, with Airflow, there is native logging implemented, so if there is anything wrong with the automated job, it should be logged in Airflow log files.

Recovery plan
For this scenerio, I simply config the job to to retries after every 1 hour, and up to 5 times of retry
In my opinion, this is sufficient, however I could be very wrong.

Concerns with the design and implementation
This design still has many problems, however, in the time frame of the test, I could not resolve them, here are the problems:

The date option does not work properly:
For this option, in order to make it easy downloading historical, I used a library called WorkCalendar to have information about working days in Singapore, so that I could map those to the IDs. However, initially worked, there are errors, with my limited experiment, up to 5 days compared to the corresponding ID ( example: if I entered the date option: 2022- 9 -1, the corresponding ID and file are that of 2022-9-6 ), and I believe there may be bigger error in between the date input and the actually file downloaded.
Because of this reason, I wrote an alternate version of this job that accept IDs instead of Date. This version guarantees the correct files downloaded, given that you can specify the IDs for the historical data you wanted.
However, my idea holds still, user should be able to input the Date and retrieve the data effortlessly.

File IDs are not entirely orderd
For this problem, I initially wanted to do Proof of Concept, but it failed, basically for the more recent files, they are published every work day (from Monday to Friday), around 3000 recent IDs follow this pattern.
However, for very old data files, its not linearly ordered, not all of them have 4 listed files. For example the date 2004-03-29 has a corresponding ID of 2378, while the date 2004 11 03 has a corresponding ID of 2224, it’s backward.
This may be because there is a mechanism for historical data that I am not aware of as of the time doing this project, for this problem I think with more time and information we can have the desired outcome.

Accepting Config files
In the time frame of this project, I was not able to implement config files parsing, but if implemented, I would have designed a more robust option sets, maybe including option for user to specify the  time frame of historical data to be downloaded and option to choose which file to download, rather than just 1 file or all 4 files like this current implementation.

Testing
My intention was to implement unit testing for every function used in this project, however I was not able to get my research done for some of the functions.
In total, I created 4 unit tests for 4 functions:
	- Download the file
	- Check if the records are available
	- Calculate IDs based on date
	- Create folder
	
Out of the 4 tests, all passed the scenarios except the Create folder function, it failed one of the assertions, but I still have not figured out why.

Regarding Airflow job
In this project, I used SSHOperator to test the scrip on my local machine, because I am using Docker for Airflow so in order to run the more ordinary BashOperator, I would have to set up many things. Those set ups are time consuming and quite heavy on my machine, so I choose to use SSHOperator.

7. Conclusion
 		With this project, I have learned many things new and actually implemented them. It’s a fun 5 days. Regardless of the result, I sincerely want a feedback from the team on where I should improve with this project, or with Software/Data Engineering practices in general. 

Thanh Binh
