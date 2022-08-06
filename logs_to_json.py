import json
import re

class Log():
    def __init__(self, player_one, player_two,kill, guild, time):
        self.player_one = player_one
        self.player_two = player_two
        self.kill = kill
        self.guild = guild
        self.time = time


logs = []


with open("logs.txt") as file:
    for line in file:

        kill = "has killed" in line
        result = re.search(r"\[(.*)\] (\w*) (died to|has killed) (\w*) from (\w*)", line)
        if(result == None):
            continue
        time = result.groups()[0]
        p1 = result.groups()[1]
        p2 = result.groups()[3]
        guild = result.groups()[4] 
        logs.append(Log(p1, p2, kill, guild, time))
        
        
        
        
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump([log.__dict__ for log in logs], f, ensure_ascii=False, indent=4)