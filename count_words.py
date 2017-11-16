def count_substring(string, sub_string):
    count=0
    for i in range(len(string)-len(sub_string)+1):
        if string[i:i+3]==sub_string:
                   count+=1
    return count

print(count_substring("Deepikadediuahndfcidewchn","de" ))