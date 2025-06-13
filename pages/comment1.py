import streamlit as st
from pymongo import MongoClient
from datetime import datetime
import uuid
from streamlit_modal import Modal
import hashlib

import os

# လက်ရှိ directory ကို print ထုတ်ပါ
print("Current Directory:", os.getcwd())

# လက်ရှိ directory ထဲမှာရှိတဲ့ဖိုင်တွေကို ကြည့်ပါ
print("Files here:", os.listdir())

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["comment_system"]
comments_collection = db["comments1"]
users_collection = db["users"]

# Initialize session state
if 'user' not in st.session_state:
    st.session_state.user = None
if 'clear_text' not in st.session_state:
    st.session_state.clear_text = False

st.set_page_config(
    page_title="MLLIP Name Checker",
    page_icon="🎙️",
    layout="wide",
  
)



POST_ID = "post456"

# CSS Styling
st.markdown("""
<style>
    .comment-box {
        border-left: 3px solid #4CAF50;
        padding: 10px;
        margin-left: 20px;
        background-color: #f9f9f9;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .user {
        font-weight: bold;
        color: #1E90FF;
    }
    .timestamp {
        font-size: 0.8em;
        color: gray;
    }
    .stButton>button {
        padding: 4px 8px;
        font-size: 12px;
        margin: 2px 1px;
        border-radius: 8px;
    }
    @media screen and (max-width: 600px) {
        div[data-modal-container='true'] {
            width: 95% !important;
            left: 2.5% !important;
            padding: 5px !important;
        }
        div[data-modal-container='true'] > div:first-child {
            padding: 0.5rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Modal for Reply Form
modal = Modal(key="Reply Modal", title="🖋️ Write a Reply")

# User Authentication Functions
def create_user(username, password):
    """Create a new user account"""
    if users_collection.find_one({"username": username}):
        return False
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    users_collection.insert_one({
        "username": username,
        "password": hashed_pw,
        "created_at": datetime.utcnow()
    })
    return True

def authenticate(username, password):
    """Authenticate user"""
    user = users_collection.find_one({"username": username})
    if user:
        hashed_pw = hashlib.sha256(password.encode()).hexdigest()
        if user["password"] == hashed_pw:
            return True
    return False

# Authentication UI
def show_auth():
    """Show login/signup forms"""
    st.subheader("မြန်မာနာမည်စာလုံးပေါင်းကို အင်္ဂလိပ်အက္ခရာဖလှယ်ခြင်းနည်းစနစ်",divider=True)
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab1:
        with st.form("Login"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("Login"):
                if authenticate(username, password):
                    st.session_state.user = username
                    st.rerun()
                else:
                    st.error("Invalid username or password")
    
    with tab2:
        with st.form("Sign Up"):
            new_user = st.text_input("New Username")
            new_pw = st.text_input("New Password", type="password")
            confirm_pw = st.text_input("Confirm Password", type="password")
            if st.form_submit_button("Create Account"):
                if new_pw != confirm_pw:
                    st.error("Passwords don't match")
                elif create_user(new_user, new_pw):
                    st.success("Account created! Please login")
                else:
                    st.error("Username already exists")

# Comment Display Function
def display_comments(parent_id=None, depth=0):
    """Recursively display comments"""
    query = {"postId": POST_ID, "parentId": parent_id}
    comments = list(comments_collection.find(query).sort("createdAt", 1))
    
    for comment in comments:
        likes = comment.get('likes', 0)
        unlikes = comment.get('unlikes', 0)
        
        with st.container():
            st.markdown(f"""
               <div class='comment-box' style='margin-left: {depth * 20}px;'>
                    <span class='user'>{comment['userId']}</span>: {comment['text']}<br> 
                    <div class='timestamp'>{comment['createdAt'].strftime('%Y-%m-%d %H:%M')}</div>
                </div>
            """, unsafe_allow_html=True)

            col1, col2, col3 = st.columns([1,1,1])
            with col1:
                if st.button(f"👍 {likes}", key=f"like_{comment['_id']}"):
                    comments_collection.update_one(
                        {"_id": comment["_id"]},
                        {"$inc": {"likes": 1}}
                    )
                    st.rerun()
            with col2:
                if st.button(f"👎 {unlikes}", key=f"unlike_{comment['_id']}"):
                    comments_collection.update_one(
                        {"_id": comment["_id"]},
                        {"$inc": {"unlikes": 1}}
                    )
                    st.rerun()
            with col3:
                if st.session_state.user and st.button("💬 Reply", key=f"reply_{comment['_id']}"):
                    st.session_state.replying_to = comment["_id"]
                    modal.open()

            display_comments(comment["_id"], depth + 1)

# Main App Logic
if st.session_state.user:    
    st.sidebar.success(f"Logged in as {st.session_state.user}")
    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.rerun()
    if st.sidebar.button("အကြောင်းအရာ"):
        st.page_link("pages/home.py", label="Home", icon="🏠")
        
    st.sidebar.button("မြန်မာအညွှန်း")
    st.sidebar.button("ပါ")
    
    st.subheader("🗨️ Comments")
    display_comments()
    
    # Reply Modal
    if modal.is_open():
        with modal.container():
            st.write("Your reply will be posted under this comment.")
            reply_text = st.text_area("Your Reply", key="reply_text", height=150)
            
            if st.button("📤 Submit Reply"):
                if reply_text.strip() and "replying_to" in st.session_state:
                    reply_data = {
                        "_id": uuid.uuid4().hex,
                        "userId": st.session_state.user,
                        "postId": POST_ID,
                        "text": reply_text,
                        "parentId": st.session_state.replying_to,
                        "likes": 0,
                        "unlikes": 0,
                        "createdAt": datetime.utcnow()
                    }
                    comments_collection.insert_one(reply_data)
                    st.success("✅ Reply added!")
                    st.session_state.replying_to = None
                    modal.close()
                    st.rerun()
    
    # New Comment
    st.subheader("➕ Add a New Comment")
    new_comment = st.text_area("Write your comment here:", key="main_comment")
    if st.button("📤 Post Comment"):
        if new_comment.strip():
            comment_data = {
                "_id": uuid.uuid4().hex,
                "userId": st.session_state.user,
                "postId": POST_ID,
                "text": new_comment,
                "parentId": None,
                "likes": 0,
                "unlikes": 0,
                "createdAt": datetime.utcnow()
            }
            comments_collection.insert_one(comment_data)
            st.success("✅ Comment posted!")
            st.session_state.clear_text = True
            st.rerun()
else:
    show_auth()