import sys
import os, glob
import pandas as pd

## macOS ONLY
def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

output_path = "output/"
history_path = "history/"
targets=["rtx2070"]

if (len(sys.argv) - 1) != 1:
    print("No target provided, exiting...")
    quit()


target = sys.argv[1]

filenames = glob.glob(os.path.join(output_path, target + "*.csv"))
filenames += glob.glob(os.path.join(history_path, target + ".csv"))
combined_csv = pd.concat( [ pd.read_csv(f) for f in filenames ] )
combined_csv.to_csv( "history/" + target + ".csv", index=False )

file = pd.read_csv("history/" + target + ".csv")

# Find the prices that we care about.
current = file['price'].iloc[0]
max = file['price'].max()
min = file['price'].min()
first = file['price'].iloc[-1]

if (first * 0.9) > current:
    notify("PRICE ALERT: " + target, "10% drop in price. Now $" + str(current))
if (first * 1.05) < current and first != current:
    notify("PRICE ALERT: " + target, "5% increase in price. Now $" + str(current))
