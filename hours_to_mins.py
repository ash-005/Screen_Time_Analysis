import pandas as pd
df = pd.read_csv("screen_time.csv")
df = df.set_index('Date')
df = df.drop(['14-04-2024','15-04-2024','16-04-2024','17-04-2024','18-04-2024','19-04-2024','20-04-2024'],axis=0)
#print(df['Times_Unlocked'].count)
#print(df.head(7))
def hours_to_mins(time):
    print(time)
    ls = time.split()
    #print(ls)
    #print(ls[0][0])
    if len(ls[0]) == 3:
        hrs_num = int(ls[0][:2])
        hrs_min = hrs_num*60
        return hrs_min+int(ls[1][:2])
    else:
        hrs_num = int(ls[0][0])
        hrs_min = hrs_num*60
        return hrs_min+int(ls[1][:2])

print("Enter the screentime in Xhrs Ymins to get total mins duration: ")
ch = 1
mins_spent = []
while ch!=22:

    user_input = input("FORMAT(7h 18mins/16h 04mins): ")
    #print(hours_to_mins(user_input))
    mins_spent.append(hours_to_mins(user_input))
    ch+=1

#print(mins_spent)
df['Time_Spent(minutes)'] = mins_spent
df.head()
save = input("Save this file? ")
if save == 'yes':
    df.to_csv("updated_stime.csv")
else:
    print(f'MEHHHH')
#print(df.Times_Unlocked.value_counts().sum())