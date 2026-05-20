import dns.resolver

resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8']

try:
    answers = resolver.resolve('_mongodb._tcp.cluster0.bscwx.mongodb.net', 'SRV')
    for rdata in answers:
        print(f"Host: {rdata.target}, Port: {rdata.port}")
except Exception as e:
    print(f"Error: {e}")
