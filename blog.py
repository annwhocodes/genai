import streamlit as st
import os
import datetime

# Set up a directory for saving the blog posts and images
if not os.path.exists("blog_posts"):
    os.makedirs("blog_posts")
if not os.path.exists("blog_images"):
    os.makedirs("blog_images")

# Define the sidebar for creating new blog posts
def create_sidebar():
    st.sidebar.title("Create New Blog Post")
    post_title = st.sidebar.text_input("Title")
    post_tags = st.sidebar.text_input("Tags (comma-separated)")
    post_content = st.sidebar.text_area("Content", height=500)
    post_formatting = st.sidebar.selectbox("Formatting", ["Markdown", "Plain Text"])
    post_image = st.sidebar.file_uploader("Upload an image (optional)", type=["jpg", "jpeg", "png"])
    if st.sidebar.button("Create"):
        # Save the blog post and any uploaded images
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        post_filename = f"{timestamp}-{post_title}.md"
        with open(f"blog_posts/{post_filename}", "w") as f:
            f.write(f"Title: {post_title}\n")
            f.write(f"Tags: {post_tags}\n")
            f.write(f"Timestamp: {timestamp}\n")
            if post_image is not None:
                image_filename = f"{timestamp}-{post_image.name}"
                with open(f"blog_images/{image_filename}", "wb") as img_file:
                    img_file.write(post_image.getbuffer())
                f.write(f"Image: {image_filename}\n")
            f.write("\n")
            f.write(post_content)
        st.sidebar.success("Blog post created!")

# Define the main content area for viewing existing blog posts
def create_main_content():
    st.title("Tantra Lekh")
    post_files = os.listdir("blog_posts")
    if not post_files:
        st.info("No blog posts yet.")
    for post_file in post_files:
        with open(f"blog_posts/{post_file}", "r") as f:
            post_content = f.read()
            post_lines = post_content.split("\n")
            post_title = post_lines[0][7:]
            post_tags = post_lines[1][6:].split(",")
            post_timestamp = post_lines[2][11:]
            post_image = None
            if len(post_lines) > 3 and post_lines[3].startswith("Image: "):
                post_image = post_lines[3][7:]
            post_content = "\n".join(post_lines[4:])
            st.write(f"## {post_title}")
            st.write(f"*Tags:* {' '.join(['`'+tag.strip()+'`' for tag in post_tags])}")
            st.write(f"*Date/Time:* {post_timestamp}")
            if post_image is not None:
                st.image(f"blog_images/{post_image}", use_column_width=True)
            if post_file.endswith(".md"):
                st.markdown(post_content)
            else:
                st.write(post_content)

# Run the app
create_sidebar()
create_main_content()