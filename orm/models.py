import datetime

from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.types import String, CHAR, BigInteger, Integer, Text, DateTime

BaseModel = declarative_base()


class Blog(BaseModel):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), server_default='', nullable=False)
    text = Column(Text, nullable=False)
    create = Column(BigInteger, index=True, server_default='0', nullable=False)

    user = Column(CHAR(32), index=True, server_default='', nullable=False)


class UserDepartment(BaseModel):
    __tablename__ = 'user_department'

    user_id = Column(Integer, primary_key=True)
    department_id = Column(Integer, primary_key=True)
    extra_data = Column(String(50))
    create_time = Column(DateTime, default=datetime.datetime.now())

    user = relationship('User', foreign_keys='User.id', primaryjoin='UserDepartment.user_id == User.id',
                        uselist=False, backref='user')

    department = relationship('Department', foreign_keys='Department.id',
                              primaryjoin='UserDepartment.user_id == Department.id',
                              uselist=False, backref='department')


class Department(BaseModel):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), server_default='', nullable=False)

    users = relationship('User',
                         primaryjoin='UserDepartment.department_id==Department.id',
                         secondary=UserDepartment.__table__,
                         secondaryjoin='UserDepartment.user_id == foreign(User.id)')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }


class User(BaseModel):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), server_default='', nullable=False)
    username = Column(String(32), index=True, unique=True, server_default='', nullable=False)
    password = Column(String(64), server_default='', nullable=False)
    departments = relationship('Department',
                               foreign_keys=[id],
                               primaryjoin='UserDepartment.user_id==User.id',
                               secondary=UserDepartment.__table__,
                               secondaryjoin='UserDepartment.department_id==foreign(Department.id)')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'departments': [department.name for department in self.departments]
        }


class Permission(BaseModel):
    __tablename__ = 'permission'

    id = Column(Integer, primary_key=True)


class Task(BaseModel):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    celery_id = Column(String(32), server_default='', comment='celery task id')


class ActionLog(BaseModel):
    __tablename__ = 'action_log'

    id = Column(Integer, primary_key=True)
    user_id = Column('user_id', Integer, nullable=False, comment='动作的执行人')
    target = Column('task_id', Integer, nullable=False, comment='动作影响的对象')
    create_time = Column('create_time', DateTime, nullable=False, comment='创建时间')
