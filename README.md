# Window-Server-Quota-Report-Automation
Python &amp; Powershell based script to produce a HTML based report for Windows Server Quota Available Space
The script is orchestrated via Windows Task Schedular for 08:00 Daily.

# Tech Stack
- Python
- PowerShell
- Windows Task Schedular
- SMTP
- HTML
- SQLite

# Motivation
The objective of this project was to automate a manual governance check that ensures divisional offices have sufficient available quota on Windows SMB file servers for workload storage.
Previously, this process required engineers to:

-Manually RDP into each Windows server
-Individually check filesystem quota availability
-Record and consolidate results manually

-This approach was time-consuming, inefficient, and prone to human error.
Uses PowerShell to remotely query quota and disk availability across multiple on-prem Windows servers

# Solution
This project introduces a modern, automated solution that: </br>
-Uses PowerShell to remotely query quota and disk availability across multiple on-prem Windows servers
-Leverages Python to orchestrate execution and process the collected data
-Stores the data in SQLITE for future analysis
-Converts the results into a structured HTML report
-Automatically distributes the report via SMTP email to a shared operations mailbox

# Outcome

-Eliminated the need for manual server checks
-Reduced operational overhead and time-to-report
-Improved accuracy and consistency of quota monitoring
-Provided a scalable, repeatable solution suitable for enterprise environments
-Provides a data set for future analysis (which divisions use the most storage)


The below shows what the report that the script produces looks like

__DISCLAIMER:__ Sensitive information has been blurred for privacy
<img width="1062" height="1032" alt="image" src="https://github.com/user-attachments/assets/c3b9a0c3-bc88-4e9a-8d83-38ae073e01c7" />
