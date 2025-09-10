# google-playstore-data-analysis
📊 Google Playstore Data Analysis
This project performs exploratory data analysis (EDA) on the Google Play Store Apps dataset.
It includes data cleaning, preprocessing, and generating insights into what drives app success on the Play Store.

📂 Project Structure
nginx
Copy code
google playstore data analysis/
│
├─ data/                         # Raw & cleaned datasets
│   ├─ googleplaystore.csv       # Raw dataset (from Kaggle)
│   └─ googleplaystore_clean.csv # Cleaned dataset (generated)
│
├─ notebooks/
│   └─ 01_EDA.ipynb              # Jupyter Notebook for EDA
│
├─ src/
│   └─ data_cleaning.py          # Data cleaning script
│
├─ reports/                      # Plots, slides, and findings
│
├─ requirements.txt              # Python dependencies
└─ README.md                     # Project documentation
⚙️ Setup Instructions
1. Clone / Create the project
Make sure the dataset (googleplaystore.csv) is placed inside the data/ folder.
Final path:

kotlin
Copy code
google playstore data analysis/data/googleplaystore.csv
2. Create a virtual environment
Open VS Code terminal (PowerShell or CMD) inside the project folder:

bash
Copy code
python -m venv .venv
Activate the environment:

PowerShell:

bash
Copy code
.\.venv\Scripts\Activate.ps1
CMD:

cmd
Copy code
.venv\Scripts\activate
When active, you should see (.venv) before your prompt.

3. Install requirements
Install all dependencies from requirements.txt:

bash
Copy code
pip install --upgrade pip
pip install -r requirements.txt
📦 Requirements
Main libraries used in this project:

pandas – data manipulation

numpy – numerical computing

matplotlib – plotting

seaborn – statistical visualizations

plotly – interactive charts

scikit-learn – machine learning (optional use)

jupyter / notebook / ipykernel – running notebooks

All are included in requirements.txt.

🧹 Data Cleaning
Run the cleaning script to process the raw dataset:

bash
Copy code
python src\data_cleaning.py
This will:

Handle missing values

Convert columns (Reviews, Installs, Price, Size) to numeric formats

Convert Last Updated to datetime

Remove duplicates

Save cleaned file as:

bash
Copy code
data/googleplaystore_clean.csv
📊 Exploratory Data Analysis
Open the Jupyter notebook:

bash
Copy code
jupyter notebook notebooks/01_EDA.ipynb
Example analyses:

Distribution of app ratings

Top categories by app count

Free vs Paid apps comparison

Installs vs Reviews correlation

Size vs Rating

Update frequency vs Rating

Correlation heatmap of numeric features

Visuals include bar charts, histograms, scatter plots, and heatmaps.

📈 Business Insights
Some example insights this project explores:

Free apps dominate installs, but Paid apps can achieve higher average ratings.

Games have the largest number of apps, while Productivity apps tend to score higher ratings.

Frequent updates correlate with higher user ratings.

Larger apps (in MB) don’t always guarantee better ratings.

📑 Deliverables
Cleaned dataset → data/googleplaystore_clean.csv

Jupyter notebook → notebooks/01_EDA.ipynb

Plots → stored in reports/ (exported manually from notebook)

Presentation/summary → A short slide deck with top findings (optional for interview use)

✅ Quick Checklist
 Project folder created on Desktop

 CSV extracted into data/

 Opened project in VS Code

 Created & activated .venv

 Installed packages via requirements.txt

 Ran python src/data_cleaning.py → created cleaned CSV

 Opened notebooks/01_EDA.ipynb and started visual analysis
