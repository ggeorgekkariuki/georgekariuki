import streamlit as st
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

# Load animation
education_url = "https://lottie.host/63fa3a56-a69b-46a1-b609-e75d4449edcc/Sr5cOLopsJ.json"
about_me_url = "https://lottie.host/2ece5997-22b7-471a-840b-897732198fad/isYcrkVd9p.json"
projects_url = "https://lottie.host/946c32ef-b98e-4a65-9b7c-d6ba879716c5/tFY90WiRta.json"
work_url = "https://lottie.host/6243771b-edce-4b43-8023-8bffdb526f8e/ddYEyTDjf4.json"
chicken_url = "https://lottie.host/0bf1cc6a-b299-4de0-af5c-5b02d6085a4b/JlrWkdTPmT.json"
tree_waving_url = "https://assets7.lottiefiles.com/packages/lf20_i9mxcD.json"

# Parse the URLS
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Page configuration
st.set_page_config(layout="wide")

# Name
st.title("George Kariuki - Website")

# Main Navigation Tab
selected2 = option_menu(None, ["Home", "Projects", "Employment", "Contact"], 
    icons=['house', 'cloud-upload', "list-task", "phone"], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},})

# TODO
# 1. Think about adding still images if the st_lottie images do not work

# About Us Page
if selected2 == "Home":
    with st.container():
        col1, col2 = st.columns([3,7])
        # Image
        with col1:
            st_lottie(load_lottieurl(url=about_me_url))

        # Profile  and Education
        with col2:
            st.header('Profile')
            st.markdown(
                """
                I am an innovative Python developer with expertise in machine learning, data analysis, and data science. 

                I am skilled in developing efficient algorithms and user-friendly applications. 
                
                I am seeking to apply my software expertise and data insights to a progressive company. 

                I have strong communication and interpersonal skills, with proven adaptability, in and about the workplace.

                ---
                """)

            # Education, Skills and Courses
            col3, col4, col5 = st.columns(3)

            # Skills
            with col5:
                st.markdown("""
                    ## Skills
                    **Programming Languages** - 
                    Python, Javascript
                            
                    **Libraries** - 
                    Scikit-learn, Pandas, Numpy, TensorFlow, Keras

                    **Database Management** - 
                    SQL, PostgreSQL, MySQL

                    **Data Analysis and Visualisation** - 
                    Matplotlib, Seaborn, Power BI, Tableau

                    **Presentation** - 
                    Streamlit, HTML, CSS

                    **Collaboration**
                    GitHub, Slack, Mattermost
                    """)
            
            # Education
            with col3:
                st.markdown("""
                    ## Education
                    **Moringa School**
                             
                    *Certificate - Data Science*
                    _2024 - Present_

                    **Strathmore University** 
                    
                    *Diploma - Association of Chartered Certified Accountants (ACCA)* | _2017 – 2022_

                    **Kenyatta University** 
                            
                    *Degree - Bachelor of Arts Degree in Economics and Sociology*
                    | _2012 – 2016_

                    """)
                
            # Courses
            with col4:
                st.markdown("""
                    ## Courses
                    **AFRALTI** 
                            
                    *CCNA - Certificate* | _2023_

                    **Udacity** 
                            
                    *Data Analysis - Nanodegree* | _2022_

                    **Techcamp Kenya** 
                            
                    *Certificate - Python Programming* |
                    _2019_
                    """)
            st.divider()

# TODO
# 1. Add more Details to the Projects
# 2. Add GitHub, Streamlit Links where applicable

# Projects
if selected2 == "Projects":
    with st.container():
        col1, col2 = st.columns([3,7])
        with col1:
            st_lottie(load_lottieurl(url=projects_url))

        with col2:
            st.header('My Projects')
            col3, col4 = st.columns(2)
            with col3:
                st.markdown("""
                ### Sentiment Analysis

                ***About the project***      
                                          
                A Natural Language Preprocessing project that analyses texts with a beautiful Streamlit based UI.
                                        
                _View this project on_  *[GitHub](https://github.com/ggeorgekkariuki/SentimentFlow_NLP)* or *[Streamlit](https://sentimentflow-nlp-project.streamlit.app/)* 
                                                            
                ---
                ### Picasso's Book Bar

                ***About the project***        
                                             
                This is a book recommendation system project using Unsupervised Machine Learning Algorithms, Python and Streamlit.
                                        
                _View this project on_  *[GitHub](https://github.com/ggeorgekkariuki/picasso-book-bar)* or *[Streamlit](https://picaapp-book-bar.streamlit.app/)*
                        
                ---
                ### King County Real Estate

                ***About the project***   
                                              
                This was a supervised machine learning algorithm project to predict the prices of developed houses in America based on historical data.
                                        
                _View this project on_  *[GitHub](https://github.com/ggeorgekkariuki/Kings-Country-Housing-Project)*.
                                        
                ---            
                """)

            with col4:
                st.markdown("""
                ### COVID Analysis
                ***About the project***           
                                             
                An SQL project aimed to explore the effects of COVID from historical data. The project was visualised using Tableau.

                _View this project on_  *[GitHub](https://github.com/ggeorgekkariuki/COVID-Portfolio)* or *[Tableau](https://public.tableau.com/app/profile/george.kariuki7367/viz/COVIDDashboard_16646179556420/Dashboard1)* 

                ---
                ### Microsoft Movie Data Analysis      
                          
                ***About the project***       
                           
                An optimisation of a makeshift company's profitability using Pandas, NumPy and Matplotlib.  
                                    
                _View this project on_ *[GitHub](https://github.com/ggeorgekkariuki/Microsoft-Movie-Analysis)*. 
                                        
                ---
                ### Ford Go Bikes Analysis     
                          
                ***About the project***       
                           
                The goal of this project was to master visualisation using MatplotLib and Seaborn to analyse historical data about the Ford GO Bikes data.
                                    
                _View this project on_ *[GitHub](https://github.com/ggeorgekkariuki/Ford-Go-Bikes-Analysis)*. 
                                        
                ---""")

# All Employment History
if selected2 == "Employment":
    with st.container():
        col1, col2 = st.columns([3,7])
        with col1:
            st_lottie(load_lottieurl(url=work_url))

        with col2:
            st.header('Employment History')
            st.markdown("""
### Financial and Management Accounting Assistant
***International House Limited*** | _Oct 2019 – Jan 2024 | Nairobi, Kenya_                   
- Utilized data visualizations to provide insights for management, contributing to a 10% decrease in operating cost.                        
- Developed and maintained management reporting systems using Excel, Tableau, and Power BI.                     
- Analyzed and supported daily accounting tasks, improving processes through data analysis.                
- Enhanced cash flow management by leveraging data analysis techniques reducing debtors.               
- Conducted forecasting and trend analysis using statistical models.
- Created financial models to support forecasting and business planning increasing forecasting accuracy by 15%.
---
### Integrity Assurance and Communication Officer                        
***Kenya National Highways Authority (KENHA)*** | _2018 – 2019 | Nairobi, Kenya_
- Led 7 community sensitization seminars and participated in national events to promote organizational mission and vision.
- Developed and implemented 2 policies focusing on integrity and ethics.
- Maintained customer resolution processes and led training to improve customer experience.
- Developed a complaint tracking system for better customer management.
---                        
### Junior Programmer and Android Developer 
***Aliquot Limited (Fintech company)*** | _2017 – 2018 | Nairobi, Kenya_
- Researched and maintained 1 Android and web application, ensuring code efficiency.
- Managed MySQL database and provided insights through SQL queries.
- Improved website user experience using HTML, CSS, and JavaScript.
---
""")
            
# TODO
# 1. Add Contact Page Including Email, CV, Github and LinkedIn
if selected2 == "Contact":
        col1, col2 = st.columns([3,7])
        with col1:
            st_lottie(load_lottieurl(url=tree_waving_url))

        with col2:
            st.header('Contact Me')

            st.write(f"""
### George Kariuki                     
Email me at ggeorgekkariuki@gmail.com
                     
View My Github Account [here.](https://github.com/ggeorgekkariuki/)
                     
View My LinkedIn Account [here.](https://linkedin.com/in/george-gachugu/)""")
            
            st.link_button("View My CV", "https://flowcv.com/resume/maw7k8s9hs")