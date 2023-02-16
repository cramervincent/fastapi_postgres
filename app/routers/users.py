from ..dependencies.router_dependencies import *
from ..auth import hash_password
router = APIRouter()


@router.get('/users', response_model=list[schemas.ResponseUser])
async def get_all_users(db:Session = Depends(get_db)):
    return db.query(models.User).all()

@router.post('/users', response_model=schemas.ResponseUser)
async def create_new_user(data:schemas.User, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if user:
        raise HTTPException(status_code=409, detail='Email allready exist.')
    
    new_user = models.User(
        email=data.email,
        fullname=data.fullname,
        hashed_password=hash_password(data.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/users/:id', response_model=schemas.ResponseUser)
async def get_one_user(id:int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=404
        )
    return user

@router.patch('/users/:id', response_model=schemas.ResponseUser)
async def update_one_user(id:int, data:schemas.UserUpdate, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=404
        )
     
    for key, value in data:
        if not value == None:
            print(value)
            setattr(user, key, value)
    
    db.commit()
    db.refresh(user)
    return user

@router.delete('/users/:id')
async def delete_one_user(id, db:Session = Depends(get_db)):
    user =db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404)
    db.delete(user)
    db.commit()
    return "user deleted"