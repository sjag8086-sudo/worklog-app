# Flask Webアプリ開発チートシート

## ① ルーティング
@app.route("/")
def home():
    return "Hello"

## ② テンプレート表示
return render_template("index.html")

HTML:
{{ name }}

## ③ フォーム入力
<form method="POST">
    <input type="text" name="username">
    <button type="submit">送信</button>
</form>

Python:
name = request.form["username"]

## ④ GET / POST
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        pass

## ⑤ DBモデル
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

## ⑥ Create
new_user = User(name=name)
db.session.add(new_user)
db.session.commit()

## ⑦ Read
users = User.query.all()

## ⑧ Update
user = User.query.get(user_id)
user.name = name
db.session.commit()

## ⑨ Delete
db.session.delete(user)
db.session.commit()

## ⑩ URLパラメータ
@app.route("/edit/<int:user_id>")

## ⑪ リダイレクト
return redirect("/")

## ⑫ 入力チェック
if not name.strip():
    return render_template("index.html", error="入力してください")

## ⑬ 一覧表示
{% for user in users %}
    {{ user.name }}
{% endfor %}

## ⑭ 削除確認
onclick="return confirm('削除しますか？')"

---

## ⑭ これは覚える（重要）
・@app.route("/") → URLと処理をつなぐ

・request.form → 入力を受け取る

・render_template → 画面表示

・redirect → 画面遷移

・CRUDの概念（登録・取得・更新・削除）

---
ブラウザ → URL → route → Python → DB → HTML → 表示

