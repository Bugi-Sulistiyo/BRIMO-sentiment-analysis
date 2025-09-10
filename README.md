# 📊 BRIMO Sentiment Analysis

A sentiment analysis project on **BRIMO**, the mobile banking app from **BRI (Bank Rakyat Indonesia)**.  
This project applies machine learning models to classify customer feedback into **positive, neutral, or negative sentiments**.

---

## 📌 Motivation
As a frequent user of BRIMO, I was curious to understand customer feedback and overall sentiment toward the application.  
By analyzing reviews, this project aims to provide insights into user satisfaction and identify potential areas for improvement.

---

## 📂 Dataset
- **Source**: Scraped from Google Play Store using Google Apps API  
- **Size**: 14,789 reviews (newest first)  
- **Languages**: Indonesian 🇮🇩 and English 🇬🇧  
- **Format**: CSV  

### 🔧 Preprocessing Steps
- Lowercasing text  
- Trimming leading/trailing whitespaces  
- Removing non-alphabet characters, numbers, and non-ASCII characters  
- Removing extra whitespaces  
- Stopword removal (Indonesian & English)  
- Tokenization with **NLTK**  
- Stemming using **Sastrawi** (for Indonesian)  
- Manual slang word removal  
- Null value removal  

---

## 🛠️ Tech Stack
- **Language**: Python  
- **Libraries**: Pandas, NLTK, Scikit-learn, Sastrawi, Lexicon  

---

## 🤖 Modeling Approach
The following machine learning models were tested:

1. **Random Forest**  
2. **Logistic Regression**  
3. **Decision Tree**

Two feature extraction methods were compared: **Bag-of-Words (BOW)** and **TF-IDF**.

---

## 📈 Results

| Model               | Vectorization | Accuracy (Train) | Accuracy (Test) |
| ------------------- | ------------- | ---------------- | --------------- |
| Random Forest       | TF-IDF        | 1.0000           | 0.8854          |
| Random Forest       | BOW           | 1.0000           | 0.8803          |
| Logistic Regression | TF-IDF        | 0.9518           | 0.8870          |
| Logistic Regression | BOW           | 0.9684           | **0.8946**      |
| Decision Tree       | BOW           | 1.0000           | 0.8661          |

✅ **Best model**: Logistic Regression with **Bag-of-Words (BOW)** vectorization (Test Accuracy = **89.46%**)  

---

## 📂 Project Structure
```
│── data/
│ ├── brimo_reviews.csv
│ ├── clean_brimo_reviews.csv
│ └── dataset_sentiment.csv
│
│── script/
│ ├── a. scrapping.py
│ ├── b. clean_data.ipynb
│ ├── c. labelling.ipynb
│ └── d. modeling.ipynb
│
│── requirements.txt
│── README.md
```


---

## ⚙️ How to Run
1. Clone this repository  
   ```bash
   git clone https://github.com/yourusername/BRIMO-Sentiment-Analysis.git
   cd BRIMO-Sentiment-Analysis
   ```
2. Create a virtual environment and install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Run the scripts in order (A → D):
   - `a. scrapping.py` → Scrape reviews
   - `b. clean_data.ipynb` → Clean text data
   - `c. labelling.ipynb` → Label sentiment
   - `d. modeling.ipynb` → Train and evaluate models


---
## 🚀 Future Improvements
- Implement deep learning models (e.g., LSTM, BERT)
- Add more visualization (word clouds, confusion matrix, sentiment distribution)
- Deploy as a web application for interactive sentiment analysis

---
## 📜 License
This project is created for educational and research purposes.
No official affiliation with **Bank Rakyat Indonesia (BRI)** or the **BRIMO app**.