import sys
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP
from flask_login import UserMixin 

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8mb4' % (
    "root",
    "root",
    "127.0.0.1:3306",
    "python_db",
)

#DB接続用のインスタンスを作成
ENGINE = create_engine(
    DATABASE,
    convert_unicode=True,
    echo=True  #SQLをログに吐き出すフラグ
)

#上記のインスタンスを使って、MySQLとのセッションを張る
session = scoped_session(
    sessionmaker(
        autoflush = False,
        autocommit = False,
        bind = ENGINE,
    )
)

#以下に書いていくDBモデルのベース部分を作る
Base = declarative_base()
Base.query = session.query_property()

#DBとデータをやり取りするためのモデルを定義
class User(Base):
    __tablename__ = 'kaiin_table'
    id = Column('id', Integer, primary_key = True)
    name = Column('name', String(200))
    email = Column('email', String(200))
    password = Column('password', String(200))
    created_at = Column('created_at', TIMESTAMP, server_default=current_timestamp())
    updated_at = Column('updated_at', TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

# 今まで利用していたUserモデルと、ログイン機能用のUserMixinを合成
class LoginUser(UserMixin, User):
    # このモデルを介して認証ユーザーIDを内部で取得するためのメソッド(このメソッド名で作ってあげます)
    def get_id(self):
        return self.id

def main(args):
    Base.metadata.drop_all(bind=ENGINE)
    Base.metadata.create_all(bind=ENGINE)

#このファイルを直接実行したとき、mainメソッドでテーブルを作成する
if __name__ == "__main__":
    main(sys.argv)