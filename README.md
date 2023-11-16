# CURU Skincare Recommendation System
## Project Overview
CURU aims to simplify the skincare selection process by providing tailored product recommendations based on user preferences and skin profiles. The platform prioritizes genuine advice, avoiding paid promotions, and integrates data science to enhance its recommendation system. This project involves data collection from Chemist Warehouse, data cleaning, exploratory data analysis, and two key methodologies for recommendation: User-Based Collaborative Filtering (UBCF) and Keyword Extraction with Textrank.

## Files and Directories
# Data Collection:
ChemistWarehouseWebScraping.ipynb: Contains python script to web scrap data from the Chemist warehouse. website.

# Data Cleaning:
KeywordExtractionAndClustering.ipynb: Jupyter notebook detailing the methodology for keyword extraction using Textrank and clustering products based on attributes.
# Recommendation Function:

recommendation.py: Python script containing the function to recommend products based on UBCF method.
spacyRecommendation.py: Python script containing the function to recommend products based on Key extraction and Clustering method.

# Web App Demo Layout:
## Front Page: 
Recommends products for both existing and non-existing users, 

Existing Users:  

Based on the products they reviewed previously. 

Both UBCF and Key word extraction methodology is used separately to recommend products. 

Non-Existing Users:  

Based on the skin profile they select.  

Only Key word extraction methodology is used to recommend products. 

 
 ![image](https://github.com/devayani24/Personalized-skin-care-recommnedation/assets/76246283/54fb42a8-ce09-4781-be68-4c269b4c4e41)



## For Existing Users: 

 ![image](https://github.com/devayani24/Personalized-skin-care-recommnedation/assets/76246283/633be510-5d4b-4c74-b988-170f367c57c6)
 ![image](https://github.com/devayani24/Personalized-skin-care-recommnedation/assets/76246283/25a380bb-4f3b-4ed8-9f14-b46ad36061e0)



## For New Users: 

For example, if a new user selects their skin profiles such as, 

Hydrate Skin 

Acne Skin 

Dry Skin 

Sensitive Skin 

![image](https://github.com/devayani24/Personalized-skin-care-recommnedation/assets/76246283/e50389d8-a808-4c46-90c2-6e4d50f94815)

After selecting the skin profiles and clicking “submit” button, the recommended products are listed with the explanation,
![image](https://github.com/devayani24/Personalized-skin-care-recommnedation/assets/76246283/82655bf6-e684-4126-b217-790d37eb0055)

