"""05 기본필수: qa와 summary를 서로 다른 0/1 열로 표현합니다."""
from sklearn.preprocessing import OneHotEncoder

train = [["qa"], ["summary"], ["qa"]]
valid = [["summary"], ["qa"]]
# sparse_output=False는 결과를 바로 볼 수 있는 숫자 표로 받는 설정입니다.
encoder = OneHotEncoder(sparse_output=False)
encoder.fit(train)

# 해설 B05-1: train에서 배운 열 순서는 qa, summary입니다. summary는 [0, 1], qa는 [1, 0]입니다.
valid_ready = encoder.transform(valid).tolist()
print("열 순서:", encoder.categories_[0].tolist())
print("valid 변환:", valid_ready)
