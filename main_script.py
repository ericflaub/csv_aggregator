import os
import pandas as pd


directory = 'C:/Users/eflau/test_docs/EIM Summary Files'
col_names = ['ID','Sensor','Rater','Muscle','P50','X50','R50','P100','X100','R100']
df_main = pd.DataFrame(columns = col_names)

for filename in os.listdir(directory):
    filename = filename.replace("._", "")
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        df = pd.read_csv(f)
        df['ID'] = filename.replace("_summary.csv", "")
        df_main = pd.concat([df_main, df])
        print('sam is a poopoo head \n sam is a poopoo head \n a big big poopoo head')


df_main.to_csv('one_file.csv')