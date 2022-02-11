# Chinese News Aggregator
## Status Update
**Current Sprint Backlog:**
- Ticket-006: Update China Daily automated web scraper to version 2.0 (replace basic web scraper with Scrapy framework)
- Ticket-007: Scrape historical China Daily data using Scrapy framework
- Ticket-008: Update pipeline S3 module to support expanded dataset and new Scrapy framework

**Next Sprint Backlog:**
- Ticket-009: Expand Scrapy spiders to collect data from full list of 20+ news sources
- Ticket-010: Update pipeline part 1 (data extraction via web scraping and data staging via AWS S3) to support expanded dataset; S3 naming conventions and S3 data upload module will need updates
- Ticket-011: Write unit tests/incorporate Great Expectations for data validation for Scraper and S3 modules

## Table of Contents
- [Project Description](#project-description)
- [Project Motivation](#project-motivation)
- [How to Install and Run the Project](#how-to-install-and-run-the-project)
    - [Environment - Coming Soon](#environment---coming-soon)
    - [Technologies Used](#technologies-used)

## Project Description
The Chinese News Aggregator project will be a fully-automated ETL pipeline that collects article data from Chinese national newspapers and stores it in a data warehouse for future analysis.

This project has a data engineering focus of building a pipeline that collects, prepares, and stores data so that it is ready for analysis by data analysts and data scientists or ready for import into other integrated applications. The secondary goal is to aggregate the data into a dashboard containing a sentiment analysis as well as metrics of the Chinese government's attitude towards the United States over time.


## Project Motivation
Returning to the United States after living in Shanghai, China, I realized how little knowledge average Americans have about the rising superpower, the Chinese Communist Party (CCP), and its views on the world; America in particular.

In China, national newspapers exist as the mouthpiece of the CCP and in a country with extensive censorship they represent the messages that the sole governing party of China broadcasts to its people. People are not their governments, therefore the attitudes of national newspapers do not necessarily represent the attitudes of the average Chinese person. However, this project aims to shine a light on the ideas and opinions that the CCP is pushing towards its citizens regarding the United States.


## How to Install and Run the Project
### Environment - Coming Soon
- Python version 3.9.5
- Run setup.py file or restore venv from requirements.txt file (setup.py file not yet available)
### Technologies Used
- Web Scraping
    - BeautifulSoup for version 1.0
    - Scrapy framework for version 2.0
- Computing
    - AWS EC2 type t2.micro running Red Hat Enterprise Linux
- Staging
    - AWS S3
- Warehousing
    - AWS Redshift
