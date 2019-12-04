import gaipy as gp
import json
def search(cur_category,cur_page):
    db_name = "category_tag"
    res = gp.Select(db_name,pattern={'col':['category'],'val':[cur_category]},ret_col=['keywords'])
    ret = json.loads(res)
    ret = json.loads(ret['data'])
    tags = []
    for i in range(len(ret['recs'])):
        tags.append(ret['recs'][i]['rec']['keywords'])
    return tags
print(search('政治',1))