import argparse as ap

def parse():
    """
    Parse command line arguments
    """
    parser = ap.ArgumentParser(prog="geoDist",description="Determine the distance between two cities")

    cities = parser.add_argument('c',nargs=2,help="Supply cities to calculate distance.")
    unit = parser.add_argument('-u',nargs=1,default=['km'],help="Distance unit to use.")
    args = parser.parse_args()

    if args.c == []:
        raise ap.ArgumentError(cities,"No cities provided")
    
    if not (args.u[0].lower() in ('km','mi')):
        raise ap.ArgumentError(unit,"Invalid unit, expected ('km','mi').")

    return args