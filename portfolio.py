import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="Anna | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide"
)

# 2. Sidebar / Bio
with st.sidebar:
    st.markdown("# Anna Szcz")
    st.markdown("🚀 **Data Analyst** specialising in complex relational database design, analytics engineering, and business insight generation.")
    st.markdown("---")
    st.markdown("🔗 **Connect with me:**")
    st.markdown("[GitHub](https://github.com/annaszcz)")
    st.markdown("[LinkedIn](https://linkedin.com) *(Update link)*") # set up
    st.markdown("---")
    st.markdown("💡 **Core Stack:**\n- **SQL** (SQL)\n- **Python** (Pandas, Streamlit)\n- **BI** (Tableau, PowerBI)\n- **Tools** (dbt, Git)")

# 3. Main Hero Section
st.title("Hi, I'm Anna! 👋")
st.subheader("Data Analyst | BI Specialist")
st.write(
    "Welcome to my interactive data portfolio. I specialise in parsing massive datasets, "
    "structuring star-schema data warehouses, and delivering actionable optimizations for business leaders."
)
st.markdown("---")

# 4. Featured Portfolio Projects Section
st.header("🎯 Featured Projects")

# Create tabs to neatly split projects without forcing the recruiter to scroll endlessly
tab1, tab2 = st.tabs(["📊 Bike-share analysis" , "🛍️ E-commerce-analysis"])

with tab1:
    st.subheader(" Bike share analysis on Capital Bike Share (Washington, DC) dataset")
    st.markdown("**Business Goal:** Prediction of the bike demand and supply optimisation")
    
    # Showcase your tech tags
    st.info("🛠️ **Technologies Used:** Data Wrangling, Exploratory Data Analysis, Time Series and Linear Regression, ",
            "**Python: Pandas, Numpy, Sklearn, Matplotlib, Seaborn**"
    )
    
    # Mock data to show you know how data inputs work
    mock_data = pd.DataFrame({
        'cohort_month': ['January', 'February', 'March'],
        'total_users': [1200, 950, 1100],
        'month_1_retention': ['88%', '84%', '89%'],
        'month_2_retention': ['61%', '58%', '64%']
    })
    
    # Split the view layout side-by-side using columns
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🗄️ The Portfolio SQL Query")
        st.markdown("This query demonstrates calculating running cohort drops using window functions:")
        
        # Displaying your clean syntax
        sql_code = """
WITH user_activity AS (
    SELECT 
        user_id,
        DATE_TRUNC('month', signup_date) AS cohort_month,
        EXTRACT(MONTH FROM AGE(activity_date, signup_date)) AS period_month
    FROM web_events
)
SELECT 
    cohort_month,
    period_month,
    COUNT(DISTINCT user_id) AS active_users,
    LAG(COUNT(DISTINCT user_id), 1) OVER (
        PARTITION BY cohort_month ORDER BY period_month
    ) AS prior_month_users
FROM user_activity
GROUP BY 1, 2;
        """
        st.code(sql_code, language="sql")
        
    with col2:
        st.markdown("### 📈 Pipeline Output")
        st.dataframe(mock_data, use_container_width=True)
        st.success(
            "💡 **Core Insight:** The data showed a 39% average drop-off by Month 2. "
            "Cross-referencing feature activity logs showed that users who didn't set up "
            "Profile Feature X within week 1 made up 80% of the churn group."
        )
        st.markdown("[👉 View Code Repository](https://github.com/annaszcz)")

with tab2:
    st.subheader("E-Commerce Supply Chain Optimization")
    st.markdown("**Business Goal:** Detect hidden shopping cart abandonment intervals and optimize stock levels.")
    st.info("🛠️ **Technologies Used:** MySQL, Self-Joins, Conditional Aggregation")
    st.write("*(You can structure this tab identically to Project 1 with your second query and metrics!)*")

st.markdown("---")
st.markdown("✍️ *Built completely inside Python using the Streamlit framework.*")
