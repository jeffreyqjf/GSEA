import gseapy as gp
from gseapy.plot import gseaplot
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("./df1XX全部基因.csv")
# print(df)
term_to_plot = df["Unnamed: 0"]
rnk = df.sort_values('logFC', inplace=False, ascending=False)
rnk = rnk.set_index("Unnamed: 0")
rnk = rnk["logFC"]
print(rnk)


pre_res = gp.prerank(rnk=rnk, gene_sets='KEGG_2016',
                     processes=10,
                     outdir='test/prerank_report_kegg', format='png', seed=6)
terms = pre_res.res2d.index
# to save your figure, make sure that ofname is not None
gseaplot(rank_metric=pre_res.ranking, term=terms[0], **pre_res.results[terms[0]])
print(term_to_plot)
