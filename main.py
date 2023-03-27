import pandas as pd
import my_sel as sel


df_email = pd.read_csv("base_email.csv", delimiter = ",")
df = df_email
# sel.check_email(df_email)
sel.check_email_v2(df)
