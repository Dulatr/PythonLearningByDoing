#####   Example usage from another Python script #####
from Pi import Chudnovsky

ans=Chudnovsky(55)

print(f"Value: {ans[0]}\n\nError: {ans[1]}")
print('\n'+len(str(ans[0])).__str__())