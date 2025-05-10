def main():
    syn_times: int = int(input())

    syns: dict[str, str] = {}
    syns_rev: dict[str, str] = {}
    for _ in range(syn_times):
        k, v = input().split()
        syns[k] = v
        syns_rev[v] = k

    val = input()
    if syn_val:=syns[val]:
        print(syn_val.strip())
    else:
        print(syns_rev[val].strip())
        
        
