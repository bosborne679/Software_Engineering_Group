import server


print(f"Server start up:")

shell = server.app_mcs_server._server_ignition()

print(f"Server loop starting:")

shell.server_engine()