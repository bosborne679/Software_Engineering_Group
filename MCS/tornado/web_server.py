import tornado.ioloop
import tornado.web


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is the Back End Test Page")

class staticRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("html/mcspage.html")


        if self.get_argument("input1") is not None:
            value = self.get_argument("input1")

            print(value)
        else:
            pass

class Application(tornado.web.Application):
    def __init__(self):
        handlers =[
        (r"/",basicRequestHandler),
        (r"/home", staticRequestHandler)
        ]

        tornado.web.Application.__init__(self, handlers)
if __name__ == "__main__":
    app = Application()
    app.listen(8888)
    print("Listening to port 8888")
    tornado.ioloop.IOLoop.current().start()


