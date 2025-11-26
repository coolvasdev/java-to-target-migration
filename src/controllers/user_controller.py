from fastapi import APIRouter, HTTPException, status
from typing import List
from models.user import User, UserCreate, UserUpdate

router = APIRouter(prefix="/api/users", tags=["users"])


@router.get("/", response_model=List[User])
async def get_all_users():
    """Get all users"""
    # TODO: Implement database query
    return []


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str):
    """Get user by ID"""
    # TODO: Implement database query
    raise HTTPException(status_code=404, detail="User not found")


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate):
    """Create new user"""
    # TODO: Implement user creation
    pass


@router.put("/{user_id}", response_model=User)
async def update_user(user_id: str, user_data: UserUpdate):
    """Update user"""
    # TODO: Implement user update
    pass


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str):
    """Delete user"""
    # TODO: Implement user deletion
    pass
