import lxml
import sys
import glob


def check_params ():
  if len(sys.argv) < 2:
    print("Concordia Crawler.")
    print("")
    print("Usage: ")
    print("  python indexer.py <data_glob>")
    print("")

def main ():
  check_params()
  files = glob.glob(sys.argv[1])


if __name__ == "__main__":
  main()