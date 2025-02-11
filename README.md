# FeatureRank: AI-Powered Feature Prioritization Tool

## 📌 Overview
FeatureRank is a data-driven **feature prioritization tool** designed to help product managers, engineers, and teams rank product features effectively. Using frameworks like **RICE** and **MoSCoW**, FeatureRank provides insights into which features should be prioritized for development. The tool supports CSV uploads, manual data entry, and dynamic visualization.

## 🚀 Features
- **🔢 RICE & MoSCoW Prioritization** – Choose between **RICE (Reach, Impact, Confidence, Effort)** or **MoSCoW (Must Have, Should Have, etc.)** frameworks.
- **📂 CSV Upload Support** – Easily import your own feature dataset.
- **📊 Interactive Data Visualization** – Get clear insights through bar charts and dynamic tables.
- **🔄 Column Auto-Detection** – Handles missing data by allowing manual input.
- **📥 Export Prioritized Features** – Download results in CSV format for further use.

## 🛠️ Installation
Ensure you have **Python 3.8+** installed.

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/FeatureRank.git
   cd FeatureRank
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📌 Usage
Run the Streamlit app:
```bash
streamlit run app.py
```
Then, open the **localhost link** in your browser to start prioritizing features.

## 📂 Example CSV Format
If you want to upload your own dataset, ensure it follows this structure:
```csv
Feature,Reach,Impact,Confidence,Effort,Priority
Live Chat Support,12000,4,0.9,3,Must Have
AI-Powered Search,9000,5,0.85,4,Must Have
Custom Dashboards,7000,4,0.8,5,Should Have
```

If your dataset has different column names, the tool will prompt you to map them accordingly.

## 🛠️ Roadmap & Future Improvements
- 📈 Support for **Weighted Scoring Models**.
- 🤖 **AI-based Feature Recommendations**.
- 📊 **More Visualization & Roadmap Tools**.

## 🤝 Contributing
Want to improve **FeatureRank**? Feel free to submit pull requests!

## 📜 License
MIT License © 2025 Your Name

