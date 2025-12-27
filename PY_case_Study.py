import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
import os

# ✅ Create folder to store graphs
folder = "graphs"
os.makedirs(folder, exist_ok=True)

graph_count = 1

# ✅ Auto-save function
def save_plot():
    global graph_count
    plt.savefig(f"{folder}/graph_{graph_count}.png",
                dpi=300, bbox_inches='tight')
    graph_count += 1


# Task 1
state_txn = pd.read_excel("S:\DATA SCIENCE\python dataset\phonepe-Data.xlsx" ,sheet_name="State_Txn and Users")
state_split = pd.read_excel("S:\DATA SCIENCE\python dataset\phonepe-Data.xlsx" ,sheet_name="State_TxnSplit")
state_dev = pd.read_excel("S:\DATA SCIENCE\python dataset\phonepe-Data.xlsx" ,sheet_name="State_DeviceData")
state_txn_District = pd.read_excel("S:\DATA SCIENCE\python dataset\phonepe-Data.xlsx" ,sheet_name="District_Txn and Users")
Demographics_dis = pd.read_excel("S:\DATA SCIENCE\python dataset\phonepe-Data.xlsx" ,sheet_name="District Demographics")

print("State_Txn and Users top 5 rows")
print(state_txn.head())
print("State_TxnSplit bottom 10 rows")
print(state_split.tail(10))
print("State_DeviceData middle 10 rows")
mid= len(state_dev)//2
print(state_dev.iloc[mid-5:mid+5])
print("District_Txn and Users bottom & top 10 rows")
print(state_txn_District.head(10))
print(  state_txn_District.tail(10))
print("District Demographics every 10th rows")
print(Demographics_dis.iloc[::10])

# Task 1.2
print("Statistics for each dataset")

print("State_Txn Summary Statistics")
print(state_txn.describe())
print("Median:\n", state_txn.median(numeric_only=True))

print("\nState_TxnSplit Summary Statistics")
print(state_split.describe())
print("Median:\n", state_split.median(numeric_only=True))

print("\nState_DeviceData Summary Statistics")
print(state_dev.describe())
print("Median:\n", state_dev.median(numeric_only=True))

print("\nDistrict_Txn and Users Summary Statistics")
print(state_txn_District.describe())
print("Median:\n", state_txn_District.median(numeric_only=True))

print("\nDistrict Demographics Summary Statistics")
print(Demographics_dis.describe())
print("Median:\n", Demographics_dis.median(numeric_only=True))

# ----- Data Types -----
print("\nData Types for Each Dataset")
print("State_Txn dtypes")
print(state_txn.dtypes)
print("\nState_TxnSplit dtypes")
print(state_split.dtypes)
print("\nState_DeviceData dtypes")
print(state_dev.dtypes)
print("\nDistrict_Txn and Users dtypes")
print(state_txn_District.dtypes)
print("\nDistrict Demographics dtypes")
print(Demographics_dis.dtypes)

# Task 1.3
print("Identifying missing values")

# ---- State_Txn ----
null_state_txn = (
    state_txn.isnull()
    .sum()
    .to_frame("null")
    .assign(
        len_of_clm=len(state_txn),
        percentage_Na=lambda x: 100 * x["null"] / x["len_of_clm"]
    )
)

print("Null Analysis: State_Txn")
print(null_state_txn)
mc = null_state_txn["null"].idxmax() 
if null_state_txn["null"].max() == 0:
    print("NO null values")
else:
    mc = null_state_txn["null"].idxmax()
    print("The column with most null values is:", mc)

print("\n--------------------------------------------\n")

# ---- State_TxnSplit ----
null_state_split = (
    state_split.isnull()
    .sum()
    .to_frame("null")
    .assign(
        len_of_clm=len(state_split),
        percentage_Na=lambda x: 100 * x["null"] / x["len_of_clm"]
    )
)

print("Null Analysis: State_TxnSplit")
print(null_state_split)

mc = null_state_split["null"].idxmax()
if null_state_split["null"].max() == 0:
    print("NO null values")
else:
    mc = null_state_split["null"].idxmax()
    print("The column with most null values is:", mc)
print("-------------------------------------------------------\n")

# ---- State_DeviceData ----
null_state_dev = (
    state_dev.isnull()
    .sum()
    .to_frame("null")
    .assign(
        len_of_clm=len(state_dev),
        percentage_Na=lambda x: 100 * x["null"] / x["len_of_clm"]
    )
)

print("Null Analysis: State_DeviceData")
print(null_state_dev)

mc = null_state_dev["null"].idxmax()
if null_state_dev["null"].max() == 0:
    print("NO null values")
else:
    print("The column with most null values is:", mc)

print("-------------------------------------------------------\n")

# ---- District_Txn and Users ----
null_district_txn = (
    state_txn_District.isnull()
    .sum()
    .to_frame("null")
    .assign(
        len_of_clm=len(state_txn_District),
        percentage_Na=lambda x: 100 * x["null"] / x["len_of_clm"]
    )
)

print("Null Analysis: District_Txn and Users")
print(null_district_txn)

mc = null_district_txn["null"].idxmax()
if null_district_txn["null"].max() == 0:
    print("NO null values")
else:
    mc = null_district_txn["null"].idxmax()
    print("The column with most null values is:", mc)
print("-------------------------------------------------------\n")

# ---- District Demographics ----
null_demo = (
    Demographics_dis.isnull()
    .sum()
    .to_frame("null")
    .assign(
        len_of_clm=len(Demographics_dis),
        percentage_Na=lambda x: 100 * x["null"] / x["len_of_clm"]
    )
)

print("Null Analysis: District Demographics")
print(null_demo)

mc = null_demo["null"].idxmax()
if null_demo["null"].max() == 0:
    print("NO null values")
else:
    mc = null_demo["null"].idxmax()
    print("The column with most null values is:", mc)
print("-------------------------------------------------------\n")

# Task 1.4
total_state = Demographics_dis["State"].nunique()
unique_district = Demographics_dis["District"].nunique()
print("Total number of states:", total_state)
print("Total number of districts:", unique_district)

d = Demographics_dis.groupby("State")["District"].count().idxmax()
print("State with highest number of districts:", d)

# Task 2.1 - EDA
trans = state_txn.pivot_table(
    values= ["Transactions", "Amount (INR)"],
    index=  "State",
    aggfunc= "sum",
    columns="Year"
)

print(trans)
top_5 = state_txn.groupby("State")["Transactions"].sum().to_frame("SUM")
lowest_5 = top_5.sort_values("SUM").head(5)
highest_5 = top_5.sort_values("SUM", ascending=False).head(5)

print("Lowest 5 States:\n", lowest_5)
print("\nHighest 5 States:\n", highest_5)

# Task 2.2 - EDA 
most_common1 = state_split.groupby(["State" , "Quarter" , "Transaction Type"])["Transaction Type"].count()
most_frequent = most_common1.groupby(
    ["State", "Quarter"]
).idxmax().to_frame("Most Frequent Transaction Type")   
most_frequent = most_frequent.reset_index(drop=True)
print(most_frequent)

# Task 2.3 - EDA 
most_device = state_dev.groupby(["State" , "Brand"])["Registered Users"].sum()
brand =  most_device.groupby(["State"]).idxmax().to_frame("MAX")

print(brand.reset_index(drop=True))

# Task 2.4 - EDA
df = Demographics_dis.groupby(["State", "District"])["Population"].sum().reset_index()
df = df.sort_values(["State", "Population"], ascending=[True, False])
result = df.drop_duplicates("State")

print(result)
cat = result["District"]
val = result["Population"]
plt.figure(figsize=(20,8))  
sns.barplot( x="District", y="Population",hue="State",  data=result,palette="tab20")
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.title("Most Populated District in Each State", fontsize=18, fontweight="bold")
plt.xlabel("Districts", fontsize=14)
plt.ylabel("Population ", fontsize=14)
plt.xticks(rotation=75, ha="right", fontsize=8)
plt.subplots_adjust(bottom=0.2)
plt.legend( title="State", bbox_to_anchor=(1, 1), loc="upper left", borderaxespad=0, fontsize=8)

save_plot()
plt.show()

# Task 2.5 - EDA

atv_state= state_txn.groupby("State")["ATV (INR)"].sum().to_frame("ATV").reset_index()
order = atv_state.sort_values(by="ATV" , ascending=False)
print(atv_state)
print("Top 5 highest ATV State")
print(order.head(5))
print("bottom 5  ATV State")
print(order.tail(5))

# Task 2.6 - EDA

app_open = state_txn.pivot_table(
    values = "App Opens" ,
    index= "State" , 
    aggfunc= "sum" ,
    columns= ["Year", "Quarter"]
)

state_txn["Time"] = (
    state_txn["Year"].astype(str) + 
    " Q" + 
    state_txn["Quarter"].astype(str)
)

print(state_txn.head(5))
print(app_open)
bihar =  state_txn[ state_txn["State"] == "Bihar"]
plt.figure(figsize=(8,6))
plt.plot(bihar["Time"] , bihar["App Opens"] , label="BIHAR DATA ")
plt.xlabel("YEAR") 
plt.xticks(rotation=60)  
plt.ylabel("ATV")
plt.title("BIHAR ATV ANALYSIS")
plt.legend()

save_plot()
plt.show()

# Task 2.7 - EDA
latest_year = state_split["Year"].max()
latest_quarter = state_split[state_split["Year"] == latest_year]["Quarter"].max()

print("Most Recent Quarter:", latest_year, "Q", latest_quarter)
trans_type = state_split[(state_split["Year"] == latest_year) & (state_split["Quarter"] == latest_quarter)]
grouped = trans_type.groupby(["State", "Transaction Type"])["Transactions"].sum().reset_index()
plt.figure(figsize=(22,10))
sns.barplot(
    data=grouped, x="State",  y="Transactions",  hue="Transaction Type")
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.xticks(rotation=90)
plt.title(f"Transaction Type Distribution by State ({latest_year} Q{latest_quarter})")
plt.tight_layout()

save_plot()
plt.show()

# Task 2.8 - EDA
uc =state_txn_District["District"].drop_duplicates().to_frame()
uc2= state_txn_District["Code"].drop_duplicates().to_frame()
dis_code = uc.join(uc2)
dis_code.to_csv("Dis_code.csv" , index=False)
print(dis_code)

# Task 3 - Data Quality Check
state_level = state_txn.groupby("State")[["Transactions" , "Amount (INR)", "Registered Users"]].sum()
state_level.loc["Total"] = state_level.sum()
print(state_level)

print("NOW DISTRICT LEVEL")
District_level = state_txn_District .groupby("State")[["Transactions" , "Amount (INR)", "Registered Users"]].sum()
District_level.loc["Total"] = District_level.sum()
print(District_level)
diff = state_level - District_level
print(diff.loc["Andhra Pradesh"])
print("The only difference between the two grouped sheets is the “Amount (INR)” for Andhra Pradesh, which is higher in the district-level dataset. All other states and all other columns (Transactions, Registered Users) match exactly.")
 
# Task 4.1 - data merging 
state_demo = pd.merge( state_txn , Demographics_dis ,
                      how="left",
                      on="State")
gcr = state_demo.groupby("State")[["Population","Registered Users"]].sum().reset_index()
gcr["Ratio of Users to Population"] = gcr["Registered Users"] / gcr["Population"]
print(gcr)

# Task 4.2 - data merging 
dis_group = state_txn_District.groupby("District")[["Transactions"]].sum().reset_index()

dis_demo = pd.merge(
    dis_group,
    Demographics_dis,
    how="inner",
    on="District"
)

dis_demo["Density"] = dis_demo["Population"] / dis_demo["Area (sq km)"]
print("DENSI")
print(dis_demo)

dis_demo = dis_demo.replace([np.inf, -np.inf], np.nan)
dis_demo = dis_demo.dropna(subset=["Density", "Transactions"])

corr = dis_demo["Transactions"].corr(dis_demo["Density"])

print("Correlation:", corr)

plt.figure(figsize=(8,6))
plt.scatter( dis_demo["Density"] ,dis_demo["Transactions"] ,  marker='o', s=100, alpha=0.4 , label="CORRELATION")
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.title("CORRELATION of population and density")
plt.xlabel("Transactoions")
plt.ylabel("Density")
plt.legend()

save_plot()
plt.show()

# Task 4.3 - data merging 
state_grouped = state_txn.groupby("State").agg({
    "Amount (INR)": "sum",
    "Registered Users": "sum"
}).reset_index()

state_grouped["Avg Amount per User"] = (
    state_grouped["Amount (INR)"] / state_grouped["Registered Users"]
)

print(state_grouped[["State", "Avg Amount per User"]])
data = state_grouped[["State", "Avg Amount per User"]].sort_values(by="Avg Amount per User" , ascending=False).reset_index(drop=True)
print("TOP 5 STATE WITH HIGHEST ATV")
print(data.head(5))
print("LEAST 5 STATE WITH LOWEST ATV")
print(data.tail(5).reset_index(drop=True))

# Task 4.4 - data merging
device_txn_merge = pd.merge(state_dev , state_txn,
                            how = "left",
                            on = ["State" , "Year" , "Quarter"])
gr_reg = device_txn_merge.groupby("State")["Registered Users_x"].sum().reset_index()
gr_dev = device_txn_merge.groupby(["State","Brand"])["Registered Users_x"].sum().reset_index()
merge = pd.merge(gr_dev , gr_reg ,
                 how= "left",
                 on="State")
print(merge)
merge["Ratio"] =  merge["Registered Users_x_x"]  /  merge["Registered Users_x_y"]
print(merge)
st_d = merge[merge["State"] =="West Bengal"]
print(st_d)
plt.figure(figsize=(16,12))
ax = sns.barplot(x="Brand" , y="Ratio", data=st_d , edgecolor="black", linewidth=1.5, hatch="/", alpha=0.8)
plt.bar_label(ax.containers[0], fontsize=12)
plt.title("Device wise Ratio of West bengal", fontsize=16, color="darkblue", fontweight="bold", loc="center")
plt.xlabel("BRAND", fontsize=14, color="green", fontstyle="italic")
plt.ylabel("RATIO", fontsize=14, color="purple")
plt.legend(loc="upper left") 
plt.grid(True, linestyle="--", alpha=0.7) 
plt.tight_layout()
plt.xticks()

save_plot()
plt.show()

# Task 5.1 - Visualisation
arn_state= state_txn[state_txn["State"] == "Meghalaya"]
print(arn_state)
plt.figure(figsize=(10,8))
plt.plot(arn_state["Time"] ,arn_state["Transactions"] , color="cyan", linewidth=2, linestyle="--", marker="o",
        markersize=8, markerfacecolor="pink", markeredgecolor="lightgray" ,  
        label="Growth Trend of Transaction")
plt.plot(arn_state["Time"] ,arn_state["Amount (INR)"] , color="palegreen", linewidth=2, linestyle="--", marker="o",
        markersize=8, markerfacecolor="pink", markeredgecolor="black" ,  
        label="Growth Trend of Amount")
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.title("Meghalaya")
plt.xlabel("YEAR AND QUARTER")
plt.xticks(rotation=75)
plt.legend()

save_plot()
plt.show()

# Task 5.2 - Visualisation
Delhi = state_split[(state_split["State"]=="Delhi") & (state_split["Quarter"]==1)]
gr_d = Delhi.groupby(["State", "Quarter","Transaction Type"])["Transactions"].sum().reset_index()

print(gr_d)
plt.figure(figsize=(10,8))

plt.pie(
    gr_d["Transactions"], autopct="%1f%%",startangle=90,pctdistance=1.15,shadow=True,explode=[0, 0, 0, 0.05, 0],
    colors=["red", "palegreen", "yellow", "orange", "lightgray"]
)

plt.legend(gr_d["Transaction Type"],title="Transaction Types",loc="upper left",
    bbox_to_anchor=(-0.1, 1.05) 
)
plt.tight_layout()

save_plot()
plt.show()

# Task 5.3 - Visualisation
den_state = dis_demo[dis_demo["State"] ==  "Telangana"]
print(den_state)
plt.figure(figsize=(12,10))
ax = sns.barplot(x="District" , y="Density",  data=den_state , edgecolor="black", linewidth=1.5, color="#7BEB81", hatch="/", alpha=0.8)
plt.bar_label(ax.containers[0], fontsize=6)
plt.title("Telangana District Density", fontsize=16, color="#966C13", fontweight= "bold", loc="center")
plt.xlabel("STATE", fontsize=14, color="green", fontstyle="italic")
plt.ylabel("Density ", fontsize=14, color="purple")
plt.grid(True, linestyle="--", alpha=0.7) 
plt.tight_layout()
plt.xticks(rotation=45, ha="right") 
plt.subplots_adjust(bottom=0.12)

save_plot()
plt.show()

# 6 Advance Analysis
#6.1
analysis1 = state_txn
analysis1 ["Time"] = state_txn["Year"].astype(str) + " Q"+ state_txn["Quarter"].astype(str)
group_analysis = analysis1.groupby(["Time"])["Transactions"].sum().reset_index()
print(group_analysis)
plt.figure(figsize=(8,6))
plt.plot(group_analysis["Time"], group_analysis["Transactions"])
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.title("Transaciton trend over Year and Quarter")
plt.xlabel("Year & Quarter")
plt.ylabel("Transactions")
plt.xticks(rotation=75,fontsize=7) 

save_plot()
plt.show()

analysis2_group =  state_split.groupby("Transaction Type")["Transactions"].sum().reset_index()
print(analysis2_group)
analysis2_group["Transactions_Cr"] = analysis2_group["Transactions"] / 1e7
plt.figure(figsize=(8,6))
ax = sns.barplot(x="Transaction Type" , y="Transactions_Cr",  data=analysis2_group , edgecolor="black", linewidth=1.5, color="#7BEB81", hatch="--", alpha=0.8)
plt.bar_label(ax.containers[0], fontsize=12)
plt.title("Transactions accordding to transaction Type", fontsize=16, color="#966C13", fontweight= "bold", loc="center")
plt.xlabel("Transaction Type", fontsize=14, color="green", fontstyle="italic")
plt.ylabel("Transactions in Crores", fontsize=14, color="purple")
plt.grid(True, linestyle="--", alpha=0.7) 
plt.tight_layout()
plt.xticks(fontsize=8) 
plt.subplots_adjust(bottom=0.12)

save_plot()
plt.show()

#6.2 
correl = dis_demo["Density"].corr(dis_demo["Transactions"])
print(f"Correlation value: {correl:.3f}")

if correl > 0.7:
    interpretation = "Strong positive correlation"
elif correl > 0.3:
    interpretation = "Moderate positive correlation"
elif correl > 0:
    interpretation = "Weak positive correlation"
else:
    interpretation = "No meaningful positive correlation"

print("Interpretation:", interpretation)

plt.figure(figsize=(8,6))
plt.scatter(dis_demo["Density"],dis_demo["Transactions"]) 
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.text(0.95, 0.95, 
         f"Correlation: {correl:.2f}", 
         transform=plt.gca().transAxes,
         ha='right', va='top')
plt.title("Correlation Between Population Density and Transaction Volume")
plt.xlabel("Density", fontsize=14, color="green", fontstyle="italic")
plt.ylabel("Transactions", fontsize=14, color="purple")

save_plot()
plt.show()
