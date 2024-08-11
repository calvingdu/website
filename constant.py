import streamlit as st  

skill_col_size = 5

def menu():
    bar0, bar1, bar2, bar3, bar4= st.columns([0.1,1,1,1,1])
    bar1.page_link("app.py", label="Introduction", icon="🏠")
    bar2.page_link("pages/Experience.py", label= "Experience", icon="📚")
    bar3.page_link("pages/Portfolio.py", label="Portfolio", icon="💻")
    bar4.page_link("pages/Contacts.py", label="Contacts", icon="🌏")
    st.write("")

#publication_url --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
linkedin_logo = '''                                                                                                                                          
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-linkedin" style="font-size: 28px;"></i>                                                                           
'''

github_logo = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-github" style="font-size: 28px;"></i>                                                                           
'''

# personal info (for main page) --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
info = {'brief':
              """    
                Dedicated individual with a background in statistical programming & data science with an interest in finance, economics and technology.

                Graduating in May 2025

                **Everything Data**
              """,
        'name':'Calvin Du', 
        'education':'University of British Columbia',
        'location':'Vancouver, BC',
        'interest':'Data Engineering, Data Science, Machine Learning',
        'skills':['Python','SQL'],
        }

# Experience --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#[[header, subheader, date, location, content, link, link_url], [...], etc.]

Experience = []      

# Portfolio --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#     {'project1':[HEADER, CONTENT]
#      'project2':[HEADER, CONTENT]
#      ...}

Portfolio = { 1:[':blue[Deis]Evaluation - Course Evaluation Website',
              """
              Launched a course evaluation web app for Brandeis students to review and share courses, exceeding 200+ active users.
              Designed the whole UI with Figma and Implemented front end with Javascript, HTML/CSS in a MERN Stack.
              """],
              2:['Data Visualization in :orange[D3.js]',
                  """
                Created a data visualization web app for Massachusetts police expenditure data using D3.js.
                """],
              3:[':blue[LLM] Desktop ChatApp',
                """
                - Designed and developed a cross-platform **desktop LLM Chat app**, enabling chat over user-upload dataset; providing a more accurate response to domain-specific inquiries than ChatGPT.
                - Utilized Embedding and Searching from **OpenAI API** to optimize Chat app’s response. Split the user-upload file into small chunks; used OpenAI Embedding model to vectorize each chunk and save them into Qdrant database. Transform user query to vector using OpenAI, and then inquire the top match text chunk from Qdrant database using topk value.
                """],
              4:[':orange[Anthropology] Research Project - A Timeless Building',
                """
                - An **qualitative anthropological research** on the preservation and adaption of historical sites; as final project, received the highest score in class.
                - My fieldwork includes interviewing educators, examing archive, on-site obervation. Through my fieldwork at King’s Chapel, I argued for a humane approach to preserving historic sites, that seeks a balance between **maintaining the historical significance and the sites’ adaptations to societal changes**.
                """],
              5:[':green[RAG] playground',  
                """
                - Developed a **RAG** chatbot that support difference choices over Embedding model, chunking strategy, top k retreival, LLM model, prompt engineering, and meta-data retreival search.
                - Implemented the file uploading workflow; Utilized **Langchain splitter** module and Python script to clean and chunk the uploaded file and use Huggingface sentence transformers and **Pinecone** to vectorize and store data.
                - Used SpaCy NER model to retreive meta data from prompt and ran a hybrid search using meta-data and vector.
                """]
            }
              
# Contacts --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
email = "calvingdu@gmail.com"
linkedin_link = "www.linkedin.com/in/calvingdu/"
github_link = "https://github.com/calvingdu"


# iframes --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
figma_iframe = '<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1" allowfullscreen></iframe>'

figma_link = "https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1"

StoryMap_iframe = "https://storymaps.arcgis.com/stories/dfb9689618e343cf9f6ef36d9a8329a7?header"

Evaluation_html = '''
                <div class="github-card" data-github="Rsirp0c/deis-course-evaluation" data-width="400" data-height="" data-theme="default"></div>
                <script src="https://cdn.jsdelivr.net/github-cards/latest/widget.js"></script>                
                '''
