import pandas as pd

datalist = [["Weather", "S,S,C,R,R,R,C,S,S,R,S,C,C,R".split(',')],
            ["Temp","H,H,H,N,C,C,C,H,C,N,N,N,H,N".split(',')],
            ["Exer",[0,0,1,1,1,0,1,0,1,1,1,1,1,0]]
]

df = pd.DataFrame.from_dict(dict(datalist))

# print(df)

# df.groupby("Exer").count()
# df.groupby(["Weather", "Exer"]).count()
df.groupby(["Temp","Exer"]).count()