import sys
import os, glob
import pandas as pd

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
