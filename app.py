# import streamlit as st
# from pymongo import MongoClient
# from datetime import datetime
# import uuid

# # MongoDB Connection
# client = MongoClient("mongodb://localhost:27017/")
# db = client["comment_system"]
# comments_collection = db["comments"]

# st.title("📝 Comment System with MongoDB & Streamlit")

# # Post ID (သင့် application မှာ dynamic ဖြစ်ရပါမည်)
# POST_ID = "post456"

# def display_comments(comments, depth=0):
#     for comment in comments:
#         # ပုံစံပြင်ပြီး indent ပြသ
#         with st.container():
#             st.markdown(
#                 f"<div style='margin-left: {depth * 20}px; border-left: 1px solid #ccc; padding-left: 10px;'>"
#                 f"<strong>{comment['userId']}</strong>: {comment['text']}<br>"
#                 f"<small>{comment['createdAt'].strftime('%Y-%m-%d %H:%M')}</small><br>"
#                 # f"<button style='font-size: 0.8em;'>💬 Reply</button>"
#                 f"</div>",
#                 unsafe_allow_html=True,
#             )
#             if st.button("Reply", key=f"btn_{comment['_id']}"):
#                 st.session_state.replying_to = comment["_id"]

#             # Nested replies ကို recursive ပြသ
#             if "replies" in comment and len(comment["replies"]) > 0:
#                 display_comments(comment["replies"], depth + 1)

# # Show existing comments
# comments = list(comments_collection.find({"postId": POST_ID, "parentId": None}))
# st.subheader("🗨️ Comments")
# display_comments(comments)

# # Reply Form
# if "replying_to" in st.session_state:
#     st.subheader("🖋️ Reply")
#     reply_text = st.text_area("Your reply:")
#     if st.button("📤 Submit Reply"):
#         if reply_text.strip():
#             reply_data = {
#                 "_id": uuid.uuid4().hex,
#                 "userId": "anonymous_user",  # သင့် app မှ user auth စနစ်ထည့်နိုင်
#                 "postId": POST_ID,
#                 "text": reply_text,
#                 "parentId": st.session_state.replying_to,
#                 "replies": [],
#                 "createdAt": datetime.utcnow()
#             }

#             # Insert new reply into the parent comment
#             comments_collection.update_one(
#                 {"_id": st.session_state.replying_to},
#                 {"$push": {"replies": reply_data}}
#             )
#             st.success("✅ Reply added!")
#             st.session_state.replying_to = None
#             st.rerun()

# # Add New Comment
# st.subheader("➕ Add a New Comment")
# new_comment = st.text_area("Write your comment here:")
# if st.button("📤 Post Comment"):
#     if new_comment.strip():
#         comment_data = {
#             "_id": uuid.uuid4().hex,
#             "userId": "anonymous_user",
#             "postId": POST_ID,
#             "text": new_comment,
#             "parentId": None,
#             "replies": [],
#             "createdAt": datetime.utcnow()
#         }
#         comments_collection.insert_one(comment_data)
#         st.success("✅ Comment posted!")
#         st.rerun()

import streamlit as st
from pymongo import MongoClient
from datetime import datetime
import uuid

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["comment_system"]
comments_collection = db["comments"]

# Page Config
st.set_page_config(page_title="Comment System", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
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
        .action-buttons {
            display: flex;
            gap: 10px;
            margin-top: 5px;
        }
        .like-btn, .unlike-btn {
            background: none;
            border: none;
            cursor: pointer;
            font-size: 0.9em;
        }
        .like-btn:hover {
            color: green;
        }
        .unlike-btn:hover {
            color: red;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📝 Comment System with MongoDB & Streamlit")
POST_ID = "post456"

def display_comments(comments, depth=0):
    for comment in comments:
        likes = comment.get('likes', 0)
        unlikes = comment.get('unlikes', 0)

        with st.container():
            st.markdown(f"""
                <div class='comment-box' style='margin-left: {depth * 30}px;'>
                    <span class='user'>{comment['userId']}</span>: {comment['text']}
                    <div class='timestamp'>{comment['createdAt'].strftime('%Y-%m-%d %H:%M')}</div>
                  
                </div>
            """, unsafe_allow_html=True)

            if st.button("Reply", key=f"btn_{comment['_id']}"):
                st.session_state.replying_to = comment["_id"]

            # Like/Unlike Logic (JavaScript မဟုတ်ဘဲ Python ဖြင့် handle)
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"👍 Like ({likes})", key=f"like_{comment['_id']}"):
                    comments_collection.update_one(
                        {"_id": comment["_id"]},
                        {"$inc": {"likes": 1}}
                    )
                    st.rerun()
            with col2:
                if st.button(f"👎 Unlike ({unlikes})", key=f"unlike_{comment['_id']}"):
                    comments_collection.update_one(
                        {"_id": comment["_id"]},
                        {"$inc": {"unlikes": 1}}
                    )
                    st.rerun()
            ## 1 comment

        if "replies" in comment and len(comment["replies"]) > 0:
            display_comments(comment["replies"], depth + 1)

# Show existing comments
comments = list(comments_collection.find({"postId": POST_ID, "parentId": None}))
st.subheader("🗨️ Comments")
display_comments(comments)

# Reply Form
if "replying_to" in st.session_state:
    st.subheader("🖋️ Reply")
    reply_text = st.text_area("Your reply:")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("📤 Submit Reply"):
            if reply_text.strip():
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

                # Insert new reply into the parent comment
                comments_collection.update_one(
                    {"_id": st.session_state.replying_to},
                    {"$push": {"replies": reply_data}}
                )
                st.success("✅ Reply added!")

                # ✅ Reply တင်ပြီးရင် session_state ကို clear လုပ်ပြီး form ကိုဖျောက်
                st.session_state.replying_to = None
                st.rerun()  # page ကို refresh လုပ်ပြီး form ကိုမပြတော့ဘူး

    with col2:
        if st.button("❌ Cancel"):
            st.session_state.replying_to = None
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