# ==========================================
# 🚨 [초긴급] _loss 에러 원천 차단 우회막 (가장 먼저 실행되어야 함)
# ==========================================
import sys
import types

if 'sklearn.ensemble._loss' not in sys.modules:
    dummy_loss_module = types.ModuleType('sklearn.ensemble._loss')
    class DummyLoss:
        pass
    dummy_loss_module.LossFunction = DummyLoss
    sys.modules['sklearn.ensemble._loss'] = dummy_loss_module
# ==========================================

import streamlit as st
import pandas as pd
import joblib
import time
import random

# 1. 페이지 세팅
st.set_page_config(page_title="Project: 제2의 지구를 찾아서", page_icon="🛸", layout="wide")

# 🎨 CSS: 사이드바까지 완벽한 딥블랙 통일
st.markdown("""
    <style>
    .stApp, [data-testid="stSidebar"] {
        background-color: #090B0E !important;
        color: #E2E8F0 !important;
    }
    [data-testid="stSidebar"] {
        border-right: 1px solid #1E293B !important;
    }
    div[data-testid="stSlider"] label {
        color: #00f0ff !important;
        font-weight: bold;
        font-size: 15px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        border: 2px solid #00f0ff;
        background: #0F172A;
        color: #00f0ff;
        font-size: 18px;
        font-weight: bold;
        padding: 15px;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 0 15px rgba(0, 240, 255, 0.2);
    }
    .stButton>button:hover {
        background: #00f0ff;
        color: #090B0E;
        box-shadow: 0 0 35px #00f0ff;
    }
    .glass-panel {
        background: rgba(15, 23, 42, 0.9);
        padding: 35px;
        border-radius: 16px;
        border: 1px solid #1E293B;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
        text-align: center;
        margin-bottom: 25px;
    }
    .neon-title {
        color: #FFFFFF;
        text-shadow: 0 0 15px rgba(0, 240, 255, 0.8);
        font-family: 'Courier New', monospace;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 🤖 모델 로드
@st.cache_resource
def load_model():
    return joblib.load("exoplanet_model.pkl")

# 로딩 화면용 랜덤 우주 이미지 리스트
OPENING_IMAGES = [
    "https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", 
    "https://images.unsplash.com/photo-1614313913007-2b4ae8ce32d6?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", 
    "https://images.unsplash.com/photo-1506318137071-a8e063b4bec0?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", 
    "https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", 
    "https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"  
]

try:
    model = load_model()

    if 'entered' not in st.session_state:
        st.session_state.entered = False
    
    if 'bg_img' not in st.session_state:
        st.session_state.bg_img = random.choice(OPENING_IMAGES)

    # ==========================================
    # 🌌 PHASE 1: 오프닝 대문 화면
    # ==========================================
    if not st.session_state.entered:
        st.write("\n" * 2)
        st.markdown("""
            <div class='glass-panel' style='border-top: 4px solid #00f0ff;'>
                <p style='color: #00f0ff; letter-spacing: 6px; font-size: 13px;'>DEEP SPACE EXPLORATION SYSTEM</p>
                <h1 class='neon-title' style='font-size: 38px;'>🪐 [Project] 제2의 지구를 찾아서</h1>
                <p style='color: #94A3B8; font-size: 15px; margin-top: 10px;'>Gradient Boosting 알고리즘 기반 외계행성 기후 데이터 분석 시스템</p>
            </div>
        """, unsafe_allow_html=True)
        
        _, img_col, _ = st.columns([1, 1.8, 1])
        with img_col:
            st.image(st.session_state.bg_img, caption="[📡 실시간 포착된 미개척지 외계행성 스캔 이미지]", use_container_width=True)
        
        st.write("\n")
        _, btn_col, _ = st.columns([1, 1.2, 1])
        with btn_col:
            if st.button("🛸 탐사 네비게이션 가동 및 진입"):
                with st.spinner("🤖 양자 신경망 분석기 가동 중..."):
                    progress_bar = st.progress(0)
                    for percent_complete in range(100):
                        time.sleep(0.01)
                        progress_bar.progress(percent_complete + 1)
                st.session_state.entered = True
                st.session_state.bg_img = random.choice(OPENING_IMAGES)
                st.rerun()

    # ==========================================
    # 🛰️ PHASE 2: 메인 시뮬레이터 조종석
    # ==========================================
    else:
        with st.sidebar:
            st.markdown("<h3 style='color: #00f0ff; text-align:center;'>🛰️ NAVI CONTROL</h3>", unsafe_allow_html=True)
            st.write("---")
            st.markdown("""
            🎯 **지구 매칭 꿀팁**<br>
            * **행성 크기/무게**: 1.0 근처<br>
            * **햇빛 세기**: 1.0 근처<br>
            * **측정 온도**: 15°C 근처<br>
            이렇게 맞추면 대박 터집니다!
            """, unsafe_allow_html=True)
            st.write("\n" * 4)
            if st.button("⬅️ 시스템 종료"):
                st.session_state.entered = False
                st.rerun()

        # 메인 대시보드 상단 레이아웃
        title_col, view_col = st.columns([1.5, 1])
        
        with title_col:
            st.write("\n" * 2)
            st.markdown("<h1 class='neon-title' style='text-align:left; font-size:35px;'>🎛️ [Project] 제2의 지구를 찾아서</h1>", unsafe_allow_html=True)
            st.markdown("<p style='color: #94A3B8; font-size:16px;'>탐사선 제어 데스크입니다. 인공지능 예측 모델을 가동하기 위해 새로 관측된 행성의 환경 제원을 조절하세요.</p>", unsafe_allow_html=True)
        
        with view_col:
            st.image("https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80", 
                     caption="🛰️ 탐사선 전면 윈도우 시야", use_container_width=True)

        st.write("---")

        # 3열 슬라이더 레이아웃
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("<h4 style='color: #FFF;'>[01] 행성 덩치 스펙</h4>", unsafe_allow_html=True)
            mass = st.slider("행성 몸무게 (지구의 몇 배?)", 0.1, 10.0, 1.0, 0.1)
            radius = st.slider("행성 크기 (지구의 몇 배?)", 0.1, 5.0, 1.0, 0.1)

        with col2:
            st.markdown("<h4 style='color: #00f0ff;'>[02] 대기 기후 환경 (핵심)</h4>", unsafe_allow_html=True)
            flux = st.slider("받는 햇빛 세기 (지구의 몇 배?)", 0.1, 5.0, 1.0, 0.1)
            celsius_temp = st.slider("우주선 측정 온도 (°C)", -100, 100, 15, 1)
            temp = celsius_temp + 273.15 

        with col3:
            st.markdown("<h4 style='color: #FFF;'>[03] 공전 궤도 정보</h4>", unsafe_allow_html=True)
            period = st.slider("한 바퀴 공전 주기 (며칠?)", 10, 1000, 365, 5)
            distance = st.slider("태양(별)과의 거리 (지구-태양 거리의 몇 배?)", 0.1, 10.0, 1.0, 0.1)

        st.write("---")

        if st.button("⚡ QUANTUM ANALYSIS START (지구 유사도 연산)"):
            input_df = pd.DataFrame([[mass, radius, flux, temp, period, distance]], 
                                    columns=['P_MASS', 'P_RADIUS', 'P_FLUX', 'P_TEMP', 'P_PERIOD', 'P_DISTANCE'])
            
            pred = model.predict(input_df)
            esi = pred[0] * 100

            st.markdown(f"""
                <div class="glass-panel" style='border: 2px solid #00f0ff; background: #0B132B;'>
                    <h3 style='color: #00f0ff; letter-spacing: 3px; font-size:15px;'>ANALYZE COMPLETE</h3>
                    <p style='color: #94A3B8; margin: 0; font-size:13px;'>지구 유사도 지수 (Earth Similarity Index)</p>
                    <h1 style='font-size: 70px; color: #FFFFFF; font-family: monospace; margin: 5px 0;'>{esi:.2f}%</h1>
                </div>
            """, unsafe_allow_html=True)

            if esi >= 95.0:
                st.balloons()
                st.snow()
                st.success("👑 **[GOD GRADE]** 전 인류가 이주해도 손색없는 완벽한 '제2의 지구'를 개척했습니다!!")
            elif esi >= 80.0:
                st.balloons()
                st.success("🌟 **[GRADE A]** 환경이 아주 쾌적합니다. 인류가 살아가기 적합합니다.")
            elif esi >= 50.0:
                st.warning("⛺ **[GRADE C]** 기후가 조금 척박하지만 기지 구축은 가능한 행성입니다.")
            else:
                st.error("💀 **[GRADE F]** 생명체가 절대로 살 수 없는 가혹한 죽음의 행성입니다.")

except Exception as e:
    st.error(f"⚠️ 시스템 오류: {e}")