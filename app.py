import streamlit as st
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from PIL import Image

##Theme and page layout settings

CURRENT_THEME = "dark"
st.set_page_config(page_title="Kuldeep Garg",
                   layout="wide")
st.title("Kuldeep Garg :grey[(He/Him)]:technologist:")

## reducing the top margin of default streamlit application

def reduce_top_whitespace():
    st.markdown("""
    <style>

    .block-container
    {
        padding-top: 1rem;
        margin-top: 1rem;
    }

    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    reduce_top_whitespace()

##accessing the local css file to beautify the form in contacts section

def localcss(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css=localcss("./Style/style.css")

##importing the animation from lottie url

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coder = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_UBiAADPga8.json")

ETL_Aws_image=Image.open("./Images/ETL_AWS_Project.jpg")
Bulldozer_price_prediction_image=Image.open("./Images/Bulldozer_price_prediction.png")
Heart_disease_prediction_image=Image.open("./Images/Heart_disease_prediction.jpeg")

##creating the body for the appliaction pages

with st.container():
    selected=option_menu(
        menu_title  =None,
        options=['About','Projects','Tech Stack','Contact'],
        icons=['person','code-slash','star-fill','chat-left-dots-fill'],
        orientation='horizontal'
    )

## adding different conditions based on the pages.    

if selected=='About':
    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.write("""I possess a Bachelor's degree in Computer Science and currently serve as a Data Analyst at [DRYiCE MyXalytics](https://www.dryice.ai/products-and-platforms/my-xalytics). My primary responsibility involves utilizing a sophisticated reporting tool to aggregate data from diverse Cloud Sources and Monitoring Tools, storing it in respective databases. I then leverage this data to create multiple dashboards and reports, facilitating meaningful insights for end-users.""")
            st.write("""In my role, I proficiently collect and transform data to meet specific requirements, subsequently constructing reports and dashboards. I am well-versed in various business tools such as Zabbix, SNOW, Moogsoft, Nimsoft, and major cloud platforms including GCP, AWS, and Azure. Additionally, I have experience as a frontend developer for an internal HCL project, where I utilized the Flask Framework in Python.""")
            st.write("""Furthermore, I have delved into the realms of Machine Learning and Deep Learning, showcasing my skills through demonstration projects, which are accessible in the "Projects" section for your review.""")

        with col2:
            st_lottie(lottie_coder)    

##content for projects section
            
if selected=='Projects':
    with st.container():
        col5,col6=st.columns(2)
        with col5:
            st.image((ETL_Aws_image).resize((500,250)))
            st.write("#")
            st.image(Bulldozer_price_prediction_image.resize((500,350)))
            st.write("#")
            st.image(Heart_disease_prediction_image.resize((500,280)))


        with col6:
            st.subheader(":technologist: Data Visualization Using AWS Services")    
            st.write("In this project, I engaged in data visualization by leveraging AWS Services to transform raw Excel files containing information about YouTube videos into insightful visual representations.")
            st.write("#")
            st.write("#")
            st.write("#")

            st.subheader("	:moneybag: Bulldozer Price Prediction")    
            st.write("This project represents a comprehensive end-to-end endeavor focused on predicting Bulldozer prices. Through meticulous analysis of provided features, I successfully forecasted the anticipated prices of these bulldozers.")
            st.write("This project revolves around regression analysis, aiming to construct a robust model capable of accurately predicting bulldozer prices using provided features. Employing feature engineering, I tailored the model with a keen awareness of the temporal nature of the data.Conducting thorough Exploratory Data Analysis (EDA), I employed various models to minimize the Root Mean Squared Logarithmic Error (RMSLE). The ultimate choice was based on selecting the model that yielded the most optimal results.")
            st.write("[Check Out the Code](https://github.com/Kuldeepkdg/Machine_Learning_Projects/blob/main/Bulldozer_project_new.ipynb)")

            st.subheader("	:anatomical_heart: Heart Disease Prediction")    
            st.write("This project encompasses a comprehensive heart disease prediction initiative. It involves the prediction of the presence or absence of heart disease in individuals, determined by the analysis of provided features.")
            st.write("This is a classification project designed to develop a model capable of predicting whether an individual has heart disease. Through extensive Exploratory Data Analysis (EDA), I assessed various models, evaluating their accuracy scores. The chosen model is selected based on its optimal performance in addressing the specific challenges posed by the problem at hand.")
            st.write("[Check Out the Code](https://github.com/Kuldeepkdg/Machine_Learning_Projects/blob/main/heart_disease_project_end_to_end.ipynb)")


##content for contacts section
            
            
if selected=='Contact':
    st.write("Get In Touch")

    contact_form=("""
     <form action="https://formsubmit.co/kuldeepgarg065@gmail.com" method="POST" >
        <div class="form-group">
        <label for="Name">Name</label>
        <input type="text" name="name" class="form-control" id="name" placeholder="Name">
        </div>
        <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
        <input type="email" name="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
        </div>
        <div class="form-group">
        <label for="Message">Message</label>
        <input type="text" name="Message" class="form-control" id="Message" placeholder="Message">
        </div>
        <button type="submit" class="btn btn-success">Submit</button>
        </form>""")
    


    with st.container():
        col7,col8=st.columns((2,1))
        with col7:
            st.markdown(contact_form,unsafe_allow_html=True)    
    
