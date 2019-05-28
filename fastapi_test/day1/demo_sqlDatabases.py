from fastapi_test import Depends, FastAPI
from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import Session, sessionmaker
from starlette.requests import Request
from starlette.responses import Response

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:qian95@127.0.0.1/test'

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class CustomBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

Base = declarative_base(cls=CustomBase)

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean(), default=True)

Base.metadata.create_all(bind=engine)

db_session = SessionLocal()

first_user = db_session.query(User).first()
if not first_user:
    u = User(email='zhangsan@163.com', hashed_password='notreallyhashed')
    db_session.add(u)
    db_session.commit()

db_session.close()

def get_user(db_session: Session, user_id: int):
    return db_session.query(User).filter(User.id == user_id).first()

def get_db(request: Request):
    return request.state.db

app = FastAPI()

@app.post('/users')
def add_user():
    u = User(email='wangwu@163.com', hashed_password='lisi')
    db_session.add(u)
    db_session.commit()

@app.get('/users/{user_id}')
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id=user_id)
    return user

@app.middleware('http')
async def db_session_middleware(request: Request, call_next):
    response = Response('Internal server error', status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response