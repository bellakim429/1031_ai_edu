import requests
import streamlit as st

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "b97f8190-974a-11ef-994e-b7bbb9cee7dde5ec4b24-e116-4773-919e-06a0754b2ca7"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to something you want your machine learning model to classify

while True:
    #question = input("도쿄여행 장소추천 가이드 입니다.\n 원하는 활동키워드를 입력해주세요.\n예시 카테고리 : 쇼핑, 음식, 관광, 카페 \n질문이 끝나면'나가기'를 입력해주세요\n")
    question = st.text_input("도쿄여행 지역추천 가이드 입니다.\n 원하는 활동키워드를 입력해주세요.\n예시 카테고리 : 쇼핑, 음식, 관광, 카페 \n질문이 끝나면'나가기'를 입력해주세요\n>>>",'')
    if len(question)>0:

        if (question =="나가기"):
            break

        demo = classify(question)

        label = demo["class_name"]
        confidence = demo["confidence"]

        if confidence < 50 :
            st.write("조금 더 정확하게 입력해주세요\n")

        elif label == "shopping":
            st.write("쇼핑을 위해서는 신주쿠와 하라주쿠가 유명합니다.\n백화점에서 쇼핑 시 외국인이시라면 Guest card와 tax free도 잊지마세요.\n\n")
            st.write("답변 정확도 : %d%% \n\n" % ( confidence))
            
        elif label == "sightseeing":
            st.write("시간이 충분하시면 관광은 근교 소도시로 추천드려요. \n도쿄에서 2시간거리의 후지마을이나 요코하마는 요즘 인기 명소입니다!\n\n")
            st.write("시간이 널널하지 않으시다면 도쿄타워근처시바공원이나, 아키하바라, 시부야스카이, 오다이바지역을 둘러보기 좋습니다.\n\n")
            st.write("답변 정확도 : %d%% \n\n " % ( confidence))
            
        elif label == "Food":
            st.write("시부야에는 맛있는 식당들이 많습니다. 하지만 23시정도면 거의 문들 닫으니 일찍 움직이시길 바래요.\n\n")
            st.write("좀 더 늦은 시간에 즐기고 싶으시다면 신바시 근처를 추천드립니다!\n\n")
            st.write("답변 정확도 : %d%%\n\n " % ( confidence))
        
        elif label =="Cafe":
            st.write("도쿄에는 오래된 카페들도 많은데요, 특히나 요즘 긴자의 트리콜로레가 유명합니다\n\n")
            st.write("케이크를 좋아하신다면 도쿄 곳곳에 있는 하브스를 추천드립니다!\n\n")
            st.write("답변 정확도 : %d%% \n\n" % ( confidence))
    else:
        st.write("Please enter a data\n")