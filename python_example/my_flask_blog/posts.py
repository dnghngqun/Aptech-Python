# Post a news
# Bộ nhớ tạm thời lưu bài viết
posts =[]

def get_posts():
    return posts

def add_post(title, content):
    posts.append({"title": title, "content": content})