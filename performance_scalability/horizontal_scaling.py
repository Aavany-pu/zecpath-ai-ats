def create_scaling_strategy(service_names):
    if not service_names:
        return {
            "Status": "No Services Available",
            "Services": [],
            "Load Balancing": None,
            "Microservice Scaling": None
        }

    services = []

    for service in service_names:
        services.append({
            "Service": service,
            "Scaling": "Horizontal"
        })

    return {
        "Status": "Horizontal Scaling Strategy Created",
        "Services": services,
        "Load Balancing": "Distribute requests across available service instances",
        "Microservice Scaling": "Add or remove service instances based on workload"
    }