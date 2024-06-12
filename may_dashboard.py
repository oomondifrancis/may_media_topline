import streamlit as st
import pandas as pd
import plotly.express as px

# Define the data for child-related issues most prominent in the media
child_issues_data = {
    "Child Related Issues": [
        "HEALTH", "CHILD SAFETY", "ENVIRONMENT", "EDUCATION AND YOUTH", "NATURAL CALAMITIES", "HIV AIDS", 
        "QUALITY EDUCATION", "MATERNAL HEALTH", "GENDER BASED VIOLENCE_GBV", "NUTRITION", "MENTAL HEALTH", 
        "DEFILEMENT", "CLIMATE CHANGE", "WATER AND SANITATION", "EARLY CHILDHOOD DEVELOPMENT"
    ],
    "Frequency": [
        515, 318, 299, 293, 285, 271, 251, 185, 183, 169, 154, 146, 126, 124, 115
    ]
}

# Define the data for media coverage of child-related issues by media type
media_coverage_data = {
    "Media Type": ["PRINT", "RADIO", "TV"],
    "Frequency": [380, 1979, 468]
}

# Define the data for top 10 thematic areas with the most media coverage
top_thematic_areas_data = {
    "Thematic Area": [
        "HEALTH", "CHILD SAFETY", "ENVIRONMENT", "EDUCATION AND YOUTH", "NATURAL CALAMITIES", "HIV AIDS", 
        "QUALITY EDUCATION", "MATERNAL HEALTH", "GENDER BASED VIOLENCE_GBV", "NUTRITION", "MENTAL HEALTH", "DEFILEMENT"
    ],
    "Number of Mentions": [
        515, 318, 299, 293, 285, 271, 251, 185, 183, 169, 154, 146
    ]
}

# Define the data for free space & airtime accorded to child rights issues in the monitored media outlets
free_space_data = {
    "Media Type": ["PRINT", "RADIO", "TV"],
    "Amount": [
        1241151304, 313927719, 1746566702
    ]
}

# Convert dictionaries to DataFrames
df_child_issues = pd.DataFrame(child_issues_data)
df_media_coverage = pd.DataFrame(media_coverage_data)
df_top_thematic_areas = pd.DataFrame(top_thematic_areas_data)
df_free_space = pd.DataFrame(free_space_data)

# Streamlit App Layout
st.title("UNICEF Top Line May Dashboard")
st.markdown(
    """
    <style>
    /* Title color */
    .title {
        color: #03A9F4;
    }
    /* Sidebar style */
    .sidebar .sidebar-content {
        background-color: #B2EBF2;
    }
    .sidebar .sidebar-content h1 {
        color: #03A9F4;
    }
    /* Dashboard summary style */
    .dashboard-summary {
        background-color: #E0F7FA;
        padding: 10px;
        margin-bottom: 20px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add logo to the sidebar above the title
#st.sidebar.image("logo.jpeg", width=500)  # Replace 'your_logo.png' with the path to your logo file

st.sidebar.title("Top Line Summary")
st.sidebar.markdown("""
In May, media coverage of UNICEF-related stories surged to 173, a notable increase from April's 116,
continuing a consistent upward trend over the past three months. The coverage predominantly focused on nutrition and child play initiatives.
Highlighted stories included development partners' commitment to combating food insecurity and malnutrition in Uganda, with the Prime Minister urging prioritization of nutrition efforts.
Additionally, UNICEF and the Minister of Education organized a national play day at Kololo, emphasizing the importance of play in child development.
This extensive coverage underscores the growing recognition of UNICEF's efforts and initiatives in Uganda.
""", unsafe_allow_html=True)

# Add tagline
st.sidebar.markdown("**Developed by Farsight Africa Group**", unsafe_allow_html=True)

# Display Child-related Issues Most Prominent in the Media
st.subheader("Child Related Issues Most Prominent in the Media")
child_issues_chart = px.bar(
    df_child_issues,
    x='Child Related Issues',
    y='Frequency',
    #title='Child Related Issues Most Prominent in the Media',
    labels={'Frequency': 'Number of Mentions', 'Child Related Issues': 'Issue'},
    color='Child Related Issues'
)
st.plotly_chart(child_issues_chart)

# Display Media Coverage of Child-related Issues by Media Type
st.subheader("Media Coverage of Child-related Issues by Media Type")
media_coverage_chart = px.pie(
    df_media_coverage,
    names='Media Type',
    values='Frequency',
    #title='Media Coverage of Child-related Issues by Media Type',
    hole=0.4
)
st.plotly_chart(media_coverage_chart)

# Display Top 10 Thematic Areas with the Most Media Coverage
st.subheader("Top 10 Thematic Areas with the Most Media Coverage")
top_thematic_areas_chart = px.bar(
    df_top_thematic_areas,
    x='Thematic Area',
    y='Number of Mentions',
    #title='Top 10 Thematic Areas with the Most Media Coverage',
    labels={'Number of Mentions': 'Number of Mentions', 'Thematic Area': 'Thematic Area'},
    color='Thematic Area'
)
st.plotly_chart(top_thematic_areas_chart)

# Display Free Space & Airtime Accorded to Child Rights Issues
st.subheader("Free Space & Airtime Accorded to Child Rights Issues")
free_space_chart = px.bar(
    df_free_space,
    x='Media Type',
    y='Amount',
    #title='Free Space & Airtime Accorded to Child Rights Issues',
    labels={'Amount': 'Amount (in billions)', 'Media Type': 'Media Type'},
    color='Media Type'
)
st.plotly_chart(free_space_chart)
