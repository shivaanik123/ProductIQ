import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def calculate_rice_score(reach, impact, confidence, effort):
    return (reach * impact * confidence) / effort

def calculate_moscow_score(priority):
    return {"Must Have": 5, "Should Have": 3, "Could Have": 2, "Won't Have": 1}.get(priority, 1)

# Streamlit UI setup
st.set_page_config(layout="wide")
st.title("Feature Prioritization Tool")
st.sidebar.header("Settings")

# CSV Upload
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Check for necessary columns, if missing, allow manual input
    required_columns = {"Feature", "Reach", "Impact", "Confidence", "Effort", "Priority"}
    missing_columns = required_columns - set(df.columns)
    
    if missing_columns:
        st.sidebar.warning(f"Missing columns: {', '.join(missing_columns)}. Please manually input missing values.")
        for col in missing_columns:
            if col == "Feature":
                df[col] = st.sidebar.text_input(f"Enter default {col}")
            else:
                df[col] = st.sidebar.number_input(f"Enter default {col}", value=1)
else:
    data = {
        "Feature": ["Enhanced Search", "Dark Mode", "AI Recommendations", "Offline Mode", "User Analytics"],
        "Reach": [5000, 8000, 10000, 3000, 6000],
        "Impact": [3, 2, 5, 4, 3],
        "Confidence": [0.8, 0.7, 0.9, 0.6, 0.75],
        "Effort": [4, 2, 6, 5, 3],
        "Priority": ["Must Have", "Should Have", "Could Have", "Won't Have", "Must Have"]
    }
    df = pd.DataFrame(data)

# Choose Prioritization Method
method = st.sidebar.selectbox("Select Prioritization Method", ["RICE", "MoSCoW"])

if method == "RICE":
    df["Score"] = df.apply(lambda row: calculate_rice_score(row["Reach"], row["Impact"], row["Confidence"], row["Effort"]), axis=1)
    score_label = "RICE Score"
elif method == "MoSCoW":
    df["Score"] = df["Priority"].apply(calculate_moscow_score)
    score_label = "MoSCoW Score"

# Sort features by highest score
df = df.sort_values(by="Score", ascending=False)

# Display key metrics
st.metric("Top Feature", df.iloc[0]["Feature"])
st.metric("Average Score", round(df["Score"].mean(), 2))

# Display ranked features
st.subheader("Prioritized Features")
st.dataframe(df)

# Visualization
st.subheader("Feature Prioritization Chart")
fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(df["Feature"], df["Score"], color='skyblue')
ax.set_xlabel(score_label)
ax.set_ylabel("Feature")
ax.set_title(f"Feature Prioritization Based on {method}")
ax.invert_yaxis()
st.pyplot(fig)

# Download button
st.sidebar.download_button("Download Prioritized Features", df.to_csv(index=False), "prioritized_features.csv", "text/csv")
