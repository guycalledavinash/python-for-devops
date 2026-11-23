servers = [
    {"name": "web-01", "status": "healthy"},
    {"name": "api-01", "status": "unhealthy"},
    {"name": "worker-01", "status": "healthy"},
    {"name": "database-01", "status": "unhealthy"},
]

unhealthy_servers = [server for server in servers if server["status"] == "unhealthy"]

print("All servers:")
for server in servers:
    print(f"- {server['name']}: {server['status']}")

print("\nUnhealthy servers:")
for server in unhealthy_servers:
    print(f"- {server['name']}")

print(f"\nTotal unhealthy servers: {len(unhealthy_servers)}")
