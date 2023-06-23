import pandas as pd
import random
import streamlit as st

# 원본 데이터프레임 생성
pose = pd.read_csv('pose.csv', encoding='ms949')
practice = pd.read_csv('practice.csv', encoding='ms949')
dictation = pd.read_csv('dictation.csv', encoding='ms949')

# 랜덤한 결과 출력하는 함수
def show_random_results():
    # 랜덤한 4개의 운동 선택
    random_practice = random.sample(practice['name'].tolist(), 4)
    random_pose = random.sample(pose['pose'].tolist(), 1)
    random_dictation = random.sample(dictation['question'].tolist(), 4)

    # 새로운 데이터프레임 생성
    selected_practice = practice[practice['name'].isin(random_practice)]
    selected_pose = pose[pose['pose'].isin(random_pose)]
    selected_dictation = dictation[dictation['question'].isin(random_dictation)]

    # 결과 출력
    st.write("Selected Practice:")
    practice_results = [f"{i+1}. {name}" for i, name in enumerate(selected_practice['name'])]
    st.write("\n".join(practice_results))

    st.write("Selected Pose:")
    st.write(selected_pose.pose.unique()[0])


    st.write("Selected Dictation:")
    dictation_results = [f"{i+1}. {question}" for i, question in enumerate(selected_dictation['question'])]
    st.write("\n".join(dictation_results))

    st.write("\nSelected Pose answer:\n")
    pose_name = [f"{i+1}. {name}" for i, name in enumerate(selected_pose['name'])]
    st.write("\n".join(pose_name))

    st.write("\nSelected Dictation answer:\n")
    dictation_answer = [f"{i+1}. {answer}" for i, answer in enumerate(selected_dictation['answer'])]
    st.write("\n".join(dictation_answer))


# Streamlit 애플리케이션 구성
st.title("생체사 2급 실기/구슬 모의 평가")
start_button = st.button("시작")

# Start 버튼이 클릭되면 결과 출력
if start_button:
    show_random_results()
