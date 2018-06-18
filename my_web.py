#
# web示例
#
import web
import json
import denglj.my_crawler

# 指定模板目录
render = web.template.render('templates/')



# urls =(
#     '/' , 'index'
# )
#
# class index :
#     def GET(self):
#         i = web.input(name=None)        #获取参数url?name=xxx
#         return render.index(i.name)     #index指向模板文件名称


urls = (
    '/index/(.*)', 'index',                      #括号内容将映射到get方法name参数
    '/info', 'info'
)

class index :
    def GET(self, name):
        return render.index(name)

# 输出json示例
class info :
    def GET(self):
        person = [{'name' : 'denglj', 'age' : 30, 'address' : '莲岳里'}]
        web.header('Content-Type', 'application/json')
        result = denglj.my_crawler.fetchResult()
        for item in result:
            print(item['url'])
        return json.dumps(result)


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()