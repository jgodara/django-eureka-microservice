import py_eureka_client.eureka_client as eureka

registry_client, discovery_client = eureka.init(eureka_server="http://192.168.1.3:8761/eureka",
                                                app_name="django-app",
                                                instance_port=9000)
