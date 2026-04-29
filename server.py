import random
import os

FLAG = os.getenv("FLAG", "flag{dummy}")

print("ようこそ！ロシアンルーレットゲームへ！", flush=True)
print("さっそくゲームを始めよう！", flush=True)
print("心の準備がつかない？では何度かシミュレーションをしてみるとしようか", flush=True)

# 乱数でシードを決める
seed = random.randint(1, 100)
rng = random.Random(seed)

# 10回シミュレーション
history = [rng.randint(1, 10) for _ in range(10)]
# ここでは1を選んだこととする、死んだ回数をカウント
death_count = len(history) - history.count(1)

print("\n=== シミュレーション結果 ===", flush=True)
for i, n in enumerate(history, 1):
    print(f"{i}回目: {n}", flush=True)

print(f"\nもし本番なら君は {death_count} 回は死んだね", flush=True)
print("さあ本番だ", flush=True)
print("1〜10の数字を入力してください:", end="", flush=True)

try:
    guess = int(input())
except Exception:
    print("入力が不正です。", flush=True)
    exit()

if not 1 <= guess <= 10:
    print("1〜10の数字を入力してください。", flush=True)
    exit()

# この数字を当てれば生還
answer = rng.randint(1, 10)

if guess == answer:
    print("生還おめでとう！", flush=True)
    print(f"FLAG: {FLAG}", flush=True)
else:
    print("GAME OVER", flush=True)
