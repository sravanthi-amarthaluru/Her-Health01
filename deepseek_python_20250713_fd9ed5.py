import streamlit as st
import os

# Initialize session state
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Load CSS with robust path handling
def load_css():
    css_paths = [
        "assets/style.css",          # Default path
        "her-health/assets/style.css", # Streamlit Cloud path
        "style.css"                  # Fallback path
    ]
    
    for path in css_paths:
        try:
            if os.path.exists(path):
                with open(path, "r") as f:
                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
                return
        except:
            continue
    
    st.warning("Note: Default styling applied (CSS file not found)")

load_css()

# --- App UI ---
st.title("🏥 HerHealth+ Personalized Recommendations")

# Input Form
with st.form("health_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=1, max_value=100, value=25)
    with col2:
        gender = st.selectbox("Gender", ["Female", "Male", "Other"])
    
    days = st.slider("Days per week for health focus:", 1, 7, 3)
    health_issues = st.text_input("Any specific health concerns? (optional)")
    
    submitted = st.form_submit_button("Generate My Plan")
    
    if submitted:
        st.session_state.submitted = True

# Display Results
if st.session_state.submitted:
    st.success("Here's your personalized health plan!")
    
    # Hygiene Tips Card
    st.markdown("""
    <div class="card">
        <div class="card-header">🧼 Hygiene Tips</div>
        <div class="card-content">
            <ul>
                <li>Shower daily with mild soap</li>
                <li>Wash hands frequently</li>
                <li>Brush teeth twice daily</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Diet Plan Card
    st.markdown("""
    <div class="card">
        <div class="card-header">🍎 Diet Plan</div>
        <div class="card-content">
            <ul>
                <li>Eat 5 servings of fruits/vegetables daily</li>
                <li>Drink 8 glasses of water</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)