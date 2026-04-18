# 🧹 Customer Deduplication Pipeline

## Problem
This project helps companies identify and remove 
duplicate customer accounts that may be missed due 
to typing errors or different ways of writing names.
Using intelligent matching rules, the system recognizes 
that records like "John Smith" and "Smith, John" likely 
refer to the same person even when formatting differs.

By cleaning these duplicates we:
- Improve data accuracy and maintain a cleaner database
- Reduce operational mistakes like duplicate emails
- Get a more reliable and truthful unique customer count

## Solution
**Normalize:** Make all names lowercase and trim hidden 
spaces so "JOHN" and "john" are treated identically.

**Sort:** Order records by date so the most recent 
information is always prioritized.

**Remove Exact Duplicates:** Delete 100% identical 
records leaving one clean copy of each person.

**Catch Fuzzy Duplicates:** Use intelligent fuzzy 
search to find typos or flipped names like "Jon Smith" 
and "Smith, John" and flag them as the same person.

## Technologies Used
- Python
- Pandas
- NumPy
- RapidFuzz
- Google Colab
- GitHub

## How To Run
1. Clone this repository
2. Open cleaning_pipeline.ipynb in Google Colab
3. Run each cell from top to bottom
4. View the cleaned output dataframe

## Author
**Stephen Abiodun**
Founder - AimFastTech
Data Scientist & Cyber Security Analyst 🇳🇬
