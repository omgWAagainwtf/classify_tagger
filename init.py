import gaipy as gp
import json
def init():
    db_name = "category_tag"
    res = gp.Select(db=db_name,ret_col=['category'],page_cnt=50)
    ret = json.loads(res)
    ret = json.loads(ret['data'])
    keyword_list = []
    for i in range(len(ret['recs'])):
        keyword_list.append(ret['recs'][i]['rec']['category'])
    
    return keyword_list
def get_document():
    db_name = "doc_tag"
    res = gp.Select(db=db_name,pattern={'col':["confirm"],"val":["0"]},page=1,page_cnt=1)
    ret = json.loads(res)
    ret = json.loads(ret['data'])
    #print(ret)
    if ret['cnt'] == 0:
        return "no document left"
    document = ret['recs'][0]['rec']['content']
    keywords = ret['recs'][0]['rec']['keywords'].split(',')
    category = ret['recs'][0]['rec']['category']
    text_id = ret['recs'][0]['rec']['text_id']
    confirm = ret['recs'][0]['rec']['confirm']
    return {"text":document,"tag":keywords,"category":category,"text_id":text_id,"confirm":str(confirm)}
def get_status():
    db_name = "doc_tag"
    res = gp.Select(db=db_name,pattern={'col':["confirm"],"val":["1"]})
    ret = json.loads(res)
    ret = json.loads(ret['data'])
    tagged = ret['cnt']
    res = gp.Select(db=db_name)
    ret = json.loads(res)
    ret = json.loads(ret['data'])
    total = ret['cnt']
    return(tagged,total)
#get_status()
#print(get_document())
#print(init())