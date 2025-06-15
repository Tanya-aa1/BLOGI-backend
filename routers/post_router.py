from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form, Query
from sqlalchemy.orm import Session
from models import Post
from database import get_db
from schemas import PostCreate, PostOut
import shutil
import os
import uuid
from routers.auth_router import get_current_user
from sqlalchemy import or_


router = APIRouter(prefix="/posts", tags=["Posts"])

# Create Post
@router.post("/", response_model=PostOut)
def create_post(
    title: str = Form(...),
    content: str = Form(...),
    image: UploadFile = File(None),
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    image_url = None
    if image:
        if not image.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Only image files are allowed")
        os.makedirs("static", exist_ok=True)  
        file_ext = os.path.splitext(image.filename)[-1]
        unique_filename = f"{uuid.uuid4()}{file_ext}"
        image_path = f"static/{unique_filename}"
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        image_url = f"/static/{unique_filename}"
    new_post = Post(
        title=title,
        content=content,
        user_id=user.id,
        image_url=image_url 
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# Get All Posts
@router.get("/", response_model=list[PostOut])
def get_posts(
    db: Session = Depends(get_db),
    limit: int = Query(10, ge=1),
    skip: int = Query(0, ge=0),
    search: str = Query(default=None),
):

    query = db.query(Post)
    if search:
        query = query.filter(
            or_(
                Post.title.ilike(f"%{search}%"),
                Post.content.ilike(f"%{search}%")
            )
        )
    posts = query.order_by(Post.created_at.desc()).offset(skip).limit(limit).all()
    return posts

# Get Post by ID
@router.get("/{post_id}", response_model=PostOut)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

# Update Post
@router.put("/{id}", response_model=PostOut)
def update_post(
    id: int,
    title: str = Form(...),
    content: str = Form(...),
    image: UploadFile = File(None),
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    post_query = db.query(Post).filter(Post.id == id)
    post = post_query.first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    if post.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    # Handle optional new image upload
    image_url = post.image_url  # default to existing image
    if image:
        os.makedirs("static", exist_ok=True)
        file_ext = os.path.splitext(image.filename)[-1]
        unique_filename = f"{uuid.uuid4()}{file_ext}"
        image_path = f"static/{unique_filename}"
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        image_url = f"/static/{unique_filename}"

    # Update fields
    post.title = title
    post.content = content
    post.image_url = image_url

    db.commit()
    db.refresh(post)
    return post

# Delete Post
@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    db.delete(post)
    db.commit()
    return None
