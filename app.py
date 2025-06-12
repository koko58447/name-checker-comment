
import streamlit as st
from pymongo import MongoClient
from datetime import datetime
import uuid
from streamlit_modal import Modal

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["comment_system"]
comments_collection = db["comments"]

# Page Config
st.set_page_config(page_title="Comment System", layout="centered")

POST_ID = "post456"
# CSS for comment styling
st.markdown("""
    <style>
    
    .stButton > button {
        # background-color: #4CAF50;
        color: black;
        border: none;
        padding: 4px 4px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 10px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        transition: all 0.3s;
    }
    
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
       .inline-container {
            display: flex;
            gap: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Modal for Reply Form
modal = Modal(key="Reply Modal", title="🖋️ Write a Reply")

def display_comments(comments, depth=0,reply=True):
    for comment in comments:
        likes = comment.get('likes', 0)
        unlikes = comment.get('unlikes', 0)  # နောက်ထပ်ထည့်နိုင်ပါတယ်
        with st.container():
            st.markdown(f"""
               <div class='comment-box' style='margin-left: {depth * 30}px;'>
                    <span class='user'>{comment['userId']}</span>: {comment['text']}<br> 
                     <div class='timestamp'>{comment['createdAt'].strftime('%Y-%m-%d %H:%M')}</div>
                </div>
            """, unsafe_allow_html=True)           

            col1,col2,col22,col33,col3 = st.columns([1,1,1,1,1], gap="small", vertical_alignment="top", border=False)
            if reply:

                with col1:
                    if st.button(f"{likes}👍 Like", key=f"like_{comment['_id']}"):
                            comments_collection.update_one(
                                {"_id": comment["_id"]},
                                {"$inc": {"likes": 1}}
                            )
                            st.rerun()
                with col2:
                    if st.button(f"{unlikes} 👎 UnLike", key=f"unlike_{comment['_id']}"):
                            comments_collection.update_one(
                                {"_id": comment["_id"]},
                                {"$inc": {"unlikes": 1}}
                            )
                            st.rerun()
                  
                with col3:
                
                    if st.button("💬 Reply", key=f"btn_{comment['_id']}"):
                        st.session_state.replying_to = comment["_id"]
                        modal.open()

        if "replies" in comment and len(comment["replies"]) > 0:
            display_comments(comment["replies"], depth + 1,True)

# Show existing comments
comments = list(comments_collection.find({"postId": POST_ID, "parentId": None}))
st.subheader("🗨️ Comments")
display_comments(comments)

# Modal Form for Reply
if modal.is_open():
    with modal.container():
        st.write("Your reply will be posted under this comment.")
        reply_text = st.text_area("Your Reply")

        if st.button("📤 Submit Reply"):
            if reply_text.strip() and "replying_to" in st.session_state:
                reply_data = {
                    "_id": uuid.uuid4().hex,
                    "userId": "anonymous_user",
                    "postId": POST_ID,
                    "text": reply_text,
                    "parentId": st.session_state.replying_to,
                    "replies": [],
                    "likes": 0,
                    "unlikes": 0,
                    "createdAt": datetime.utcnow()
                }

                comments_collection.update_one(
                    {"_id": st.session_state.replying_to},
                    {"$push": {"replies": reply_data}}
                )
                st.success("✅ Reply added!")
                st.session_state.replying_to = None
                modal.close()
                st.rerun()


# Add New Comment
st.subheader("➕ Add a New Comment")
new_comment = st.text_area("Write your comment here:", key="main_comment")
if st.button("📤 Post Comment"):
    if new_comment.strip():
        comment_data = {
            "_id": uuid.uuid4().hex,
            "userId": "anonymous_user",
            "postId": POST_ID,
            "text": new_comment,
            "parentId": None,
            "replies": [],
            "likes": 0,
            "unlikes": 0,
            "createdAt": datetime.utcnow()
        }
        comments_collection.insert_one(comment_data)
        st.success("✅ Comment posted!")
        st.rerun()