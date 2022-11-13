
from playhouse.db_url import connect
from peewee import Model
from peewee import CharField

db = connect("sqlite:///peewee_db.sqlite") # データベースに接続

if not db.connect():
    print("接続NG")
    exit()
print("接続OK")

# 作りたいテーブルをクラスで書く
class Post(Model):
    name = CharField()  # 名前   CharField() 文字列
    title = CharField()  # タイトル
    body = CharField()  # 内容
    class Meta:
        database = db
        table_name = "post"

db.create_tables([Post])

