#좌/우 붙이기 
# 이번 절에서는 판다스의 concat 함수를 사용하여 데이터프레임을 
# 좌/우로 붙여 보겠습니다. 
# 인덱스는 동일한데 컬럼의 데이터가 분리되어 있을 때 
# 여러 데이터프레임을 붙여서 하나의 데이터프레임으로 만들 수 있습니다. 
# 예를 들어 네이버의 일별 시세 데이터가 
# 아래와 같이 데이터프레임으로 분리되어 있을 때 
# 두 데이터프레임을 합쳐서 시가/고가/저가/종가/거래량 컬럼을 
# 갖는 하나의 데이터프레임으로 만들어 보는 겁니다.

# concat 함수는 기본적으로 같은 컬럼 레이블을 갖는 
# 데이터프레임 객체를 위/아래로 연결합니다. 
# axis=1 파라미터를 전달하면 리스트로 전달된 데이터프레임을 
# 좌/우로 연결합니다. 
# 이때 데이터프레임들은 인덱스를 기준으로 데이터를 연결합니다.
from pandas import DataFrame 
import pandas as pd 

#첫번째 데이터프레임
data = { 
        '종가':[113000,111500],
        '거래량':[555850, 282163]
        }
index = ['2019-06-21','2019-06-20']
df1 = DataFrame(data=data, index=index)

#두번째
data = { 
        '시가':[112500,111000],
        '고가':[115000, 112000],
        '저가':[111500, 109000]
        }
index = ['2019-06-21','2019-06-20']
df2 = DataFrame(data=data, index=index)

df = pd.concat([df1, df2], axis=1)
print("---좌우로 붙이기---")
print(df)

#컬럼을 순서를 변경해 봅니다.
print("---정렬순서를 변경---")
정렬순서 = ['시가','고가','저가','종가','거래량']
df = df[정렬순서]
print(df)

# 인덱스가 다른 데이터프레임은 어떻게 동작할까요? 
# 인덱스가 다른 두 개의 데이터프레임을 정의하고 concat 함수를 
# 사용해 봅시다. 
# 위에서 사용했던 데이터프레임과는 인덱스만 다릅니다.
data = {
    '종가': [113000, 111500],
    '거래량': [555850, 282163]
}

index = ["2019-06-21", "2019-06-20"]
df1 = DataFrame(data=data, index=index)

data = {
    '시가': [112500, 110000],
    '고가': [115000, 112000],
    '저가': [111500, 109000]
}

index = ["2019-06-20", "2019-06-19"]
df2 = DataFrame(data=data, index=index)
print("---concat함수 사용---")
df = pd.concat([df1, df2], axis=1)
print(df)
# 결과를 보면 df1의 존재하지 않는 2019-06-19의 
# 종가/거래량과 df2의 2019-06-21의 시가/고가/저가가 
# 결측값 NaN으로 표기된 것을 알 수 있습니다.

# concat 함수에서 join 파라미터를 사용하여 outer, inner 옵션으로 
# 인덱스가 다를 때의 동작을 지정할 수 있습니다. 
# outer는 합집합처럼 모든 인덱스에 대해 값을 연결하며 
# 존재하지 않는 값은 결측값으로 표시합니다. 
# join 파라미터를 지정하지 않으면 outer 모드로 동작해서 
# 위의 결과를 얻었던 겁니다. 
# inner 모드를 사용하면 교집합처럼 동작해서 
# 인덱스가 공통인 부분만 연결합니다.
df = pd.concat([df1, df2], axis=1, join='inner')
print(df)

#위/아래로 붙이기 
# 이번에는 데이터프레임을 위/아래로 이어 붙여 보겠습니다. 
# 두 개의 데이터프레임의 컬럼을 기준으로 정렬한 후 위/아래로 붙여서 
# 새로운 데이터프레임을 생성할 수 있습니다. 
# 예를 들어 네이버 주식의 일봉 데이터가 
# 있다면 두 개의 데이터프레임으로 
# 분리되어 있을 때, 두 데이터프레임을 하나의 데이터프레임으로 병합해봅시다.
from pandas import DataFrame
import pandas as pd

# 첫 번째 데이터프레임
data = {
    '종가': [113000, 111500],
    '거래량': [555850, 282163]
}
index = ["2019-06-21", "2019-06-20"]
df1 = DataFrame(data, index=index)

# 두 번째 데이터프레임
data = {
    '종가': [110000, 483689],
    '거래량': [109000, 791946]
}
index = ["2019-06-19", "2019-06-18"]
df2 = DataFrame(data, index=index)

print("---위아래 붙이기---")
df = df1.append(df2)
print(df)

#  append 메서드는 원본 데이터를 수정하는 것이 아니라 
# 결과가 저장된 새로운 데이터프레임을 반환하는 것을 주의하세요.

# 앞서 배운 concat 함수를 사용해서 데이터프레임을 위/아래로 붙일 수도 있습니다. 
# concat 함수는 여러 개의 데이터프레임을 리스트로 전달하면 
# 모든 데이터프레임을 연결해서 그 결과를 데이터프레임으로 반환합니다. 
# axis=1일 경우 좌/우로 나란히 연결하며, axis=0일 경우 위/아래로 연결합니다. 
# axis를 입력하지 않으면 0으로 해석해서 위/아래로 연결합니다. 
# 다음 코드를 실행해 보면 df1에 append 메서드를 사용해서 df2를 
# 추가한 것과 같은 결과를 갖는 것을 알 수 있습니다. 
# 두 개의 데이터프레임을 위/아래로 연결할 때는 
# append 메서드를 사용하고 연결할 
# 데이터프레임이 여러 개인 경우 concat 함수를 사용하면 편리합니다.
print("---concat함수로 위아래 붙아기---")
df = pd.concat([df1, df2])
print(df)


#Merge
# 판다스의 merge는 데이터프레임을 '병합'합니다. 
# concat이 단순히 두 데이터프레임을 이어 붙이는 연결이라면 
# merge는 특정 컬럼의 값을 기준으로 데이터를 병합합니다. 
# 병합의 개념을 예시를 통해서 확인해봅시다. 
# 세 종목에 대한 정보가 들어 있는 df1 데이터프레임이 있습니다. 
# 네 개의 업종에 대한 업종별 등락률이 
# 저장된 df2 데이터프레임이 있습니다. 
# 두 데이터프레임을 병합해서 아래와 같은 데이터프레임을 만든다고 
# 가정해 봅시다. 이러한 연산은 두 데이터프레임을 
# 단순히 이어붙이는 concat이나 append로는 해결할 수 없습니다. 
# df1에 전기전자 업종이 2개, df2에는 전기전자 업종이 1개 있습니다. 
# 이때 두 데이터로 만들어 낼 수 있는 모든 조합은 2(=2x1)개입니다. 
# 이런 방식으로 데이터를 병합하는 것이 merge입니다.
from pandas import DataFrame
import pandas as pd

# 첫 번째 데이터프레임
data = [
    ["전기전자", "005930", "삼성전자", 74400],
    ["화학", "051910", "LG화학", 896000],
    ["전기전자", "000660", "SK하이닉스", 101500]
]

columns = ["업종", "종목코드", "종목명", "현재가"]
df1 = DataFrame(data=data, columns=columns)

# 두 번째 데이터프레임
data = [
    ["은행", 2.92],
    ["보험", 0.37],
    ["화학", 0.06],
    ["전기전자", -2.43]
]

columns = ["업종","등락률"]
df2 = DataFrame(data=data, columns=columns)

print("---merge함수로 붙이기---")
df = pd.merge(left=df1, right=df2, on='업종')
print(df)

# how 파라미터를 사용해서 합치는 방법을 지정할 수 있습니다. 
# 'inner' 모드를 사용하면 df1과 df2의 교집합, 
# 'outer' 모드를 사용하면 합집합으로 병합됩니다. 
# 모드에 따른 동작은 concat에서 사용해 본 것처럼 일관성 있게 
# 설계돼 있습니다. 
# 추가로 merge에서 사용할 수 있는 left, right 옵션에 
# 대해 알아봅시다. 추가 옵션에 사용할 데이터를 우선 정의합니다. 
# 이전 코드에서 df1의 데이터만 일부 변경했습니다.
# 첫 번째 데이터프레임
data = [
    ["전기전자", "005930", "삼성전자", 74400],
    ["화학", "051910", "LG화학", 896000],
    ["서비스업", "035720", "카카오", 121500]
]

columns = ["업종", "종목코드", "종목명", "현재가"]
df1 = DataFrame(data=data, columns=columns)

# 두 번째 데이터프레임
data = [
    ["은행", 2.92],
    ["보험", 0.37],
    ["화학", 0.06],
    ["전기전자", -2.43]
]

columns = ["업종", "등락률"]
df2 = DataFrame(data=data, columns=columns)

# 두 데이터프레임을 병합할 때 left 옵션을 사용해 보겠습니다. 
# 이는 left 파라미터에 입력된 데이터프레임 df1을 기준으로 
# 두 데이터프레임을 병합합니다.
print("---merge함수에서 how=left지정하기---")
df = pd.merge(left=df1, right=df2, 
    how='left', on='업종')
print(df)


# 만약 두 데이터프레임의 컬럼이 다르다면 어떻게 해야 할까요? 
# 물론 컬럼의 이름을 변경하고 데이터프레임을 합칠 수 있지만, 
# 코드의 양만 많아집니다. 
# 다음 예제와 함께 merge의 옵션을 사용해서 한 번에 문제를 해결해 봅시다. 
# 이전 코드에서 두 번째 데이터프레임의 컬럼 이름만을 다르게 정의했습니다.
# 첫 번째 데이터프레임
data = [
    ["전기전자", "005930", "삼성전자", 74400],
    ["화학", "051910", "LG화학", 896000],
    ["서비스업", "035720", "카카오", 121500]
]

columns = ["업종", "종목코드", "종목명", "현재가"]
df1 = DataFrame(data=data, columns=columns)

# 두 번째 데이터프레임
data = [
    ["은행", 2.92],
    ["보험", 0.37],
    ["화학", 0.06],
    ["전기전자", -2.43]
]

columns = ["항목", "등락률"]
df2 = DataFrame(data=data, columns=columns)


# 두 데이터프레임의 컬럼 이름이 다르기 때문에 합칠 기준이되는 각 컬럼의 이름을 
# 모두 입력해야 합니다. 
# left_on와 right_on 파라미터에 두 컬럼 이름을 넣습니다.
print("---기준이 되는 컬럼명이 다른 경우---")
df = pd.merge(left=df1, 
    right=df2, left_on='업종',
    right_on='항목')
print(df)

