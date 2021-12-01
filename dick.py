import argparse
import interp

parser = argparse.ArgumentParser(
    description="Run dicklang code."
)

parser.add_argument("file", type=str, help="The filepath for the dicklang code you want to run")

args = parser.parse_args()
interp.runDicklang(args.file)
