import streamlit as st
from pymongo import MongoClient
from datetime import datetime
import uuid
from streamlit_modal import Modal

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["comment_system"]
comments_collection = db["comments1"]

# Page Config
st.set_page_config(page_title="Comment System", layout="centered")

POST_ID = "post456"

@st.dialog("Reply")
def vote(item):
    st.write("Your reply will be posted under this comment.")
    reply_text = st.text_area(
        "Your Reply", 
        key="reply_text",
        height=150  # Set a reasonable default height
    )
    if st.button("📤 Submit Reply", use_container_width=True):
        if reply_text.strip() and "replying_to" in st.session_state:
            reply_data = {
                "_id": uuid.uuid4().hex,
                "userId": "anonymous_user",
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

   

# CSS for comment styling (same as before)
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
        color: black;
        border: none;
        padding: 4px 8px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 12px;
        margin: 2px 1px;
        cursor: pointer;
        border-radius: 8px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #f0f0f0;
    }
    .action-buttons {
        display: flex;
        gap: 5px;
        margin-top: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for text area clearing
if 'clear_text' not in st.session_state:
    st.session_state.clear_text = False

def clear_text_area():
    st.session_state.main_comment = ""
    st.session_state.clear_text = False

# Modal for Reply Form
modal = Modal(key="Reply Modal", title="🖋️ Write a Reply")

def display_comments(parent_id=None, depth=0):
    """Recursively display comments and their replies"""
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
                if st.button("💬 Reply", key=f"reply_{comment['_id']}"):
                    st.session_state.replying_to = comment["_id"]
                    # modal.open()
                    vote("A")

            display_comments(comment["_id"], depth + 1)

# Show existing comments
st.subheader("🗨️ Comments")
display_comments()

# Add New Comment with clearing functionality
st.subheader("➕ Add a New Comment")

# Initialize text area with empty string if clear_text is True
if st.session_state.clear_text:
    clear_text_area()

new_comment = st.text_area(
    "Write your comment here:", 
    key="main_comment",
    value="" if st.session_state.clear_text else st.session_state.get("main_comment", "")
)

if st.button("📤 Post Comment"):
    if new_comment.strip():
        comment_data = {
            "_id": uuid.uuid4().hex,
            "userId": "anonymous_user",
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