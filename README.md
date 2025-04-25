# 🛍️ **E-Commerce Product Data API**  
  
## 🌐 Project Overview  
This project involves automatically cleaning an e-commerce products dataset using pandas python, normalizing it into a MySQL database, and exposing the data through a Flask-based web API.
The dataset consists of product information from SheIn website, spanning +80,000 products and +20 CSV files. This project demonstrates data cleaning, wrangling, and API development skills,
useful for anyone looking to refine their data analysis or back-end development expertise.  
  
## 🛠️ Technologies Used  
- **Python**: Primary programming language for data cleaning and API development.  
- **Pandas**: Used for cleaning and wrangling the dataset.  
- **MySQL**: Used for storing and querying the cleaned and normalized data.  
- **Flask**: Framework for building the web API.  
- **SQLAlchemy**: ORM used for interacting with the MySQL database.  
- **Flasgger**: Used to generate Swagger documentation for the API.  
  
## 📂 Dataset  
The dataset contains product details like:  
- **Product ID**  
- **Product Title**  
- **Price**  
- **Discount**  
- **Color Count**  
- **Rank**  
- **Category ID**  
  
## 🧹 Data Cleaning
The raw dataset included inconsistencies, missing values, and formatting issues. Using Pandas, the data was cleaned and prepared for further analysis. This process involved:  
- **Merging data sets**  
- **Rebuilding missing data**  
- **Standarization**  
- **Normalization**  
- **De-Duplication**  
- **Verification and enrichment**  

## 🌍 Web API  
A Flask web API was developed to expose the data stored in MySQL. The API allows you to interact with the data via multiple endpoints  
  
## ⚙️ Installation  
### Clone the repository:  
```bash
git clone https://github.com/mkfoudili/SheinCleanData.git cd <repo_folder>  
```    
### Install dependencies:  
```python
pip install -r requirements.txt  
```  
### Set up the database:  
Ensure you have MySQL installed and running. Configure the database connection in your db.py file and create the necessary tables by running the Flask app.  
  
### Run the Flask app:  
```python
python app.py
```
The Flask application should now be running locally at http://127.0.0.1:5000.  

    
## 🤝 Contributions:  
Les contributions sont les bienvenues ! Si tu veux :  
  1. corriger un bug  
  2. proposer un nouvel algorithme  
  3. améliorer les documents pédagogiques
n'hésite pas à **ouvrir une issue** ou à faire une **pull request**.  
    
## 📜 Licence  
Ce projet est sous licence MIT  
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)  
  
## 👨‍💻 Auteur:  
Développé avec ❤️ par [Khadidja Foudili](https://github.com/mkfoudili)  
