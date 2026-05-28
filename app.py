from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

FILE_PATH = "Work Log 20260402 主要4機種.xlsx"

# ✅ トップページ（Excel一覧）
@app.route("/", methods=["GET"])
def excel():

    df = pd.read_excel(FILE_PATH, header=20)
    df = df.fillna("")

    # ✅ 日付変換
    df["作業日"] = pd.to_datetime(df["作業日"], errors="coerce")

    # ✅ 新しい順
    df = df.sort_values(by="作業日", ascending=False)

    # ✅ 表示用フォーマット
    df["作業日"] = df["作業日"].dt.strftime("%Y-%m-%d")

    search = request.args.get("search")

    # ✅ SN検索
    if search:
        df = df[df["SN"].astype(str).str.contains(search)]

    # ✅ インデックス追加（詳細用）
    df = df.reset_index()

    # ✅ 表示列（重要）
    df = df[["index", "SN", "作業日", "作業者", "依頼内容", "作業内容"]]

    # ✅ 初期5件
    data = df.head(5).to_dict(orient="records")

    return render_template("excel.html", data=data)


# ✅ 詳細画面
@app.route("/detail/<int:row_id>")
def detail(row_id):

    df = pd.read_excel(FILE_PATH, header=20)
    df = df.fillna("")
    df = df.reset_index()

    row = df[df["index"] == row_id]

    if row.empty:
        return "データが見つかりません"

    return render_template("detail.html", data=row.iloc[0])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
