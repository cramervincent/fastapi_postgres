from ..dependencies.router_dependencies import *
from ..auth import *
import json
router = APIRouter()

@router.post('/auth/login')
async def login_user(data:schemas.Login, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    
    if not user:
        raise HTTPException(status_code=404)
    
    hashed_pass = user.hashed_password
   

    if not verify_password(data.password, hashed_pass):
        raise HTTPException(
            status_code=400,
            detail="Incorrect email or password"
        )
    
   
    return {
        "access_token": create_access_token(user.id),
        "refresh_token": create_refresh_token(user.id),
    }
    

@router.get('/auth/me', response_model=schemas.ResponseUser)
async def get_logged_in_user(current_user: str = Depends(get_current_user), db:Session = Depends(get_db)):
    return db.query(models.User).filter(models.User.id == current_user).first()