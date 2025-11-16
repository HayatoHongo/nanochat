import onnx
from onnx import printer

# 外部データを無視して構造だけ読み込み
with open("model_q4.onnx", "rb") as f:
    raw = f.read()
model = onnx.load_model_from_string(raw)

# テキスト形式に変換
text = printer.to_text(model)

# 画面に出す
print(text)

# またはファイルに保存
with open("model_q4_structure.txt", "w") as f:
    f.write(text)
