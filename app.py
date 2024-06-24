import streamlit as st
import pandas as pd

st.set_page_config(page_title="학습 데이터의 안전한 관리와 활용", layout="wide")

st.title("소중한 학습 데이터, 안전하게 활용하려면?")

st.markdown("## 목차")
st.markdown("""
1. 학습 데이터의 종류와 개인정보보호법 등 관련 법규
2. 학습 데이터 및 활동 결과물 관리 방법 및 유의사항
3. 학습 데이터의 한계 인식과 활용 시 유의점
4. 대시보드 분석 및 개별 맞춤 학습 설계
""")

tab1, tab2, tab3, tab4 = st.tabs(["데이터와 법규", "데이터 관리", "데이터 한계", "대시보드 분석"])

with tab1:
    st.header("1. 학습 데이터의 종류와 개인정보보호법 등 관련 법규")
    
    st.subheader("AI 개인정보보호 6대 원칙")
    principles = [
        "적법성: 개인정보 처리의 근거는 적법·명확해야 한다.",
        "안전성: 개인정보를 안전하게 처리하고 관리한다.",
        "투명성: 개인정보 처리 내역을 정보주체가 알기 쉽게 공개한다.",
        "참여성: 개인정보 처리에 대한 소통체계를 갖추고 정보주체의 권리를 보장한다.",
        "책임성: 개인정보 처리에 대한 관리책임을 명확히 한다.",
        "공정성: 개인정보를 수집목적에 맞게 처리하여 사회적 차별·편향 등 발생을 최소화한다."
    ]
    for principle in principles:
        st.markdown(f"- {principle}")

with tab2:
    st.header("2. 학습 데이터 및 활동 결과물 관리 방법 및 유의사항")
    
    st.subheader("데이터 관리 주요 사항")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 신뢰성 확보")
        st.markdown("- 데이터의 정확성 검증")
        st.markdown("- 데이터 클렌징 및 정제")
    with col2:
        st.markdown("### 데이터 활용 동의")
        st.markdown("- 명시적 동의 필요")
        st.markdown("- 동의 범위 및 목적 명확화")

    st.subheader("데이터 보안")
    security_measures = st.multiselect(
        "중요한 데이터 보안 조치를 선택하세요:",
        ["암호화", "접근 제어", "데이터 마스킹", "정기적인 보안 감사"],
        ["암호화", "접근 제어"]
    )

with tab3:
    st.header("3. 학습 데이터의 한계 인식과 활용 시 유의점")
    
    limitations = {
        "데이터 편향성": "지역별 데이터 차이로 인한 편향 가능성",
        "데이터 범위의 한계": "교실 내 데이터만으로는 학생의 전체적인 학습 환경 파악 어려움",
        "개인정보보호 이슈": "데이터 활용에 대한 동의 및 윤리적 문제",
        "데이터 수집의 어려움": "학습 과정 전반을 포괄적으로 수집하기 어려움",
        "데이터 분석 기술의 한계": "학생 개인별 특성을 정확히 파악하기 어려운 분석 기술의 한계"
    }
    
    for limitation, description in limitations.items():
        st.markdown(f"### {limitation}")
        st.markdown(description)
        st.markdown("---")

with tab4:
    st.header("4. 대시보드 분석 및 개별 맞춤 학습 설계")
    
    st.subheader("대시보드 활용 예시")
    st.image("/api/placeholder/600/400", caption="대시보드 예시 이미지")
    
    st.subheader("개별 맞춤 학습 설계 고려사항")
    considerations = [
        "학생/학급별 학업 참여도",
        "학습 성취 추이",
        "교과 흥미 현황",
        "개인별 학습 스타일",
        "학습 환경 요인"
    ]
    
    selected_considerations = st.multiselect(
        "개별 맞춤 학습 설계 시 고려해야 할 요소를 선택하세요:",
        considerations,
        ["학생/학급별 학업 참여도", "학습 성취 추이"]
    )

st.markdown("---")
st.markdown("## 정리")
st.info("학습 데이터를 안전하고 효과적으로 활용하기 위해서는 개인정보보호 원칙을 준수하고, 목적에 맞게 데이터를 수집 및 활용해야 하며, 개별 학습 데이터를 바탕으로 학생 성장을 위한 맞춤형 학습 방안을 설계해야 합니다.")

if st.button("참고문헌 보기"):
    st.markdown("""
    - AI 디지털교과서 개발 가이드라인, 2023, 교육부
    - 아동청소년 개인정보보호 가이드라인, 2022, 개인정보보호위원회
    """)
