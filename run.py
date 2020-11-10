# from codes.fastTraditionalModel import *
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("mode", type=str,
                    help="Mode: train/test. Data Folder is saved following the email.")
args = parser.parse_args()

if __name__ == "__main__":
    if args.mode == "train":
        train()
    elif args.mode == "test":
        test()
    else:
        print("input error. Mode must be chosen in train/test")