import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Algorithmic Artistry", page_icon=":paintbrush:", layout="wide")

# Define the home page
def home():
    st.title("Algorithmic Artistry")
    st.write("""
    Welcome to Algorithmic Artistry, a unique competition where participants create visually stunning digital art using deep learning and GANs (Generative Adversarial Networks). 
    The competition combines creativity with advanced AI techniques, challenging participants to generate beautiful and intricate designs through neural networks. 
    This competition highlights the intersection of art and technology, encouraging participants to explore new ways of expression through AI.
    """)
    st.image("https://keras.io/img/examples/generative/neural_style_transfer/neural_style_transfer_19_0.png", caption="Skyline of Paris in Van Gogh Style")

# Define the competition details page
def competition_details():
    st.title("Competition Details")
    st.write("### Key Features:")
    st.write("1. **Deep Learning Art**: Participants use deep learning techniques and GANs to create visual art.")
    st.write("2. **Themes and Prompts**: Each round has a specific theme or prompt that guides the artistic creation.")
    st.write("3. **Interactive Showcase**: An online gallery where participants' artworks are displayed and can be interacted with.")
    st.write("4. **Judging Criteria**: Artworks are judged based on originality, technical complexity, and aesthetic appeal.")
    st.write("5. **Learning Resources**: Tutorials and resources on deep learning and GAN techniques for creating art.")
    st.write("6. **Participant Testimonials**: Hear from past participants about their experience.")
    
    # Testimonials section
    st.subheader("Participant Testimonials")
    st.write("""
    *"Participating in Algorithmic Artistry was a transformative experience. It pushed me to think creatively and technically."* - John Doe \n
    *"The themes were challenging yet inspiring. I learned so much about GANs and creative AI!"* - Jane Smith \n
    """)

# Define the submit artwork page

def submit_artwork():
    st.title("Submit Your Artwork")
    text = """
    <h3>Make sure you submit your artwork AND GitHub repository.</h3>
    """
    st.markdown(text, unsafe_allow_html=True)
    
    artwork_file = st.file_uploader("Upload your artwork file", type=["png", "jpg", "gif"])
    github_link = st.text_input("Enter the GitHub repository link for your code")

    if st.button("Submit"):
        if artwork_file is not None and github_link:
            st.success("Your artwork and GitHub repository link have been submitted successfully!")
        if github_link is None and artwork_file is None:
            st.warning("Please enter the GitHub repository link before submitting.")
        if artwork_file is None:
            st.warning("Please upload your artwork file before submitting.")
            


# Define the learning resources page
def learning_resources():
    st.title("Learning Resources")
    st.write("Check out these resources to learn more about deep learning and GANs for creating art:")
    
    # Add links or embed tutorials/resources here
    st.markdown("""
    - [TensorFlow](https://www.tensorflow.org) - An open source library for machine learning and deep learning.
    - [PyTorch](https://pytorch.org) - An open source machine learning library based on the Torch library.
    - [DeepArt.io](https://deepart.io) - Turn photos into artwork using neural networks.
    - [Runway ML](https://runwayml.com) - A platform for machine learning models for artists.
    - [GANs in Action](https://www.manning.com/books/gans-in-action) - A comprehensive book on how to use GANs.
    """)

     # Embed tutorial videos side by side
    col1, col2 = st.columns(2)
    with col1:
        st.video("https://www.youtube.com/watch?v=8L11aMN5KY8")
    with col2:
        st.video("https://www.youtube.com/watch?v=5WoItGTWV54")

# Define the FAQ page
def faq():
    st.title("Frequently Asked Questions (FAQ)")
    st.write("### Q) How do I participate in the competition?")
    st.write("A) Simply sign up on our website, create your artwork using deep learning and GANs, and submit your entry through the 'Submit Artwork' page.")
    st.write("### Q) What tools and frameworks can I use?")
    st.write("A) You can use any deep learning framework you are comfortable with, such as TensorFlow, PyTorch, or any other GAN libraries.")
    st.write("### Q) Are there any restrictions on the themes?")
    st.write("A) Each round will have a specific theme or prompt. Participants should adhere to the theme while creating their artwork.")
    st.write("### Q) How are the artworks judged?")
    st.write("A) Artworks are judged based on originality, technical complexity, and aesthetic appeal by a panel of experts in the fields of AI and art.")

# Define the interactive gallery page
def interactive_gallery():
    st.title("Interactive Gallery")
    st.write("Explore the stunning artworks submitted by our participants:")
    
    # Placeholder for gallery - this can be replaced with actual gallery code
    st.image("https://upload.wikimedia.org/wikipedia/commons/a/a2/Mona_lisa_the_starry_night_o_lbfgs_i_content_h_720_m_vgg19_cw_100000.0_sw_30000.0_tv_1.0.jpg", caption="Artwork by John Smith")
    st.image("https://tensorflow.org/tutorials/generative/images/stylized-image.png", caption="Artwork by Jane Doe")
    st.image("https://www.researchgate.net/publication/335441628/figure/fig1/AS:796702424457216@1566960068719/State-of-the-art-neural-style-transfer-methods-eg-Johnson-et-al-20-tend-to-scatter.ppm", caption="Artwork by Alex")

# Define the pages
pages = {
    "Home": home,
    "Competition Details": competition_details,
    "Submit Artwork": submit_artwork,
    "Learning Resources": learning_resources,
    "FAQ": faq,
    "Interactive Gallery": interactive_gallery,
}

# Create an option menu for navigation
with st.sidebar:
    st.image('gdsc_logo.png')
    selected = option_menu(
        menu_title="Navigation",
        options=list(pages.keys()),
        icons=["house", "trophy", "upload", "book", "question-circle", "images"],
        default_index=0,
        orientation="vertical",
    )

# Call the selected page function
pages[selected]()

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
