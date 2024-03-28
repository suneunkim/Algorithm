N = int(input())

entry_record = {}

for _ in range(N):
    name, record = input().split()
    entry_record[name] = record

current_enter = [name for name, record in entry_record.items() if record == "enter"]

current_enter.sort(reverse=True) # sort는 리스트를 직접 정렬하고 반환값이 없다.

for name in current_enter:
    print(name)