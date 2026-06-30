原题地里有，task scheduler，感觉就这一道题
part1输入是[{"id":'1'}, {"deadline":2}], task id是string，ddl是int，用heap很快就写了

part2是加subtask，格式大概是[{"id":'1'}, {"deadline":2}, {"subtasks": ["2","3"]}]，要加consumed

part3是updateDeadline，先检查这个task是不是已经被consumed了，如果已经consumed了还update就return None。不然就update deadline, 输入[{"id":'1'}, {"deadline":5}}]
test都给写好了，直接跑就可以