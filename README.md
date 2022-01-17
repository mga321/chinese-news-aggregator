# Chinese News Aggregator
## Table of Contents
- [Project Description](#project-description)
- [Project Motivation](#project-motivation)
- [How to Install and Run the Project](#how-to-install-and-run-the-project)
    - [Environment](#environment)
    - [Technologies Used](technologies-used)

## Project Description
The Chinese News Aggregator project is a fully-automated ETL pipeline that collects article data from Chinese national newspapers and stores it in a data warehouse for future analysis.

This project has a data engineering focus of building a pipeline that collects, prepares, and stores data so that it is ready for analysis by data analysts and data scientists or ready for import into other integrated applications. The secondary goal is to aggregate the data into a dashboard containing sentiment analysis and metrics of the Chinese government's attitude towards the United States over time.


## Project Motivation
I lived in China for a combined total of over 3 years and after returning to the United States, I was surprised to find out average Americans have minimal to no knowledge about the Chinese Communist Party (CCP) and how it views the world; America in particular.

In China, national newspapers exist as the mouthpiece of the CCP and in a country with extensive censorship they represent the messages that the sole governing party of China broadcasts to its people. People are not their governments, therefore the attitudes of national newspapers do not necessarily represent the attitudes of the average Chinese person. However, this project aims to shine a light on the ideas and opinions that the CCP is pushing towards its citizens regarding the United States.


## How to Install and Run the Project
### Environment
- Python version 3.9.5
- Run setup.py file or restore venv from requirements.txt file (setup.py file not yet available)
### Technologies Used
- Web Scraping
    - BeautifulSoup for version 1.0
    - Scrapy for version 2.0 (coming soon)
- Computing
    - AWS EC2 type t2.micro running Red Hat Enterprise Linux
- Staging
    - AWS S3
- Warehousing
    - AWS Redshift
