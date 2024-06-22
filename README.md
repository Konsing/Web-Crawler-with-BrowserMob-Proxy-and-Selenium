# Web Crawler with BrowserMob Proxy and Selenium

This repository contains a web crawling project that uses BrowserMob Proxy and Selenium to capture HTTP Archive (HAR) files for a list of URLs. The project includes scripts for setting up the crawling environment, reading URLs from a CSV file, and handling various exceptions during the crawling process.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Logs](#logs)

## Introduction
This project demonstrates how to use BrowserMob Proxy and Selenium to perform web crawling and capture network traffic in HAR format. It is designed to handle a large number of URLs, manage timeouts, and log any errors that occur during the crawling process.

## Project Structure
The project includes the following files:
- **Part 2.py**: The main Python script that performs the web crawling.
- **top-1m.csv**: A CSV file containing the list of URLs to be crawled.
- **bmp.log**: Log file for BrowserMob Proxy.
- **server.log**: Log file for the server operations.
- **browserproxy-mob/**: (not provided) Directory containing BrowserMob Proxy executable and related files.

## Getting Started

### Prerequisites
- Python 3.x
- Google Chrome browser
- Chromedriver
- BrowserMob Proxy

### Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/web-crawler-bmp-selenium.git
   cd web-crawler-bmp-selenium
   ```

2. Install the required Python packages:
   ```sh
   pip install selenium browsermob-proxy
   ```

3. Download and set up BrowserMob Proxy:
   - Download from the [official site](https://github.com/lightbody/browsermob-proxy/releases).
   - Extract the files and place them in the `browserproxy-mob` directory.

4. Ensure Chromedriver is installed and available in your PATH.

## Usage
1. Place the `top-1m.csv` file in the project directory. Ensure the URLs are listed in the second column of the CSV file.

2. Run the web crawler script:
   ```sh
   python Part 2.py
   ```

3. The script will crawl up to 1000 URLs (or as configured) and save the HAR files in the specified folder.

## Configuration
- **Maximum Crawl Limit**: Adjust the `maxCrawl` variable in `Part 2.py` to change the number of URLs to crawl.
- **Timeout Settings**: Adjust the `driver.set_page_load_timeout(45)` line to change the page load timeout duration.

## Logs
- **bmp.log**: Contains logs related to BrowserMob Proxy operations.
- **server.log**: Contains server-related logs and error messages.