# To run on Local
# from dotenv import load_dotenv
# load_dotenv()


# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("hi!")
# print(result)


from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()
chat_model.predict("hi!")


# content = "코딩"

# result = chat_model.predict(content + "에 대한 시를 써줘")
# print(result)


# import streamlit as st  

# st.title('인공지능 시인')
# # st.title('_Streamlit_ is :bule[cool] :sunglasses:')
# import streamlit as st

# title = st.text_input("시의 주제를 제시해주세요.")
# st.write("시의 주제는", title)




import streamlit as st

result = chat_model.predict(content + "에 대한 시를 써줘")
print(result)


import streamlit as st  

st.title('인공지능 시인')
content = st.text_input("시의 주제를 제시해주세요.")

if st.button("시 작성 요청하기"):
    with st.spinner("시작성 중...", show_time=True):
    result = chat_model.predict(content + "에 대한 시를 써줘")
    st.write(result)

# result = chat_model.predict(content + "에 대한 시를 써줘")
# print(result)







# howto run
# bash streamlit run main.py