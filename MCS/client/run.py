import app_mcs_client

host = "localhost"
port = int(8080)

obj = app_mcs_client._clientobj(host, port)

obj.get_action()

obj.event_loop()