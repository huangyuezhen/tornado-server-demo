import re
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy import exc
from sqlalchemy import orm
from tornado.log import app_log

from conf import settings
from handler.base import HTTPError

DB_URL = settings['database_url']

db_kwargs = settings['database_config']
Engine = create_engine(DB_URL, **db_kwargs)


def init():
    app_log.info('init mysql')


Filed = re.compile(r'(has no property) (.*)')

SESSION_MAKER = None


def connect(engine=Engine):
    global SESSION_MAKER
    if not SESSION_MAKER:
        SESSION_MAKER = orm.sessionmaker(bind=engine, autoflush=False)
    return SESSION_MAKER


@contextmanager
def session_scope(session):
    try:
        yield session
        session.commit()
    except exc.IntegrityError as e:
        session.rollback()
        raise HTTPError(status_code=400, reason=str(e))
    except orm.exc.NoResultFound as e:
        session.rollback()
        raise HTTPError(status_code=404, reason=str(e))
    except exc.InvalidRequestError as e:

        error_info = e.args[0]
        value = Filed.search(error_info)
        if value:
            value = value.group(2)
            reason = "InvalidRequestError, arguments %s is not allowed" % value
        else:
            reason = "InvalidRequestError, please check your request arguments"
        session.rollback()
        raise HTTPError(status_code=400, reason=reason)
    except Exception as e:
        session.rollback()
        raise HTTPError(status_code=400, reason=str(e))
