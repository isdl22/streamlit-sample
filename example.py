import pandas as pd
import random
import streamlit as st

# 원본 데이터프레임 생성
pose = pd.read_csv('pose.csv', encoding='ms949')
practice = pd.read_csv('practice.csv', encoding='ms949')
dictation = pd.read_csv('dictation_1.csv', encoding='ms949')

# 랜덤한 결과 출력하는 함수
def show_random_results():
    # 랜덤한 2개의 대분류 선택
    random_categories = random.sample(dictation['gubun'].unique().tolist(), 2)
    
    selected_dictation = pd.DataFrame()
    
    for category in random_categories:
        # 대분류에 해당하는 데이터 랜덤으로 2개 선택
        random_questions = random.sample(dictation[dictation['gubun'] == category]['question'].tolist(), 2)
        
        # 선택된 질문을 데이터프레임에 추가
        selected_dictation = selected_dictation.append(dictation[(dictation['gubun'] == category) & (dictation['question'].isin(random_questions))])
    
    # 결과 출력
    st.write("1. 실기 자세 문제:")
    practice_results = [f"{i+1}. {name}" for i, name in enumerate(practice['name'].sample(4))]
    st.write("\n".join(practice_results))

    st.write("2. 실기 포즈 문제:")
    st.write(pose['pose'].sample(1).values[0])

    st.write("3. 구술 문제:")
    dictation_results = [f"{i+1}. {question}" for i, question in enumerate(selected_dictation['question'])]
    st.write("\n".join(dictation_results))

    st.write("\n 실기 포즈 이름:\n")
    pose_name = [f"{i+1}. {name}" for i, name in enumerate(pose['name'].sample(1))]
    st.write("\n".join(pose_name))

    st.write("\n 구술 문제 정답:\n")
    dictation_answer = [f"{i+1}. {answer}" for i, answer in enumerate(selected_dictation['answer'])]
    st.write("\n".join(dictation_answer))


# Streamlit 애플리케이션 구성
st.title("생체사 2급 실기/구슬 모의 평가")
start_button = st.button("시작")

# Start 버튼이 클릭되면 결과 출력
if start_button:
    show_random_results()
