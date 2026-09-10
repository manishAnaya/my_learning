import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [100, 150, 120, 180]
}

df = pd.DataFrame(data)

df.plot(x="Month", y="Sales")