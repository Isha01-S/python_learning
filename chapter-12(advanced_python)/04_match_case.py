'''match case'''

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "NOT FOUND"
        case 500:
            return "INTERNAL SERVER ERROR"
        case _:
            return "UNKNOWN STATUS"

print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(403))