# Analyzing CryptoPunks Volume and Average Price using Python

## Subtitle: A Deep Dive into CryptoPunks Trading Patterns

![nft-crypto-clone 7 53 01 PM](https://github.com/Deba951/cryptopunks-analysis/assets/83878346/133bc30c-e429-4916-81d9-2d16ca992817)

## Overview
This project aims to analyze the trading volume and average price of CryptoPunks NFTs on the Ethereum blockchain. By leveraging data from the Moralis API, we process and visualize the trends over a specified period.

## Objective
To fetch and process CryptoPunks transaction data to understand market trends and investor behavior.

## Aim
Retrieve NFT transaction data, clean and process it, and create visualizations that showcase the trading volume and average price of CryptoPunks NFTs over the past few days.

## Features
- Data Collection from Moralis API
- Data Filtering and Processing
- Calculation of Daily Volumes and Average Prices
- Visualization using Matplotlib

## Setup and Installation

### Prerequisites
- Python 3.7 or above
- Moralis API Key

### Libraries Used
- `moralis`
- `numpy`
- `pandas`
- `matplotlib`
- `dotenv`

### Steps to Set Up the Environment
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/cryptopunks-analysis.git
    cd cryptopunks-analysis
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add your Moralis API key:
    ```plaintext
    api_key=your_moralis_api_key
    ```

## Usage
Run the script to fetch, process, and visualize CryptoPunks transaction data:
```bash
python main.py
