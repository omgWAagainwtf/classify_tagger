import gaipy as gp
import json
import math
def tags_search(cur_category,cur_page):
    db_name = "category_tag"
    res = gp.Select(db_name,pattern={'col':['category'],'val':[cur_category]},ret_col=['keywords'],page_cnt=10,page=cur_page)
    ret = json.loads(res)
    ret = json.loads(ret['data'])
    tags = []
    if ret['cnt'] > 0:
        tags = ret['recs'][0]['rec']['keywords'].split(',')
    total_page = math.ceil(len(tags)/10)
    return {"tags":tags,"pages":total_page}
print(tags_search('政治',1))