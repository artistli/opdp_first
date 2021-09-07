demo_map = {

}

global startId
startId = 10
service_message = "provided by service first."
class DemoService(object):

    def __init__(self):
        pass

    def add(self, demo):
        global startId
        if not demo.id:
            demo.id = startId + 1
            startId += 1
        if not demo.serviceProvider:
            demo.serviceProvider = service_message
        else:
            demo.serviceProvider = "%s 。%s" % (demo.serviceProvider, service_message)
        demo_map[demo.id] = demo
        return demo

    def delete(self, id):
        if id in demo_map.keys():
            result = demo_map[id]
            del demo_map[id]
            return result
        return {}

    def get(self, id):
        return demo_map.get(id, {})

    def get_all(self):
        return list(demo_map.values())
