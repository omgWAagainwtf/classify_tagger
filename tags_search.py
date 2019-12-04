import gaipy as gp
import json
import math
def search(cur_category,cur_page):
    db_name = "category_tag"
    res = gp.Select(db_name,pattern={'col':['category'],'val':[cur_category]},ret_col=['keywords'],page_cnt=100,page=cur_page)
    ret = json.loads(res)
    ret = json.loads(ret['data'])
    tags = []
    for i in range(len(ret['recs'])):
        tags.append(ret['recs'][i]['rec']['keywords'])
    total_page = math.ceil(ret['cnt']/10)
    return {"tags":tags,"pages":total_page}
print(search('政治',1))